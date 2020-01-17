from os import environ, path
import sys
import logging
from box import Box
from glob import glob
import json
from .. import ROOT_DIR
CONFIG_FOLDER = path.join(ROOT_DIR, 'config')
INSTANCE_ENV_NAME = 'INSTANCE_ENV'
DEFAULT_INSTANCE_ENV = 'LOCAL'

CONSTANTS_DIR = path.join(CONFIG_FOLDER, 'constants')

CONSTANTS_KEY_SEPARATION_CHAR = '#'

CONFIG_INSTANCE_ENV_MAP = {
    'DEV': 'dev',
    'PREPROD': 'preprod',
    'PROD': 'prod',
    'LOCAL': 'local'
}

CONFIG_INSTANCE_ENV_MAP_FALLBACK = 'local'


def load_from_json_file(config_filename):
    return Box.from_json(filename=config_filename, default_box_attr=None, default_box=True)


def fill_with(obj, with_obj, key_sep=CONSTANTS_KEY_SEPARATION_CHAR):
    if isinstance(obj, dict):
        return {k: fill_with(v, with_obj) for k, v in obj.items()}
    elif isinstance(obj, str):
        if key_sep in obj:
            splitted = obj.split(key_sep)
            if len(splitted) == 2:
                consts_file, consts_key = splitted
                return with_obj.get(consts_file, {}).get(consts_key)
            else:
                return obj
        else:
            return obj
    elif isinstance(obj, list):
        return [fill_with(item, with_obj) for item in obj]
    else:
        return obj

def load_from_instance_env(load_constants=True):
    instance_env = environ.get(INSTANCE_ENV_NAME, DEFAULT_INSTANCE_ENV)
    filename = CONFIG_INSTANCE_ENV_MAP.get(
        instance_env, CONFIG_INSTANCE_ENV_MAP_FALLBACK)
    config_filename = path.join(
        CONFIG_FOLDER, '{}.config.json'.format(filename))
    main_config = load_from_json_file(config_filename)
    if load_constants:
        constants = load_constants_from_dir()
        main_config = Box(fill_with(main_config, constants),
                          default_box_attr=None, default_box=True)
    return main_config


def load_constants_from_dir(dir=CONSTANTS_DIR):
    constants_global = {}
    constants_files = list(glob(path.join(dir, '*.json'), recursive=False))
    for const in constants_files:
        basename = path.basename(const)
        name = basename[:-5]
        if basename.endswith('.json'):
            try:
                with open(const, 'r') as const_file:
                    data = const_file.read()
                const_decoded = json.loads(data)
                logging.info('constants file loaded : {}'.format(
                    const))
            except ValueError:
                logging.error('loading constants file failed : {}'.format(
                    const), file=sys.stderr)
        constants_global[name] = const_decoded
    return Box(constants_global, default_box_attr=None, default_box=True)
