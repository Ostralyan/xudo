from .base import Base

import os


class Clean(Base):
    """Removes all dangling images"""

    def run(self):
        os.system("docker rmi $(docker images --quiet --filter \"dangling=true\")")
