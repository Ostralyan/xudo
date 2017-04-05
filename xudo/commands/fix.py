"""The logs command."""


from json import dumps

from .base import Base

import os, subprocess


class Fix(Base):
    """Docker logs"""

    def run(self):
        statusText = subprocess.Popen(['git status'], shell=True, stdout=subprocess.PIPE).communicate()[0]
        if "" in statusText:
            print("yes")
        else:
            print("no")