import logging
import os


log = logging.getLogger(__name__)


def post_activate_source(args):
    return """
#patch to wrap npm inside the virtual env
if [ -n "${NPM_CONFIG_PREFIX+1}" ]; then
    export _OLD_NPM_CONFIG_PREFIX="$NPM_CONFIG_PREFIX"
fi
export NPM_CONFIG_PREFIX=$VIRTUAL_ENV

"""



def pre_deactivate_source(args):
    return  """
#restore the value before exiting the venv
if [ -n "${_OLD_NPM_CONFIG_PREFIX+1}" ]; then
    NPM_CONFIG_PREFIX="$_OLD_NPM_CONFIG_PREFIX"
    export NPM_CONFIG_PREFIX
    unset _OLD_NPM_CONFIG_PREFIX
else
    unset NPM_CONFIG_PREFIX
fi

"""
