#!/usr/bin/env python3.7
#
# LICENSE
# Copyright 2020 Eric Melville
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# DESCRIPTION
# nakedports - list installed ports without a maintainer
#
# This simple script digs through installed ports and lists those without a
# maintainer, the logic being that if this is being used then picking up
# maintainership would be a nice way to help out the project.
#
# HISTORY
# 0.1 - Initial copy, no more than a single query and formatting

import sqlite3

DBPATH = "/var/db/pkg/local.sqlite"

dbh = sqlite3.connect(DBPATH)
dbc = dbh.cursor()

dbc.execute("SELECT origin,www FROM packages WHERE maintainer LIKE 'ports@FreeBSD.org';")
res = dbc.fetchall()
for r in res:
    if r[1] != "UNKNOWN":
        s = r[0] + " (" + r[1] + ")"
        print(s)
    else:
        print(r[0])

dbh.close()
