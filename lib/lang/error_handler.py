"""
[error_handler.py]

Describe errors.
"""



from lib.verbs import verbs

class ErgonomicaError(Exception):
    """Base class for exceptions in this module."""
    pass

    
def cmd_check(i):
    """Intelligent command checking (return description of error)."""

    command = i[0]

    if "(map)" in i[0]:
        return True
    
    # check command (number of commands and if the commands exist)
    if len(i[0][0]) != 1:
        return "[ergo: syntaxerror]: Wrong number of commands. Should be only one."
    else:
        if command[0][0] not in verbs.verbs:
            return "[ergo: commanderror]: No such command '%s'." % (command[0])

    # command has passed all tests
    return False

# def argCheck(string):
#     argument = parser.tokenize(string)[1][0]

# def kargCheck(string):
#     kargument = parser.tokenize(string)[2][0]