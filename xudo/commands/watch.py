"""The logs command."""


from json import dumps

from .base import Base

import os


class Watch(Base):
    """Say hello, world!"""

    def run(self):
        hbng_path = os.path.join(self.path, "../hbng")

        os.chdir(hbng_path)
        os.system('gulp watch -d')
