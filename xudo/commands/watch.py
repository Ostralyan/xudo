"""The logs command."""


from json import dumps

from .base import Base

import os


class Watch(Base):
    """Say hello, world!"""

    def run(self):
        hbngPath = os.path.join(self.path, "hbng")

        os.chdir(hbngPath)
        os.system('gulp watch -d')
