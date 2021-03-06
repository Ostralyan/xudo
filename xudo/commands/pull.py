from .base import Base

import os, sys


class Pull(Base):
    """Pulls new copies of the mysql, elastic search and electron pdf render services"""

    def run(self):
            sys.stdout.write("\033[1;31m")
            print("************************************************************")
            print("********************PULLING MY SQL IMAGE********************")
            print("************************************************************")
            sys.stdout.write("\033[0;0m")

            os.system("docker pull quay.io/honestbuildings/hb_mysql")

            sys.stdout.write("\033[0;32m")
            print("************************************************************")
            print("********************PULLING ES IMAGE*********************")
            print("************************************************************")
            sys.stdout.write("\033[0;0m")

            os.system("docker pull quay.io/honestbuildings/hb_elasticsearch")

            sys.stdout.write("\033[1;34m")
            print("************************************************************")
            print("********************PULLING ELECTRON PDF IMAGE*********************")
            print("************************************************************")
            sys.stdout.write("\033[0;0m")
            os.system("docker pull quay.io/honestbuildings/hb_electron_render_service:latest")
