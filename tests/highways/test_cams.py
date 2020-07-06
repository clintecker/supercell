"""Supercell Highway Camera Package Tests"""
# Standard Library
import gzip
from pathlib import Path
import tempfile
import unittest

# Third Party Code
import responses

# Supercell Code
from supercell import highways


class SupercellHighwayCamsTestSuite(unittest.TestCase):
    @responses.activate
    def test_fetch_cam(self):
        responses.add(
            responses.GET,
            "https://i.cotrip.org/dimages/camera",
            body=gzip.compress(b"1234444"),
            status=200,
            headers={"Content-Encoding": "gzip", "Content-Type": "image/jpeg"},
        )
        name, data = highways.cams.fetch_cam("bloop_name:bloop_path")
        self.assertEqual(("bloop_name", b"1234444"), (name, data))

    @responses.activate
    def test_fetch_cam_doesnt_exist(self):
        responses.add(
            responses.GET,
            "https://i.cotrip.org/dimages/camera",
            body=gzip.compress(b"Not Found"),
            status=404,
            headers={"Content-Encoding": "gzip", "Content-Type": "text/plain"},
        )
        with self.assertRaises(ValueError):
            highways.cams.fetch_cam("bloop_name:bloop_path")

    def test_store_cam(self):
        with tempfile.TemporaryDirectory() as d:
            local_path = highways.cams.store_cam(
                name="name", data=b"1234567890", directory=d
            )
        self.assertEqual(
            ("highway-cam-name", ".jpg"), (local_path.stem, local_path.suffix),
        )

    @responses.activate
    def test_download_cam(self):
        responses.add(
            responses.GET,
            "https://i.cotrip.org/dimages/camera",
            body=gzip.compress(b"1234444"),
            status=200,
            headers={"Content-Encoding": "gzip", "Content-Type": "image/jpeg"},
        )
        with tempfile.TemporaryDirectory() as d:
            local_path = Path(highways.cams.download_cam(cam="name:bloop", directory=d))
        self.assertEqual(
            ("highway-cam-name", ".jpg"), (local_path.stem, local_path.suffix),
        )
