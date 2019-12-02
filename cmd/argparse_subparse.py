# Example of using argparse with sub parsers, useful for
# building interfaces like that of the docker cli

import argparse

def sub1_cmd(args):
    """The command that gets called if user uses the sub1 command on the commandline"""
    print("This is sub1")
    print("You passed args:", str(args))

def sub2_cmd(args):
    """The command that gets called if user uses the sub2 command on the commandline"""
    print("This is sub2")
    print("You passed args:", str(args))

def run():
    # Create a parser object
    parser = argparse.ArgumentParser(description='Example of using argparse with subcommands')
    # Add a subparser to the parser
    subparsers = parser.add_subparsers()

    # Use the subparser to create sub parser (duh)
    sub1 = subparsers.add_parser('cmd1', help='Subcommand 1')
    # Some simple arguments, use the sub1 parser like any normal ArgParser
    sub1.add_argument('-a',type=str, default='option', help='cmd1 a option')
    sub1.add_argument('-b',type=int, default=42, help='cmd1 b option')
    # Set a function to be called if the user picks command 'sub1'
    # this is a trick from the documentation. We just put in our own default
    # variable and use it to store a function reference to use.
    sub1.set_defaults(cmd_func=sub1_cmd)

    # Do the same for another command. Add as many of these as you like
    sub2 = subparsers.add_parser('cmd2', help='Subcommand 2')
    sub2.add_argument('-a',type=str, default='optiona', help='cmd2 a option')
    sub2.add_argument('-b',type=str, default='optionb', help='cmd2 b option')
    sub2.add_argument('-c',type=str, default='optionc', help='cmd2 c option')
    # Use a different function if user picks 'sub2' command
    sub2.set_defaults(cmd_func=sub2_cmd)

    # ok, parse out the args provided in sys.argv (per documentation)
    args = parser.parse_args()

    # If the user picked no command at the command line, we won't have
    # a cmd_func (unless you add one with parser.set_defaults(cmd_func=...))
    # So, if that's the case, just print the help and quit
    if 'cmd_func' in args:
        # Provide the args that were parsed to the sub command we're calling
        args.cmd_func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    run()
