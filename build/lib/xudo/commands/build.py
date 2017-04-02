"""The logs command."""


from json import dumps

from .base import Base

import os


class Build(Base):
    """Say hello, world!"""

    def run(self):
        java_path = os.path.join(self.path, "java")
        php_path = os.path.join(self.path, "php")

        os.system("docker-compose stop")
        if self.options["-c"]:
            os.chdir(java_path)
            os.system("docker rm api_changelog_1")
            os.system("docker rmi java/changelog")
            os.system("./gradlew changelog:distDocker")
        if self.options["-m"]:
            os.chdir(java_path)
            os.system("docker rm api_migrations_1")
            os.system("docker rmi java/migrations")
            os.system("./gradlew migrations:clean")
            os.system("./gradlew migrations:jar")
            os.system("./gradlew migrations:distDocker")
        if self.options["-s"]:
            os.chdir(java_path)
            os.system("docker rm api_mysql_1")
        if self.options["-r"]:
            os.chdir(java_path)
            os.system("docker rm api_rcash_1")
            os.system("docker rmi java/rcash")
            os.system("./gradlew rcash:distDocker")
        if self.options["-e"]:
            os.chdir(java_path)
            os.system("docker rm api_email_1")
            os.system("docker rmi java/email")
            os.system("./gradlew email:distDocker")
        if self.options["-a"]:
            os.chdir(php_path)
            os.system("docker build -t hb_api .")
        if self.options["-x"]:
            os.chdir(php_path)
            os.system("docker build --no-cache -t hb_api .")

        os.system("docker-compose up -d");