"""
Highway Cameras
"""
# Standard Library
import argparse
import functools
import io
import logging
from pathlib import Path
import shutil
import sys
from typing import IO, Sequence, Tuple
from urllib.parse import urlunparse

# Third Party Code
import requests

HOST = "i.cotrip.org"
PATH = "/dimages/camera"
QUERY_PARAM = "imageURL"

logger = logging.getLogger(__name__)


def fetch_cam(cam: str) -> Tuple[str, bytes]:
    """
    Fetches an frame from a camera.
    """
    name, cam_path = cam.split(":")
    logger.info("Downloading Camera %s to %s", cam_path, name)
    image_url = urlunparse(
        ["https", HOST, PATH, None, "%s=%s" % (QUERY_PARAM, cam_path), None]
    )
    with requests.get(image_url, stream=True) as r:
        if r.status_code == requests.codes.ok:
            r.raw.read = functools.partial(r.raw.read, decode_content=True)
            return name, r.content
    raise ValueError("Could not fetch that camera.")


def store_cam(name: str, data: bytes, directory: str) -> Path:
    """
    Stores data to a local file.
    """
    local_path = Path(directory, "highway-cam-%s.jpg" % name)
    with open(local_path, "wb") as f:
        source: IO = io.BytesIO(data)
        dest: IO = f
        shutil.copyfileobj(source, dest)
    return local_path


def download_cam(cam: str, directory: str) -> str:
    """
    Fetches and then stores a camera image.
    """
    name, data = fetch_cam(cam)
    return str(store_cam(name, data, directory).resolve())


def main(output: IO, args: Sequence[str]) -> None:
    """The CLI portion of this script."""
    parser = argparse.ArgumentParser(description="Download highway cameras.")
    parser.add_argument("--cam", "-c", dest="cams", action="append")
    parser.add_argument("--directory", "-d", dest="directory")
    parser.add_argument("--quiet", dest="quiet", action="store_true", default=False)
    parser.add_argument("--verbose", dest="verbose", action="store_true", default=False)

    parsed_args = parser.parse_args(args=args)

    if parsed_args.quiet:
        log_level = logging.ERROR
    elif parsed_args.verbose:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO

    logger.setLevel(log_level)
    logger.info("Downloading Highway Cameras")

    for path in [download_cam(cam, parsed_args.directory) for cam in parsed_args.cams]:
        output.write(path + "\n")
    output.flush()


if __name__ == "__main__":
    main(sys.stdout, args=sys.argv[1:])
