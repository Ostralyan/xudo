"""The logs command."""


from json import dumps

from .base import Base

import os


class Test(Base):
    """Say hello, world!"""

    def run(self):
        java_path = os.path.join(self.path, "java")
        hbng_path = os.path.join(self.path, "../hbng")
        test_path = os.path.join(self.path, "test")

        if self.options["be"]:
            os.chdir(java_path)
            os.system("./gradlew clean build test")
        elif self.options["app"]:
            os.chdir(hbng_path)
            os.system("gulp karma-hb-app")
        elif self.options["admin"]:
            os.chdir(hbng_path)
            os.system("gulp karma-hb-admin")
        elif self.options["core"]:
            os.chdir(hbng_path)
            os.system("gulp karma-hb-core")
        elif self.options["it"]:
            os.chdir(test_path)
            os.system("gulp mocha")
