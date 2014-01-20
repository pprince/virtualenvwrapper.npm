import logging
import os


log = logging.getLogger(__name__)


def post_activate_source(args):
    return """
if [ -e "${VIRTUAL_ENV}/.npm" ]; then
    if [ -n "${NPM_CONFIG_PREFIX+x}" ]; then
        export _OLD_NPM_CONFIG_PREFIX="$NPM_CONFIG_PREFIX"
    fi
    export NPM_CONFIG_PREFIX=$VIRTUAL_ENV
fi

"""



def pre_deactivate_source(args):
    return  """
if [ -e "${VIRTUAL_ENV}/.npm" ]; then
    if [ -n "${_OLD_NPM_CONFIG_PREFIX+x}" ]; then
        NPM_CONFIG_PREFIX="$_OLD_NPM_CONFIG_PREFIX"
        export NPM_CONFIG_PREFIX
        unset _OLD_NPM_CONFIG_PREFIX
    else
        unset NPM_CONFIG_PREFIX
    fi
fi

"""
