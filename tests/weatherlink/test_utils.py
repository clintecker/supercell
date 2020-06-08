# Standard Library
import datetime
import socket
import unittest
from unittest import mock

# Third Party Code
from bitstring import BitStream

# Supercell Code
from tests.context import \
    supercell  # noqa: I202


class SupercellWeatherlinkUtilitiesTestSuite(unittest.TestCase):
    def test_crc16(self):
        bs = BitStream(b"123456789")
        crc = supercell.weatherlink.utils.crc16(
            data=bs,
            crc=0,
            table=supercell.weatherlink.utils.CRC16_TABLE
        )
        self.assertEqual(
            64217,
            crc
        )

    def test_connect(self):
        with mock.patch("socket.socket") as mock_sock_class:
            mock_sock = supercell.weatherlink.utils.connect(
                host="23.23.23.24",
                port=9999
            )
        self.assertTrue(mock_sock_class.called_with(socket.AF_INET, socket.SOCK_STREAM))
        self.assertTrue(mock_sock.connect.called_with(("23.23.23.24", 9999)))

    def test_request(self):
        mock_sock = mock.Mock(spec=socket.socket)
        mock_sock.recv.return_value = bytes([supercell.weatherlink.utils.ACKNOWLEDGED_RESPONSE_CODE, ])
        supercell.weatherlink.utils.request(
            sock=mock_sock,
            body=b"1234567"
        )
        self.assertTrue(
            mock_sock.sendall.called_with(b"1234567")
        )
        self.assertTrue(
            mock_sock.recv.called_with(supercell.weatherlink.utils.RESPONSE_CODE_SIZE)
        )

        mock_sock.recv.return_value = bytes([supercell.weatherlink.utils.NACK_RESPONSE_CODE, ])
        with self.assertRaises(supercell.weatherlink.exceptions.NotAcknowledged):
            supercell.weatherlink.utils.request(
                sock=mock_sock,
                body=b"1234567"
            )

        mock_sock.recv.return_value = bytes([supercell.weatherlink.utils.BAD_CRC_RESPONSE_CODE, ])
        with self.assertRaises(supercell.weatherlink.BadCRC):
            supercell.weatherlink.utils.request(
                sock=mock_sock,
                body=b"1234567"
            )

        mock_sock.recv.return_value = bytes([0xff, ])
        with self.assertRaises(supercell.weatherlink.exceptions.UnknownResponseCode):
            supercell.weatherlink.utils.request(
                sock=mock_sock,
                body=b"1234567"
            )

    def test_receive_data(self):
        mock_sock = mock.Mock(spec=socket.socket)
        mock_sock.recv.return_value = bytes([0xaa, 0xff])

        data = supercell.weatherlink.utils.receive_data(
            sock=mock_sock
        )
        self.assertEqual(
            b"\xaa\xff",
            data
        )
        self.assertTrue(
            mock_sock.recv.called_with(supercell.weatherlink.utils.SOCKET_BUFFER_SIZE)
        )

    def test_make_time(self):
        t = [
            (2044, datetime.time(hour=20, minute=44), None),
            (0, datetime.time(hour=0, minute=0), None),
            (1200, datetime.time(hour=12, minute=0), None),
            (123, datetime.time(hour=1, minute=23), None),
            (2399, None, ValueError),
            (2400, None, ValueError),
            (-1344, None, ValueError)
        ]
        for ts, r, exc in t:
            if r:
                self.assertEqual(r, supercell.weatherlink.utils.make_time(ts))
            elif exc:
                with self.assertRaises(exc):
                    supercell.weatherlink.utils.make_time(ts)

    def test_make_datetime(self):
        t = [
            (BitStream(bytes([0x28, 0xd6])), 1239, datetime.datetime(2020, 6, 22, 12, 39, 0), None),
            (BitStream(bytes([0x28, 0xd6])), 6323, None, ValueError),
            (BitStream(bytes([0xff, 0xb7])), 1213, None, ValueError),
            (BitStream(bytes([0xff, 0xb7])), 2599, None, ValueError)
        ]
        for ds, ts, r, exc in t:
            if r:
                self.assertEqual(r, supercell.weatherlink.utils.make_datetime(ds, ts))
            elif exc:
                with self.assertRaises(exc):
                    supercell.weatherlink.utils.make_datetime(ds, ts)
