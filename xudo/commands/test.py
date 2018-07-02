"""The test command."""
import os
from .base import Base


class Test(Base):
    def run(self):
        java_path = os.path.join(self.path, "hbng/java")
        hbng_path = os.path.join(self.path, "hbng")
        test_path = os.path.join(self.path, "hbng/test")

        if self.options["be"]:
            os.chdir(java_path)
            os.system("./gradlew clean build test")
        elif self.options["app"]:
            os.chdir(hbng_path)
            os.system("npm run test-app")
        elif self.options["admin"]:
            os.chdir(hbng_path)
            os.system("npm run test-admin")
        elif self.options["core"]:
            os.chdir(hbng_path)
            os.system("npm run test-core")
        elif self.options["it"]:
            os.chdir(test_path)
            os.system("npm run mocha --env=local")
