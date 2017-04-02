"""The logs command."""


from json import dumps

from .base import Base

import os, subprocess


class Fix(Base):
    """Docker logs"""

    def run(self):
        output = subprocess.Popen(['git', 'status'], stdout=subprocess.PIPE);
        print(output.stdout)