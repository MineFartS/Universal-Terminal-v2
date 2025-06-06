# The Universal Terminal
# Created By: Phil H.
# Github: https://github.com/MineFartS/Universal-Terminal/

import os, subprocess

class help:
    help = 'List all commands [help]\nGet more details for specific command [help *cmd*]'

class exit:
    help = 'Exit Universal Terminal'

class echo:
    help = 'Returns given text input'

    def run(params):
        string = ''
        for p in params:
            string += p + ' '

        print(string[:-1])


class clear:
    help = 'Clears The Terminal Window'

    def run(params):
        cmd = {True:'cls', False:'clear'} [os.name == 'nt']
        os.system(cmd)


class sys:
    help = "Send a command to your computer's built-in terminal"

    def run(params):
        terminal = {True:['cmd', '/c'], False:[]} [os.name == 'nt']
        subprocess.run(terminal + params)
