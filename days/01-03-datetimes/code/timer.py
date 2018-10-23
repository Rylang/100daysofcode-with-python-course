from datetime import datetime

VALID_COMMANDS = ['start', 'help', 'time', 'lap', 'stop']


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


# def help_command():
#     help_string = "Full list of valid commands: \n\n"
#     for command in VALID_COMMANDS:
#         help_string += "{0}\n".format(command)
#     print(help_string)
#
#
# def time_command(elapsed_time):
#     print("Current elapsed time is: {0}".format(elapsed_time))
#
#
# def lap_command():
#
#
#
# def stop_command(elapsed_time):
#     print("Total elapsed time is: {0}".format(elapsed_time))


def main():
    # Initialize the timer
    sanitise_input("To begin the timer please type 'Start'.", "Start", str)
    start_time = datetime.now()
    print("Timer successfully started!")
    laps = []

    # Request users next action
    while True:
        command = sanitise_input("Please enter a command or type 'Help' for a full list of commands.", type_=str)
        if command == 'start':
            print("The timer has already started, please enter a different command.")
            continue
        elif command == 'help':
            help_string = "Full list of valid commands: \n\n"
            for command in VALID_COMMANDS:
                help_string += "{0}\n".format(command)
            print(help_string)
            continue
        elif command == 'time':
            elapsed_time = str(datetime.now() - start_time)
            print("Current elapsed time is: {0}".format(elapsed_time))
            continue
        elif command == 'lap':
            if not laps:
                laps.append(str(datetime.now() - start_time))
            else:
                laps.append(str(datetime.now() - laps[:-1]))
            print(laps)
        elif command == 'stop':
            elapsed_time = str(datetime.now() - start_time)
            print("Total elapsed time is: {0}".format(elapsed_time))
            break
        else:
            break


main()
