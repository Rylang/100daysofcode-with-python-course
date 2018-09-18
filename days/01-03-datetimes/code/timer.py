from datetime import datetime

VALID_COMMANDS = ['help', 'lap', 'time', 'stop']


def sanitise_input(prompt, validation_string=None, type_=None):
    while True:
        user_input = input(prompt)
        if type_ is not None:
            try:
                type_(user_input)
            except ValueError:
                print("Input must be {0}.".format(type_.__name__))
                continue
        if validation_string is not None:
            if user_input.lower() != validation_string.lower():
                print("Invalid command! {0}".format(prompt))
                continue
        elif user_input not in VALID_COMMANDS:
            print("Invalid command! Type 'help' for a list of valid commands.")
            continue
        return user_input.lower()


def help_command():
    help_string = "Full list of valid commands: \n\n"
    for command in VALID_COMMANDS:
        help_string += "{0}\n".format(command)
    print(help_string)


def time_command(elapsed_time):
    print("Current elapsed time is: {0}".format(elapsed_time))


def main():
    # Initialize the timer
    sanitise_input("To begin the timer please type 'Start'.", "Start", str)
    start_time = datetime.now()
    print("Timer successfully started!")

    # Request users next action
    while True:
        command = sanitise_input("Please enter a command or type 'Help' for a full list of commands.", type_=str)
        if command == 'help':
            help_command()
            continue
        if command == 'time':
            elapsed_time = str(datetime.now() - start_time)
            time_command(elapsed_time)
            continue
        else:
            break


main()
