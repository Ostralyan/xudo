"""The logs command."""


from .base import Base

import os


class Logs(Base):
    """Docker logs"""

    def run(self):
        if self.options["api"]:
            os.system("docker logs hbng_api_1 -f")
        elif self.options["changelog"]:
            os.system("docker logs hbng_changelog_1 -f")
        elif self.options["migrations"]:
            os.system("docker logs hbng_migrations_1 -f")