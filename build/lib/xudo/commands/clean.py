"""The logs command."""


from json import dumps

from .base import Base

import os, sys


class Clean(Base):
    """Say hello, world!"""

    def run(self):
        os.system("docker rmi $(docker images --quiet --filter \"dangling=true\")")
