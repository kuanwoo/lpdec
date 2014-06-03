# -*- coding: utf-8 -*-
# cython: embedsignature=True
# Copyright 2014 Michael Helmling
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation
from __future__ import division

__version__ = '2014.2'


def subclasses(base):
    """Return all subclasses of `base` as dictionary mapping class names to class
    objects.
    """
    found = {base}
    toCheck = list(base.__subclasses__())
    for cls in toCheck:
        found.add(cls)
        toCheck.extend(cls.__subclasses__())
    return dict((cls.__name__, cls) for cls in found)

def exactVersion():
    """Returns the version of the lpdec package.

    If this __init__ file is located inside a git repository (identified b a ».git« subdirectory
    of the parent directory), then the output of ``git describe --dirty`` is returned. Otherwise,
    the value of the above variable ``__version__`` is returned.
    """
    import subprocess
    from os.path import normpath, join, dirname, exists
    topdir = normpath(join(dirname(__file__), '..'))
    if exists(join(topdir, '.git')):
        version = subprocess.check_output(['git', 'describe', '--dirty'], cwd=topdir)
        return version.decode().strip()
    return __version__
