import pytest
from unittest.mock import MagicMock, patch
from calculator_server.UDP_server import main


def _set_up_mocked_calculator_socket(recv_value=None):
    socket_instance = MagicMock(name="SocketInstance")
    socket_instance.recvfrom = MagicMock(return_value=(recv_value, 'ip'))

    socket_context = MagicMock(name="SocketContext")
    socket_context.__enter__ = MagicMock(return_value=socket_instance)

    socket_mock = MagicMock()
    socket_mock.socket = MagicMock(name="SocketModule", return_value=socket_context)

    return socket_mock


def test_that_received_binary_expression_returns_correct_binary_result():
    socket_mock = _set_up_mocked_calculator_socket(b'2+2')

    with patch('calculator_server.UDP_server.socket', new=socket_mock):
        raise NotImplementedError('False-positive. I need to figure out how to not stuck in the loop of main().')
