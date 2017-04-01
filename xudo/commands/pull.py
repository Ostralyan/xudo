"""The logs command."""


from json import dumps

from .base import Base

import os, sys


class Pull(Base):
    """Say hello, world!"""

    def run(self):
            sys.stdout.write("\033[1;31m")
            print("************************************************************")
            print("********************PULLING MY SQL IMAGE********************")
            print("************************************************************")
            sys.stdout.write("\033[0;0m")

            os.system("docker pull quay.io/honestbuildings/hb_mysql")

            sys.stdout.write("\033[0;32m")
            print("************************************************************")
            print("********************PULLING MY ES IMAGE*********************")
            print("************************************************************")
            sys.stdout.write("\033[0;0m")

            os.system("docker pull quay.io/honestbuildings/hb_elasticsearch")
