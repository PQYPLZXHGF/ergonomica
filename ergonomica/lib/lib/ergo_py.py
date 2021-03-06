#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

# the purpose of this program is _to execute arbitrary code_
# pylint: disable=exec-used

"""
[lib/lib/ergo_py.py]

Defines the "py" command.
"""

import sys
from copy import copy
from ptpython.repl import embed

def _execfile(filepath, _globals=None, _locals=None):
    if _globals is None:
        _globals = {}
    _globals.update({
        "__file__": filepath,
        "__name__": "__main__",
    })
    with open(filepath, 'rb') as infile:
        exec(compile(infile.read(), filepath, 'exec'), _globals, _locals)

def py(argc):
    """py: Python ergonomica integration.

    Usage:
       py [(--file FILE | STRING)]
    """
    
    if argc.args['--file']:
        # pylint seems to think execfile isn't defined
        _execfile(argc.args['FILE']) # pylint: disable=undefined-variable
        return

    elif argc.args['STRING']:
        mod_ns = copy(argc.ns)
        mod_ns.update(globals())
        # ergonomica is a shell
        # pylint: disable=eval-used
        return eval(argc.args['STRING'], mod_ns)

    try:
        temp_space = globals()

        # export ergonomica variables
        for item in argc.ns:
            if not callable(argc.ns[item]):
                temp_space[item] = argc.ns[item]

        temp_space.update({"exit":sys.exit})
        temp_space.update({"quit":sys.exit})
        temp_space.update(argc.env.namespace)

        _vi_mode = False
        if argc.env.editor in ["vi", "vim"]:
            _vi_mode = True

        embed(globals(), temp_space, vi_mode=_vi_mode)
    except SystemExit:
        for key in temp_space:
            if not callable(temp_space[key]):
                argc.ns[key] = temp_space[key]
        return


exports = {'py': py}


