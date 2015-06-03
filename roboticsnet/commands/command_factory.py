from roboticsnet.commands.command_validator import validate
from roboticsnet.commands.move_command import MoveCommand
from roboticsnet.commands.turn_command import TurnCommand
from roboticsnet.commands.reverse_command import ReverseCommand
from roboticsnet.commands.queryproc_command import QueryprocCommand
from roboticsnet.gateway_constants import *

class CommandFactory:
    """
    author: psyomn

    Consumes strings or byte arrays sent to service, and returns a command
    specific to that request
    """

    @staticmethod
    def makeFromByteArray(rcv_bytes, conn, session):
        """
        Parameters:
            rcv_bytes - the information that the client sends

            conn - the connection back to the client, which sent some request
              (some commands might need this information, as the protocol
              dictates a two-way communication channel).

            session - the current information that should be known about the
              status of the rover. See session.py
        """
        cmd = ord(rcv_bytes[0])
        params = rcv_bytes[1:]

        if cmd == ROBOTICSNET_COMMAND_MOVE:
            return CommandFactory._makeMove(params)

        elif cmd == ROBOTICSNET_COMMAND_REVERSE:
            return CommandFactory._makeReverse(params)

        elif cmd == ROBOTICSNET_COMMAND_TURN:
            return CommandFactory._makeTurn(params)

        elif cmd == ROBOTICSNET_COMMAND_QUERYPROC:
            return QueryprocCommand(conn, session)

    @staticmethod
    def _makeMove(rcv_bytes):
        magnitude = ord(rcv_bytes[0])
        return MoveCommand(magnitude)

    @staticmethod
    def _makeTurn(rcv_bytes):
        magnitude = ord(rcv_bytes[0])
        return TurnCommand(magnitude)

    @staticmethod
    def _makeReverse(rcv_bytes):
        magnitude = ord(rcv_bytes[0])
        return ReverseCommand(magnitude)

