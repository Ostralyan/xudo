"""The logs command."""


from json import dumps

from .base import Base

import os


class Test(Base):
    """Say hello, world!"""

    def run(self):
        javaPath = os.path.join(self.path, "api/java")
        hbngPath = os.path.join(self.path, "hbng")
        testPath = os.path.join(self.path, "api/test")

        if self.options["be"]:
            os.chdir(javaPath)
            os.system("./gradlew clean build test")
        elif self.options["app"]:
            os.chdir(hbngPath)
            os.system("gulp karma-hb-app")
        elif self.options["admin"]:
            os.chdir(hbngPath)
            os.system("gulp karma-hb-admin")
        elif self.options["core"]:
            os.chdir(hbngPath)
            os.system("gulp karma-hb-core")
        elif self.options["it"]:
            os.chdir(testPath)
            os.system("gulp mocha")
