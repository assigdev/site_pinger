Site Pinger
===============================

version number: 0.4.0
author: Arsen Khalilov

Overview
--------

python program for check work in site urls.

for periodical ping sites run with cron.

Installation
------------

To install use pip:

    $ pip install site_pinger


Or clone the repo:

    $ git clone https://github.com/assigdev/site_pinger.git

    $ python setup.py install

Usage
-----

first you need conf ini file:

    $ site_pinger_conf

then run program

    $ site_pinger

run with conf in flag
    
    $ site_pinger -c path_to_conf_file


Flags
-------
    
    optional arguments:
      -h, --help            show this help message and exit
      -t TIMEOUT, --timeout TIMEOUT
                            time out for async tasks
      -l LOG, --log LOG     log file path
      -d, --debug           debug logging
      -e, --email           receiver email
      -c CONFIG, --config CONFIG
                            config file path
      --email-header EMAIL_HEADER
                            header for email



Contributing
------------

TBD