from .base import Base

import os


class Jooq(Base):
    """Generates Jooq"""

    def run(self):
        javaPath = os.path.join(self.path, "hbng/java")
        os.chdir(javaPath)
        os.system("./gradlew generateJooq")