#!/usr/bin/env python
# encoding: utf-8

# Copyright (C) 2015 Chintalagiri Shashank
# Released under the MIT license.

"""
Configuration parameters for the :mod:`fs_server` package.

This package was written for tendril. The default configuration attempts
to obtain the FILESYSTEMS to expose from the local tendril configuration,
if available.

If you want something else to happen, set the :data:`FILESYSTEMS` list
accordingly.

.. rubric:: Usage Example

>>> from fs_server import config
>>> config.FILESYSTEMS = ['root_folder', '/']
>>> config.SERVER_PORT = 1079

.. warning:: Don't actually do this. Use a real, safe path instead.

"""

import logging


try:
    from tendril.utils import config
except ImportError:
    config = None


FILESYSTEMS = []

if config:
    logging.info("Adding Wallet to FILESYSTEMS")
    FILESYSTEMS.append(('wallet', config.DOCUMENT_WALLET_ROOT))
    logging.info("Adding Docstore to FILESYSTEMS")
    FILESYSTEMS.append(('docstore', config.DOCSTORE_ROOT))
    logging.info("Adding Refdocs to FILESYSTEMS")
    FILESYSTEMS.append(('refdocs', config.REFDOC_ROOT))

SERVER_PORT = 1080
