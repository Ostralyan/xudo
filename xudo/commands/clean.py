"""The logs command."""


from .base import Base

import os


class Clean(Base):
    """Say hello, world!"""

    def run(self):
        os.system("docker rmi $(docker images --quiet --filter \"dangling=true\")")
