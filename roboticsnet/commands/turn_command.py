from roboticsnet.commands.commandable import Commandable

class TurnCommand(Commandable):
    """
    author: psyomn
    """

    def __init__(self, value, hooks):
        self.magnitude = value
        self.hooks = hooks

    def execute(self):
        self.hooks.turnHook()
