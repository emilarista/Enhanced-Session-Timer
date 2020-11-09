#!/usr/bin/python

import subprocess
import json
import sys

checksessions = ['FastCli', '-p', '15', '-c', 'show configuration sessions | json']

output = subprocess.check_output(checksessions)
sessions = json.loads(output)

if len(sessions["sessions"]) > 0:
    pass
else:
    sys.exit("There are no timered sessions to commit.")

for session, data in sessions["sessions"].items():
    if data["state"] == "pendingCommitTimer":
        sessionname = session
        break
    else:
        sessionname = False
        continue

if not sessionname:
    sys.exit("There are no timered sessions to commit.")

commitcmd = ['FastCli', '-p', '15', '-c', 'configure session {} commit'.format(sessionname)]

out = subprocess.check_output(commitcmd)