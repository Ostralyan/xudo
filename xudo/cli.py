"""
xudo
Usage:
  xudo build [-c -m -s -a -x -n]
  xudo logs (api | changelog | migrations)
  xudo up
  xudo watch
  xudo jooq
  xudo test (be | app | admin | core | it)
  xudo pull
  xudo dbpw
  xudo clean
  xudo prune
  xudo -h | --help
  xudo --version
Examples:
  xudo logs api
  xudo build -cms
  xudo debug hbng app
Build Options:
  -c                                Changelog
  -m                                Migrations
  -s                                Sql
  -a                                Api
  -x                                Api no cache
  -n                                Angular
Test Options:
  be                                Backend
  it                                Integration Test
  For additional help using this tool contact luke@honestbuildings.com
  or visit https://github.com/Ostralyan/xudo
"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION

import requests 

import os


def main():
    """Main CLI entrypoint."""
    import xudo.commands
    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    path = get_path()
    for (k, v) in options.items(): 
        if hasattr(xudo.commands, k) and v:
            module = getattr(xudo.commands, k)
            xudo.commands = getmembers(module, isclass)
            command = [command[1] for command in xudo.commands if command[0] != 'Base'][0]
            command = command(path, options)
            command.run()

    completion_notification()

def get_path():
  try:
    return open(os.path.join(os.path.expanduser('~'),'.xudo_profile')).read().strip();
  except IOError:
    print("cannot find .xudo_profile in home directory")

def completion_notification():
    text = "Done"
    os.system("osascript -e \'display notification \"" + text + "!\" with title \"xudo\"'");
