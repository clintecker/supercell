"""Supercell Package Tests"""
# Standard Library
import datetime
import tempfile
import unittest

# Third Party Code
import responses

# Supercell Code
from supercell import goes


class SupercellGoesTestSuite(unittest.TestCase):
    def test_get_image_data(self):
        d = goes.get_image_data(
            "https:/doesnt.matter.com/GOES16/ABI/SECTOR/sec/Band/20201011012_GOES16-ABI-sec-band-600x600.jpg"
        )
        self.assertEqual(
            {
                "t_year": 2020,
                "t_daynum": 101,
                "t_hour": "10",
                "t_minute": "12",
                "i_width": 600,
                "i_height": 600,
                "sat_num": 16,
                "sector": "sec",
                "band": "Band",
            },
            d,
        )

    def test_get_image_data_bad_url(self):
        d = goes.get_image_data("https:/doesnt.matter.com/something_different.jpg")
        self.assertEqual({}, d)

    @responses.activate
    def test_does_exist(self):
        responses.add(
            method=responses.HEAD, url="https://example.com/bloop.jpg", status=200
        )
        responses.add(
            method=responses.HEAD, url="https://example.com/nope.png", status=404
        )
        self.assertTrue(goes.does_exist("https://example.com/bloop.jpg"))
        self.assertFalse(goes.does_exist("https://example.com/nope.png"))

    def test_image_url_from_data(self):
        d = goes.get_image_data(
            "https:/doesnt.matter.com/GOES16/ABI/SECTOR/sec/Band/20201011012_GOES16-ABI-sec-band-600x600.jpg"
        )
        d["i_width"] = 2100
        d["i_height"] = 2100
        self.assertEqual(
            "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/sec/Band/20201011012_GOES16-ABI-sec-Band-2100x2100"
            ".jpg",
            goes.image_url_from_data(d),
        )

    def test_in_cache(self):
        with tempfile.NamedTemporaryFile(mode="r") as f:
            f_parts = f.name.split("/")
            directory = "/".join(f_parts[:-1])
            key = f_parts[-1]
            full_key = goes.in_cache(key=key, directory=directory)
        self.assertEqual(f.name, str(full_key))

        with self.assertRaises(ValueError):
            goes.in_cache(key="the_key.txt", directory="/tmp")

        with self.assertRaises(ValueError):
            goes.in_cache(key="the_key.txt", directory="/tmp/bloop")

    def test_store_in_cache(self):
        with tempfile.TemporaryDirectory() as d:
            goes.store_in_cache(key="bloop.txt", directory=d, data=b"1234567890")
            goes.in_cache(key="bloop.txt", directory=d)
        # After context, file is deleted, so no longer is in cache
        with self.assertRaises(ValueError):
            goes.in_cache(key="bloop.txt", directory=d)

    @responses.activate
    def test_full_day_images(self):
        html = """<html>
<head><title>Index of /cdn02/GOES/data/GOES16/ABI/SECTOR/nr/GEOCOLOR/</title></head>
<body>
<h1>Index of /cdn02/GOES/data/GOES16/ABI/SECTOR/nr/GEOCOLOR/</h1><hr><pre><a href="../">../</a>
<a href="1200x1200.jpg">1200x1200.jpg</a>                                      01-Jun-2020 20:03             1227726
<a href="20201222001_GOES16-ABI-nr-GEOCOLOR-1200x1200.jpg">20201222001_GOES16-ABI-nr-GEOCOLOR-1200x1200.jpg</a>
   28-May-2020 20:07             1313965
<a href="20201222001_GOES16-ABI-nr-GEOCOLOR-2400x2400.jpg">20201222001_GOES16-ABI-nr-GEOCOLOR-2400x2400.jpg</a>
   28-May-2020 20:07             4457998
<a href="20201222001_GOES16-ABI-nr-GEOCOLOR-300x300.jpg">20201222001_GOES16-ABI-nr-GEOCOLOR-300x300.jpg</a>
     28-May-2020 20:07              105850
<a href="20201222001_GOES16-ABI-nr-GEOCOLOR-600x600.jpg">20201222001_GOES16-ABI-nr-GEOCOLOR-600x600.jpg</a>
     28-May-2020 20:07              378507
<a href="20201222006_GOES16-ABI-nr-GEOCOLOR-1200x1200.jpg">20201222006_GOES16-ABI-nr-GEOCOLOR-1200x1200.jpg</a>
   28-May-2020 20:11             1316732
<a href="20201222006_GOES16-ABI-nr-GEOCOLOR-2400x2400.jpg">20201222006_GOES16-ABI-nr-GEOCOLOR-2400x2400.jpg</a>
   28-May-2020 20:11             4470444
<a href="20201222006_GOES16-ABI-nr-GEOCOLOR-300x300.jpg">20201222006_GOES16-ABI-nr-GEOCOLOR-300x300.jpg</a>
     28-May-2020 20:11              106199
<a href="20201222006_GOES16-ABI-nr-GEOCOLOR-600x600.jpg">20201222006_GOES16-ABI-nr-GEOCOLOR-600x600.jpg</a>
     28-May-2020 20:11              379714
<a href="20201222011_GOES16-ABI-nr-GEOCOLOR-1200x1200.jpg">20201222011_GOES16-ABI-nr-GEOCOLOR-1200x1200.jpg</a>
   28-May-2020 20:16             1320366
<a href="2400x2400.jpg">2400x2400.jpg</a>                                      01-Jun-2020 20:03             4124628
<a href="600x600.jpg">600x600.jpg</a>                                        01-Jun-2020 20:03              361617
<a href="GOES16-NR-GEOCOLOR-600x600.gif">GOES16-NR-GEOCOLOR-600x600.gif</a>                     01-Jun-2020 20:00
            13666927
<a href="latest.jpg">latest.jpg</a>                                         01-Jun-2020 20:03             4124628
<a href="thumbnail.jpg">thumbnail.jpg</a>                                      01-Jun-2020 20:03              103347
</pre><hr></body>
</html>"""

        first_day_html = """<html>
<head><title>Index of /cdn02/GOES/data/GOES16/ABI/SECTOR/yy/GEOCOLOR/</title></head>
<body>
<h1>Index of /cdn02/GOES/data/GOES16/ABI/SECTOR/yy/GEOCOLOR/</h1><hr><pre><a href="../">../</a>
<a href="1200x1200.jpg">1200x1200.jpg</a>                                      01-Jun-2020 20:03             1227726
<a href="202012001_GOES16-ABI-yy-GEOCOLOR-1200x1200.jpg">202012001_GOES16-ABI-yy-GEOCOLOR-1200x1200.jpg</a>
   28-May-2020 20:07             1313965
<a href="202012001_GOES16-ABI-yy-GEOCOLOR-2400x2400.jpg">202012001_GOES16-ABI-yy-GEOCOLOR-2400x2400.jpg</a>
   28-May-2020 20:07             4457998
<a href="202012001_GOES16-ABI-yy-GEOCOLOR-300x300.jpg">202012001_GOES16-ABI-yy-GEOCOLOR-300x300.jpg</a>
  28-May-2020 20:07              105850
<a href="20193662001_GOES16-ABI-yy-GEOCOLOR-600x600.jpg">202012001_GOES16-ABI-yy-GEOCOLOR-600x600.jpg</a>
  28-May-2020 20:07              378507
<a href="20193662306_GOES16-ABI-yy-GEOCOLOR-1200x1200.jpg">202012006_GOES16-ABI-yy-GEOCOLOR-1200x1200.jpg</a>
   28-May-2020 20:11             1316732
<a href="20193662306_GOES16-ABI-yy-GEOCOLOR-2400x2400.jpg">202012006_GOES16-ABI-yy-GEOCOLOR-2400x2400.jpg</a>
   28-May-2020 20:11             4470444
<a href="20193662306_GOES16-ABI-yy-GEOCOLOR-300x300.jpg">202012006_GOES16-ABI-yy-GEOCOLOR-300x300.jpg</a>
  28-May-2020 20:11              106199
<a href="20193662006_GOES16-ABI-yy-GEOCOLOR-600x600.jpg">202012006_GOES16-ABI-yy-GEOCOLOR-600x600.jpg</a>
  28-May-2020 20:11              379714
<a href="20193662311_GOES16-ABI-yy-GEOCOLOR-1200x1200.jpg">202012011_GOES16-ABI-yy-GEOCOLOR-1200x1200.jpg</a>
   28-May-2020 20:16             1320366
<a href="2400x2400.jpg">2400x2400.jpg</a>                                      01-Jun-2020 20:03             4124628
<a href="600x600.jpg">600x600.jpg</a>                                        01-Jun-2020 20:03              361617
<a href="GOES16-yy-GEOCOLOR-600x600.gif">GOES16-yy-GEOCOLOR-600x600.gif</a>                     01-Jun-2020 20:00
            13666927
<a href="latest.jpg">latest.jpg</a>                                         01-Jun-2020 20:03             4124628
<a href="thumbnail.jpg">thumbnail.jpg</a>                                      01-Jun-2020 20:03              103347
</pre><hr></body>
</html>"""

        responses.add(
            responses.GET,
            "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/nr/GEOCOLOR/",
            body=html,
            status=200,
        )
        responses.add(
            responses.GET,
            "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/xx/GEOCOLOR/",
            body=None,
            status=500,
        )
        responses.add(
            responses.GET,
            "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/yy/GEOCOLOR/",
            body=first_day_html,
        )

        urls = goes.full_day_images(
            sat="G16",
            sector="nr",
            band="GEOCOLOR",
            size=1200,
            anchor_datetime=datetime.datetime(2020, 5, 1, 20, 30, 21),
        )
        self.assertEqual(
            [
                "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/nr/GEOCOLOR/20201222001_GOES16-ABI-nr-GEOCOLOR"
                "-1200x1200.jpg",
                "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/nr/GEOCOLOR/20201222006_GOES16-ABI-nr-GEOCOLOR"
                "-1200x1200.jpg",
                "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/nr/GEOCOLOR/20201222011_GOES16-ABI-nr-GEOCOLOR"
                "-1200x1200.jpg",
            ],
            urls,
        )

        self.assertEqual(
            [],
            goes.full_day_images(
                sat="G16",
                sector="xx",
                band="GEOCOLOR",
                size=1200,
                anchor_datetime=datetime.datetime(2020, 5, 1, 20, 30, 21),
            ),
        )
        self.maxDiff = 1024
        u = goes.full_day_images(
            sat="G16",
            sector="yy",
            band="GEOCOLOR",
            size=1200,
            anchor_datetime=datetime.datetime(2020, 1, 1, 20, 30, 21),
        )
        self.assertEqual(
            [
                "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/yy/GEOCOLOR/20193662306_GOES16-ABI-yy-"
                "GEOCOLOR-1200x1200.jpg",
                "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/yy/GEOCOLOR/20193662311_GOES16-ABI-yy-"
                "GEOCOLOR-1200x1200.jpg",
                "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/yy/GEOCOLOR/202012001_GOES16-ABI-yy-"
                "GEOCOLOR-1200x1200.jpg",
                "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/yy/GEOCOLOR/202012006_GOES16-ABI-yy-"
                "GEOCOLOR-1200x1200.jpg",
                "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/yy/GEOCOLOR/202012011_GOES16-ABI-yy-"
                "GEOCOLOR-1200x1200.jpg",
            ],
            u,
        )
