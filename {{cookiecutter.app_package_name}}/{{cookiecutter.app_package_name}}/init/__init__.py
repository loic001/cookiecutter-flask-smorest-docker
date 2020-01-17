import os
import sys
from importlib import util

from os import environ, path
from box import Box
import os

from .. import ROOT_DIR

INIT_FOLDER = os.path.join(ROOT_DIR, 'init')
INITIALIZER_SUFFIX = '__initializer'


def get_initializers(folder=INIT_FOLDER, suffix=INITIALIZER_SUFFIX):
    initializers = {}
    suffix_file = suffix + '.py'
    for possible_initializer in os.listdir(folder):
        if os.path.isdir(possible_initializer) or not possible_initializer.endswith(suffix_file):
            continue
        initializer_name = possible_initializer[:-len(suffix_file)]
        module_name = initializer_name + INITIALIZER_SUFFIX
        filename = module_name + '.py'
        spec = util.spec_from_file_location(
            module_name, os.path.join(INIT_FOLDER, filename))
        module = util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if(callable(module.init)):
            initializers[initializer_name] = module.init
    return initializers


def init(config):
    initialized = {}
    initializers = get_initializers()
    for _initializer_name, _initializers in config.initializers.items():
        initializer = initializers.get(_initializer_name)
        if(initializer):
            initialized[_initializer_name] = {}
            for initializer_key, initializer_config in _initializers.items():
                initializer_config = Box({k: v for d in initializer_config for k, v in d.items(
                )}, default_box=True, default_box_attr=None) if isinstance(initializer_config, list) else initializer_config
                initialized[_initializer_name][initializer_key] = initializer(
                    initializer_config, config, initializer_key, initialized)
    return Box(initialized, default_box=True, default_box_attr=None)
