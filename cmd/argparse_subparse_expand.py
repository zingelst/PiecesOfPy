# Example of using argparse with sub parsers, useful for
# building interfaces like that of the docker cli

# This version expands the args Namespace and uses the arguments to fill
# out the arguments of a function, making the function calls more natural

import argparse

# Here the kwargs is used to capture all of the arguments in the args Namespace
# that are not caled out specifically as parameters. These, for example, could
# be common arguments to the main parser that you can optionally use in the sub-function
def sub1_cmd(aoption, boption, coption, **kwargs):
    """The command that gets called if user uses the sub1 command on the commandline"""
    print("This is sub1")
    print("You passed aoption:", aoption)
    print("You passed boption:", boption)
    print("You passed coption:", coption)
    print("Other args: ", str(kwargs))

def sub2_cmd(infile, outfile, **kwargs):
    """The command that gets called if user uses the sub2 command on the commandline"""
    print("This is sub2")
    print("You passed infile", infile)
    print("You passed outfile", outfile)
    print("Other args: ", str(kwargs))

def run():
    # Create a parser object
    parser = argparse.ArgumentParser(description='Example of using argparse with subcommands')
    parser.add_argument('-m', '--main_parser_opt', type=str, default=None, help='An optional argument on the main parser')

    # Add a subparser to the parser
    subparsers = parser.add_subparsers()

    # Use the subparser to create sub parser (duh)
    sub1 = subparsers.add_parser('cmd1', help='Subcommand 1')
    # Some simple arguments, use the sub1 parser like any normal ArgParser
    sub1.add_argument('-a', '--aoption', type=str, default='option', help='cmd1 a option')
    sub1.add_argument('-b', '--boption', type=int, default=42, help='cmd1 b option')
    sub1.add_argument('-c', '--coption', type=int, default=42, help='cmd1 c option')
    # Set a function to be called if the user picks command 'sub1'
    # this is a trick from the documentation. We just put in our own default
    # variable and use it to store a function reference to use.
    sub1.set_defaults(cmd_func=sub1_cmd)

    # Do the same for another command. Add as many of these as you like
    sub2 = subparsers.add_parser('cmd2', help='Subcommand 2')
    sub2.add_argument('-i', '--infile', type=str, default='infile', help='cmd2 input option')
    sub2.add_argument('-o', '--outfile', type=str, default='outfile', help='cmd2 output option')
    # Use a different function if user picks 'sub2' command
    sub2.set_defaults(cmd_func=sub2_cmd)

    # ok, parse out the args provided in sys.argv (per documentation)
    args = parser.parse_args()

    # If the user picked no command at the command line, we won't have
    # a cmd_func (unless you add one with parser.set_defaults(cmd_func=...))
    # So, if that's the case, just print the help and quit
    if 'cmd_func' in args:
        # Provide the args that were parsed to the sub command we're calling
        # the vars() function in Python will return the __dict__ component of 
        # any object with a __dict__ in it. The parse_args() function of argparse
        # will return a Namespace object which contains entries for all of the command
        # line options that were passed to the script. The ** is then standard Python
        # way of expanding the key-value pairs in a dictionary to invoke the keyword
        # arguments of a function. The keys in the dictionary will map to the argument
        # names in the called function. Anything else will be placed in the kwargs argument
        # of our sub-command functions, sub1_cmd and sub2_cmd
        args.cmd_func(**vars(args))
    else:
        parser.print_help()

if __name__ == "__main__":
    run()
