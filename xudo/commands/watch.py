"""The logs command."""


from .base import Base

import os


class Watch(Base):
    """Say hello, world!"""

    def run(self):
        hbngPath = os.path.join(self.path, "hbng")

        os.chdir(hbngPath)
        os.system('gulp watch -d') # TODO: Figure out how to do with webpack
