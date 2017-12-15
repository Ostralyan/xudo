"""The logs command."""


from json import dumps

from .base import Base

import os, subprocess


class Build(Base):
    """Say hello, world!"""

    def run(self):
        javaPath = os.path.join(self.path, "api/java")
        phpPath = os.path.join(self.path, "api/php")
        hbngPath = os.path.join(self.path, "hbng")

        # This needs to be a blocking call, otherwise there could be an issue when removing the containers
        subprocess.Popen("docker-compose stop", shell=True, stdout=subprocess.PIPE, cwd=javaPath).wait()

        if self.options["-c"]:
            os.chdir(javaPath)
            os.system("docker rm api_changelog_1")
            os.system("docker rmi java/changelog")
            os.system("./gradlew changelog:distDocker")
        if self.options["-m"]:
            os.chdir(javaPath)
            os.system("docker rm api_migrations_1")
            os.system("docker rmi java/migrations")
            os.system("./gradlew migrations:clean")
            os.system("./gradlew migrations:jar")
            os.system("./gradlew migrations:distDocker")
        if self.options["-s"]:
            os.chdir(javaPath)
            os.system("docker rm api_mysql_1")
        if self.options["-r"]:
            os.chdir(javaPath)
            os.system("docker rm api_rcash_1")
            os.system("docker rmi java/rcash")
            os.system("./gradlew rcash:distDocker")
        if self.options["-e"]:
            os.chdir(javaPath)
            os.system("docker rm api_email_1")
            os.system("docker rmi java/email")
            os.system("./gradlew email:distDocker")
        if self.options["-a"]:
            os.chdir(phpPath)
            os.system("docker build -t hb_api .")
        if self.options["-x"]:
            os.chdir(phpPath)
            os.system("docker build --no-cache -t hb_api .")
        if self.options["-n"]:
            subprocess.Popen("gulp -nds", shell=True, stdout=subprocess.PIPE, cwd=hbngPath)

        subprocess.Popen("docker-compose up -d", shell=True, stdout=subprocess.PIPE, cwd=javaPath).wait()