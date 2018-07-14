from .base import Base

import os


class Watch(Base):

    def run(self):
        hbngPath = os.path.join(self.path, "hbng")

        os.chdir(hbngPath)
        os.system('npm run webpack -- -d --watch')
