"""
Gets highway signs.
"""
# Standard Library
import argparse
import functools
import io
import logging
from pathlib import Path
import shutil
import sys
from typing import Dict, IO, List, Optional
from urllib.parse import urlunparse

# Third Party Code
import requests

DMS_URL = "https://cotrip.org/device/getDMS.do"
IMAGE_HOST = "i.cotrip.org"

logger = logging.getLogger(__name__)


def get_all_signs() -> List[Dict]:
    """
    Gets all signs.
    """
    response = requests.get(DMS_URL)
    if response.status_code == requests.codes.ok:
        return response.json()["DMSDetails"]["DMS"]
    raise Exception("Couldn't fetch highway data.")


def get_sign_message(dms_id: str, signs: Optional[List[Dict]] = None) -> str:
    """
    Gets a particular sign's image url.
    """
    signs = signs or get_all_signs()
    for s in signs:
        if s["DMSId"] == dms_id:
            return urlunparse(
                ["https", IMAGE_HOST, s["MessageImage"], None, None, None]
            )
    raise ValueError("Could not find that sign.")


def fetch_sign_image(sign_id: str, all_signs: Optional[List[Dict]] = None) -> bytes:
    with requests.get(get_sign_message(sign_id, all_signs), stream=True) as r:
        if r.status_code == requests.codes.ok:
            r.raw.read = functools.partial(r.raw.read, decode_content=True)
            return r.content
    raise ValueError("Could not fetch sign.")


def store_sign_image(data: bytes, local_path: Path) -> None:
    with local_path.open("wb") as f:
        source: IO = io.BytesIO(data)
        dest: IO = f
        shutil.copyfileobj(source, dest)


def main(args: List[str]) -> None:
    parser = argparse.ArgumentParser(description="Download highway signs.")
    parser.add_argument("--sign", "-s", dest="signs", action="append")
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

    # highways.cams.fetch_cam and store_cam could be generalized to replace
    # the code below as well.
    logger.info("Downloading Highway Signs")
    all_signs = get_all_signs()
    for sign in parsed_args.signs:
        sign_id, name = sign.split(":")
        logger.info("Downloading DMS ID #%s to %s", sign_id, name)
        try:
            store_sign_image(
                data=fetch_sign_image(sign_id=sign_id, all_signs=all_signs),
                local_path=Path(parsed_args.directory, "highway-sign-%s.gif" % name),
            )
        except ValueError:
            logger.error("Could not download %s:%s", sign_id, name)
            continue


if __name__ == "__main__":
    main(sys.argv[1:])
