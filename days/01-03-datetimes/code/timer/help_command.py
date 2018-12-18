from .command_abc import AbsCommand
from .timer_command_abc import AbsTimerCommand

VALID_COMMANDS = ['start', 'help', 'time', 'lap', 'stop']


class HelpCommand(AbsCommand, AbsTimerCommand):
    name = 'Help'
    description = 'Prints help commands'

    def __init__(self):
        pass

    def execute(self):
        help_string = "Full list of valid commands: \n\n"
        for command in VALID_COMMANDS:
            help_string += "{0}\n".format(command)
        print(help_string)
