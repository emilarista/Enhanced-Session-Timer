#!/usr/bin/python

# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.
'''
@Copyright: 2015-2016 Arista Networks, Inc.
Arista Networks, Inc. Confidential and Proprietary.
EnhancedSession.py is a function which can be extended and used to perform various
actions on an EOS device.
'''

import subprocess
import json
import sys

checksessions = ['FastCli', '-p', '15', '-c', 'show configuration sessions | json']

output = subprocess.check_output(checksessions)
sessions = json.loads(output)

if len(sessions["sessions"]) > 0:
    pass
else:
    print "There are no timered sessions to commit."
    sys.exit(0)

for session, data in sessions["sessions"].items():
    if data["state"] == "pendingCommitTimer":
        sessionname = session
        break
    else:
        sessionname = False
        continue

if not sessionname:
    print "There are no timered sessions to commit."
    sys.exit(0)

commitcmd = ['FastCli', '-p', '15', '-c', 'configure session {} commit'.format(sessionname)]

out = subprocess.check_output(commitcmd)
