# The Universal Terminal
# Created By: Phil H.
# Github: https://github.com/MineFartS/Universal-Terminal/

# Terminal Version
ver = 2.1

# Import Packages
import sys, os, math, inspect

# Import scripts with commands
from . import __cmds__ as cmdfile1 # Internal
from . import commands as cmdfile2 # Custom

# Declare json array for commands
cmds = {}

# Loop through the commands in both files
for cmdfile in [cmdfile1, cmdfile2]:
    for cmd in dir(cmdfile):
        obj = getattr(cmdfile, cmd)
        if inspect.isclass(obj):
            # Mark as Internal or Custom
            obj.type = {True:'Internal', False:'Custom'} [cmdfile == cmdfile1]
            # Add function to json array
            cmds[cmd] = getattr(cmdfile, cmd)

# [Func] - Get dashes to fill % of terminal window
def dash(p:float):
    return math.floor(os.get_terminal_size().columns * (p/100)) * '-'

# Clear Terminal Window
os.system({True:'cls', False:'clear'} [os.name == 'nt'])

# Print Title Page
print()
print(dash(100))
print(f'The Universal Terminal (v{str(2.1)})')
print('https://github.com/MineFartS/Universal-Terminal/')
print(dash(100))
print('Run "help" for a list of commands')

print()

# Loop Forever
while True:
    # Ask for and process user input
    raw = input(f'\n{os.getcwd()} > ')
    args = raw.split(' ') # will add more logic later
    cmd, params = args[0], args[1:]

    # Exit terminal if certain command given
    if cmd.lower() in ['quit', 'exit', 'close', 'stop', 'end', 'leave']:
        exit()
    else:
        try:
            # Show help message
            if cmd in ['help', '?', '/?', '-h']:
                
                # List commands if no parameters given
                if len(params) == 0:
                    print(dash(50))
                    print('Commands:')
                    print()

                    for c in cmds:
                        if not (c.startswith('__') and c.endswith('__')):
                            print(f' - {c} ({cmds[c].type})')

                    print()
                    print(dash(50))

                # Show help message for command
                else:
                    obj = cmds[params[0]]

                    print(dash(50))
                    print(f'Command: {params[0]}')
                    print(f'Type: {obj.type}')
                    print(f'Message: {obj.help}')
                    print(dash(50))
            else:
                # Find command by input and run with parameters
                cmds[cmd].run(params)

        except:
            # Show error message if execution fails
            print(dash(25))
            print('Execution Error')
            print('Run "help" for a list of Commands')
            print(dash(25))
                
            print(dash(25))
            print('Please share any glitches or bugs on github')
            print('https://github.com/MineFartS/Universal-Terminal/')
            print(dash(25))