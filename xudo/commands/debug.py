"""The logs command."""


from json import dumps

from .base import Base

import os, sys


class Debug(Base):
    """Say hello, world!"""

    def run(self):
        hbngPath = os.path.join(self.path, "hbng")

        if self.options["php"]:
            os.system("docker exec api_api_1 /bin/sh -c \"sed -ie '\\$axdebug\.remote_host=192\.168\.65\.1' /etc/php/5.6/mods-available/xdebug.ini\"")
            os.system("docker exec api_api_1 /bin/sh -c \"sed -ie '\\$axdebug\.remote_connect_back=0' /etc/php/5.6/mods-available/xdebug.ini\"")
            os.system("docker exec api_api_1 /bin/sh -c \"service php5.6-fpm restart\"")
        elif self.options["hbng"]:
            if self.options["app"]:
                os.chdir(hbngPath)
                os.system("./debugKarma.sh app")
            elif self.options["admin"]:
                os.chdir(hbngPath)
                os.system("./debugKarma.sh admin")
            elif self.options["core"]:
                os.chdir(hbngPath)
                os.system("./debugKarma.sh core")
            
