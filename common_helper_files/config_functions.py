"""Helper functions for configuration files.
"""
import os
import logging

log = logging.getLogger(__name__)


def update_config_from_env(config):
    """ Update configuration fields in config from environment variables.

    The environment variable names are expected to be of the form, that the
    section name and the variable name are seperated by a dubble underscore,
    e.g.

        SECTION_NAME__VARIABLE_NAME

    """
    for key, val in os.environ.items():
        if '__' in key:
            section, section_key = key.lower().split('__')
            try:
                config[section.capitalize()][section_key] = val
            except KeyError:
                log.error('No section {} or value {} found.'.format(section.capitalize(), section_key))

    return config
