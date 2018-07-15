xudo-cli
========

*A quality of life tool to help bring up docker containers, access docker logs, generate jooq, run tests and more*

Installation
------------

``pip3 install xudo`` or ``python3 setup.py install`` to install with local files

Change `/Users/ostralyan/dev` to the absolute path of where the hbng folder is stored:
``echo '/Users/ostralyan/dev' > ~/.xudo_profile``

Usage
-----

``xudo logs [api | changelog | migrations]`` - This will follow the logs of the chosen container

``xudo pull`` - Pulls the Elastic Search and MySQL contianers

``xudo build [-c -m -s -a -x]`` - Deletes the corresponding process(es) and the image(s) and builds the container from scratch

* -c: Changelog
* -m: Migrations
* -s: Sql
* -a: Api
* -x: Api no cache

``xudo test (be | app | admin | core | it)`` - Runs the backend, frontend or integration tests

* be: Backend
* it: Integration Tests

``xudo watch`` - Watches hbng

``xudo clean`` - Removes all dangling containers

``xudo prune`` - Prompts to remove

        - all stopped containers
        - all networks not used by at least one container
        - all dangling images
        - all build cache

``xudo -h | --help`` - Shows the help screen

``xudo --version`` - Shows the version

Pushing to Pypi
---------------
cd /path/to/xudo-cli

rm -rf dist/

python setup.py sdist bdist_wheel

twine upload dist/*


