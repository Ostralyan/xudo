from .base import Base

import os


class Dbpw(Base):
    """Generates Database PW from AWS"""

    def run(self):
        os.system("aws ssm get-parameter --name \"/local/CFG_MYSQL_MASTER_PASS\" --with-decryption --query 'Parameter.Value' --output text")


