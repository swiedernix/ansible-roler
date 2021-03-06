#!/usr/bin/env python
""" Python cli tool to ansible role structure """

import logging
import argparse
from ansibleroler import __version__
from ansibleroler import defaults
from ansibleroler.utils.settings import get_settings
from ansibleroler.utils.template import add_role


def main():
    parser = argparse.ArgumentParser(description="Manage ansible role environments")
    parser.add_argument('-c', dest='config_file', default=defaults.config_file,
                        help="Location of configuration file: [%s]" % defaults.config_file)
    parser.add_argument('-p', '--path', action="store", dest="base_path", metavar="PATH",
                        help="Path where the new role will be created", default=None)
    parser.add_argument('-v', '--verbose', dest='log_level', action="count",
                        help="Show more verbose output", default=None)
    parser.add_argument('--version', action='version', version='%(prog)s {}'.format(__version__))

    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('-n', '--name', action="store", dest="role_name", metavar="NAME",
                               help="Name of the new role", default=None, required=True)

    options = parser.parse_args()

    # Override correct log level from argparse
    levels = [logging.WARNING, logging.INFO, logging.DEBUG]
    if options.log_level:
        options.log_level = levels[min(len(levels) - 1, options.log_level - 1)]

    settings = get_settings(options)
    logger = logging.getLogger("ansibleroler")

    try:
        add_role(settings)
    except OSError as e:
        logger.error("{}. Aborted.".format(e))


if __name__ == "__main__":
    main()
