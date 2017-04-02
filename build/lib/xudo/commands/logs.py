"""The logs command."""


from json import dumps

from .base import Base

import os


class Logs(Base):
    """Docker logs"""

    def run(self):
        if self.options["api"]:
            os.system("docker logs api_api_1 -f")
        elif self.options["changelog"]:
            os.system("docker logs api_changelog_1 -f")
        elif self.options["migrations"]:
            os.system("docker logs api_migrations_1 -f")
        elif self.options["rcash"]:
            os.system("docker logs api_rcash_1 -f")