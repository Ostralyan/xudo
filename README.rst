xudo-cli
========

*A command line program to replace dockdock, written in Python3*

Installation
------------

``pip install xudo``

Change `/Users/ostralyan/dev` to the absolute path of where the api and hbng folders are stored:
``echo '/Users/ostralyan/dev' > ~/.xudo_profile``

Usage
-----

``xudo logs [api | changelog | migrations | rcash]`` - This will follow the logs of the chosen container

``xudo pull`` - Pulls the Elastic Search and MySQL contianers

``xudo build [-c -m -s -e -r -a -x]`` - Deletes the corresponding process(es) and the image(s) and builds the container from scratch

* -c: Changelog
* -m: Migrations
* -s: Sql
* -e: Email
* -r: Rcash
* -a: Api
* -x: Api no cache

``xudo test (be | app | admin | core | it)`` - Runs the backend, frontend or integration tests

* be: Backend
* it: Integration Tests

``xudo watch`` - Watches hbng

``xudo debug (php | hbng (app | admin | core))``  - Enables PHP debugging or runs front end unit test debugging

``xudo clean`` - Removes all dangling containers

``xudo -h | --help`` - Shows the help screen

``xudo --version`` - Shows the version
