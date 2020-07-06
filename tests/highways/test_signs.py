"""
Highway Signs Tests
"""
# Standard Library
import gzip
from pathlib import Path
import tempfile
import unittest

# Third Party Code
import responses

# Supercell Code
import supercell


class SupercellHighwaySignsTests(unittest.TestCase):
    @responses.activate
    def test_get_all_signs(self):
        responses.add(
            responses.GET,
            "https://cotrip.org/device/getDMS.do",
            json={"DMSDetails": {"DMS": [{}, {}, {}]}},
            status=200,
        )
        all_signs = supercell.highways.signs.get_all_signs()
        self.assertEqual(3, len(all_signs))

    @responses.activate
    def test_get_all_signs_bad_response(self):
        responses.add(
            responses.GET,
            "https://cotrip.org/device/getDMS.do",
            status=500,
            body="Server Error!",
        )
        with self.assertRaises(Exception):
            supercell.highways.signs.get_all_signs()

    @responses.activate
    def test_get_sign_message_from_internet(self):
        responses.add(
            responses.GET,
            "https://cotrip.org/device/getDMS.do",
            json={
                "DMSDetails": {
                    "DMS": [
                        {"DMSId": "XXXX", "MessageImage": "/bloop/imageXXXX.jpg",},
                        {"DMSId": "YYYY", "MessageImage": "/bloop/imageYYYY.jpg",},
                        {"DMSId": "ZZZZ", "MessageImage": "/bloop/imageZZZZ.jpg",},
                    ]
                }
            },
            status=200,
        )
        message_url = supercell.highways.signs.get_sign_message(
            dms_id="XXXX", signs=None
        )
        self.assertEqual("https://i.cotrip.org/bloop/imageXXXX.jpg", message_url)

        with self.assertRaises(ValueError):
            supercell.highways.signs.get_sign_message("AAAA")

        sign_url = supercell.highways.signs.get_sign_message(
            "QQQQ",
            signs=[
                {"DMSId": "QQQQ", "MessageImage": "/bloop/imageQQQQ.jpg",},
                {"DMSId": "YYYY", "MessageImage": "/bloop/imageYYYY.jpg",},
                {"DMSId": "ZZZZ", "MessageImage": "/bloop/imageZZZZ.jpg",},
            ],
        )

        self.assertEqual("https://i.cotrip.org/bloop/imageQQQQ.jpg", sign_url)

    @responses.activate
    def test_fetch_sign_image(self):
        responses.add(
            responses.GET,
            "https://cotrip.org/device/getDMS.do",
            json={
                "DMSDetails": {
                    "DMS": [
                        {"DMSId": "XXXX", "MessageImage": "/bloop/imageXXXX.jpg",},
                        {"DMSId": "YYYY", "MessageImage": "/bloop/imageYYYY.jpg",},
                        {"DMSId": "ZZZZ", "MessageImage": "/bloop/imageZZZZ.jpg",},
                    ]
                }
            },
            status=200,
        )

        responses.add(
            responses.GET,
            "https://i.cotrip.org/bloop/imageZZZZ.jpg",
            body=gzip.compress(b"JFIFXXXXX"),
            status=200,
            headers={"Content-Encoding": "gzip", "Content-Type": "image/jpeg"},
        )

        responses.add(
            responses.GET,
            "https://i.cotrip.org/bloop/imageYYYY.jpg",
            body="Server Error",
            status=501,
        )

        data = supercell.highways.signs.fetch_sign_image(sign_id="ZZZZ", all_signs=None)

        self.assertEqual(b"JFIFXXXXX", data)

        with self.assertRaises(ValueError):
            supercell.highways.signs.fetch_sign_image(sign_id="YYYY", all_signs=None)

    def test_store_sign_image(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d, "bloop.jpg")
            supercell.highways.signs.store_sign_image(data=b"JFIFXXXXX", local_path=p)
            self.assertEqual(b"JFIFXXXXX", p.read_bytes())
