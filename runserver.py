#!/usr/bin/env python
# encoding: utf-8

# Copyright (C) 2015 Chintalagiri Shashank
# Released under the MIT license.

"""

Runs a Twisted reactor, exposing the filesystems specified
by the implementation of :data:`fs_server.config.FILESYSTEMS`,
and the reactor listens at :data:`fs_server.config.SERVER_PORT`.

"""

from fs_server.serve import get_resource
from fs_server.config import SERVER_PORT
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource


if __name__ == '__main__':
    root = Resource()
    XMLRPCFS_resource = get_resource(root)
    factory = Site(root)
    reactor.listenTCP(SERVER_PORT, factory)
    reactor.run()
