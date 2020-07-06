# Standard Library
import socket
import unittest
from unittest import mock

# Supercell Code
import supercell


class SupercellWeatherLinkTestSuite(unittest.TestCase):
    def test_get_current(self):
        mock_sock = mock.Mock(spec=socket.socket)
        mock_sock.recv.side_effect = [
            bytes([supercell.weatherlink.utils.ACKNOWLEDGED_RESPONSE_CODE,]),
            b"LOO\xc4\x00\x1d\x01\xe2r~\x03\x12\xf3\x02\x05\x07\xcf\x00\xff\xff",
            b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff$\xff\xff\xff",
            b"\xff\xff\xff\xff\x00\x00\xff\xff\x7f\x00\x00\xff\xff\x00\x00\x04",
            b"\x00^\x01\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\x00",
            b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
            b"\x005\x03\x07\xad\x17\x02\xea\x07\n\r\xf3\x7f",
        ]
        with mock.patch("socket.socket") as mock_socket_class:
            mock_socket_class.return_value = mock_sock
            current_data = supercell.weatherlink.get_current(
                host="111.111.222.222", port=6979
            )
        self.assertEqual(99, len(current_data))
        mock_socket_class.assert_called_with(socket.AF_INET, socket.SOCK_STREAM)
        mock_sock.sendall.assert_called_with(b"LOOP 1\n")
        self.assertEqual(
            mock_sock.recv.call_args_list,
            [
                mock.call(supercell.weatherlink.utils.RESPONSE_CODE_SIZE),
                mock.call(supercell.weatherlink.utils.SOCKET_BUFFER_SIZE),
                mock.call(supercell.weatherlink.utils.SOCKET_BUFFER_SIZE),
                mock.call(supercell.weatherlink.utils.SOCKET_BUFFER_SIZE),
                mock.call(supercell.weatherlink.utils.SOCKET_BUFFER_SIZE),
                mock.call(supercell.weatherlink.utils.SOCKET_BUFFER_SIZE),
                mock.call(supercell.weatherlink.utils.SOCKET_BUFFER_SIZE),
            ],
        )
        mock_sock.close.assert_called_once()

    def test_get_current_bad_response(self):
        mock_sock = mock.Mock(spec=socket.socket)
        mock_sock.recv.side_effect = [
            bytes([supercell.weatherlink.utils.BAD_CRC_RESPONSE_CODE,]),
            bytes([supercell.weatherlink.utils.NACK_RESPONSE_CODE,]),
            bytes([0xFF,]),
        ]
        with mock.patch("socket.socket") as mock_socket_class:
            mock_socket_class.return_value = mock_sock
            with self.assertRaises(supercell.weatherlink.exceptions.BadCRC):
                supercell.weatherlink.get_current(host="111.111.222.222", port=6979)
            with self.assertRaises(supercell.weatherlink.exceptions.NotAcknowledged):
                supercell.weatherlink.get_current(host="111.111.222.222", port=6979)
            with self.assertRaises(
                supercell.weatherlink.exceptions.UnknownResponseCode
            ):
                supercell.weatherlink.get_current(host="111.111.222.222", port=6979)
        self.assertEqual(
            [mock.call(), mock.call(), mock.call()], mock_sock.close.call_args_list
        )

    def test_get_current_request_socket_timeout(self):
        mock_sock = mock.Mock(spec=socket.socket)
        mock_sock.recv.side_effect = socket.timeout
        with mock.patch("socket.socket") as mock_socket_class:
            mock_socket_class.return_value = mock_sock
            with self.assertRaises(supercell.weatherlink.exceptions.NotAcknowledged):
                supercell.weatherlink.get_current(host="111.111.222.222", port=6979)
        mock_sock.close.assert_called_once()

    def test_get_current_data_socket_timeout(self):
        mock_sock = mock.Mock(spec=socket.socket)
        mock_sock.recv.side_effect = [
            bytes([supercell.weatherlink.utils.ACKNOWLEDGED_RESPONSE_CODE,]),
            socket.timeout,
        ]
        with mock.patch("socket.socket") as mock_socket_class:
            mock_socket_class.return_value = mock_sock
            with self.assertRaises(supercell.weatherlink.exceptions.NotAcknowledged):
                supercell.weatherlink.get_current(host="111.111.222.222", port=6979)
        mock_sock.close.assert_called_once()

    @mock.patch("supercell.weatherlink.time.sleep")
    def test_get_current_condition(self, mock_sleep):
        with mock.patch("supercell.weatherlink.get_current") as mock_get_current:
            mock_get_current.return_value = (
                b"LOO\xc4\x00\x1d\x01\xe2r~\x03\x12\xf3\x02\x05\x07\xcf\x00"
                b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
                b"\xff$\xff\xff\xff\xff\xff\xff\xff\x00\x00\xff\xff\x7f\x00"
                b"\x00\xff\xff\x00\x00\x04\x00^\x01\x00\x00\x00\x00\x00\x00"
                b"\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00"
                b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x005\x03\x07\xad"
                b"\x17\x02\xea\x07\n\r\xf3\x7f"
            )
            supercell.weatherlink.get_current_condition(
                host="111.111.222.222", port=6979
            )

        self.assertFalse(mock_sleep.called)

    @mock.patch("supercell.weatherlink.time.sleep")
    def test_get_current_condition_bad_responses(self, mock_sleep):
        with mock.patch("supercell.weatherlink.get_current") as mock_get_current:
            mock_get_current.side_effect = [
                supercell.weatherlink.exceptions.NotAcknowledged,
                (
                    b"LOO\xc4\x00\x1d\x01\xe2r~\x03\x12\xf3\x02\x05\x07\xcf\x00"
                    b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
                    b"\xff$\xff\xff\xff\xff\xff\xff\xff\x00\x00\xff\xff\x7f\x00"
                    b"\x00\xff\xff\x00\x00\x04\x00^\x01\x00\x00\x00\x00\x00\x00"
                    b"\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00"
                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x005\x03\x07\xad"
                    b"\x17\x02\xea\x07\n\r\xf3\x7f"
                ),
            ]
            supercell.weatherlink.get_current_condition(
                host="111.111.222.222", port=6979
            )
        mock_sleep.assert_called_once()
        mock_sleep.assert_called_with(0.1)

    @mock.patch("supercell.weatherlink.time.sleep")
    def test_get_current_condition_failure(self, mock_sleep):
        with mock.patch("supercell.weatherlink.get_current") as mock_get_current:
            mock_get_current.side_effect = [
                supercell.weatherlink.exceptions.BadCRC,
                supercell.weatherlink.exceptions.NotAcknowledged,
                supercell.weatherlink.exceptions.BadCRC,
            ]
            with self.assertRaises(supercell.weatherlink.exceptions.BadCRC):
                supercell.weatherlink.get_current_condition(
                    host="111.111.222.222", port=6979
                )

        self.assertEqual([mock.call(0.1), mock.call(1.0),], mock_sleep.call_args_list)
