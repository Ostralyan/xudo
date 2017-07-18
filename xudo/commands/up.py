"""The up command."""

from .base import Base

class Up(Base):

    def run(self):
        os.system("docker-compose up")
