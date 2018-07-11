"""The prune command."""


from .base import Base

import os


class Prune(Base):
    """Prompts the user to prune their docker environment"""

    def run(self):
        os.system("docker system prune")
