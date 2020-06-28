from unittest.mock import Mock


class Board:

    setmode = Mock()
    setup = Mock()


class GPIO:
    BOARD = Mock()

    IN = Mock()
    OUT = Mock()

    PUD_UP = Mock()

    HIGH = Mock()
    LOW = Mock()

    input = Mock()

    output = Mock()

    cleanup = Mock()
