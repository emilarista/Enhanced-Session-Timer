# Enhanced Config Session Extension

This is a little EOS extension that streamlines the process of working with config sessions with a commit timer applied.

Normally when you do a commit timer HH:MM:SS command, you then have to show configuration sessions, get the name of the session and do a configure session <name> commit. The extension does this automatically via an alias to a 

## Installing the extension

Log onto your switch and copy the rpm file from a tftp/scp/whatever repo. Then copy it to extensions folder on flash:

    arista#cli vrf MGMT
    arista#copy tftp:<tftp host>/EnhancedSession-1-0.noarch.rpm
    arista#copy flash:EnhancedSession-1-0.noarch.rpm extension:
  
    arista#show extensions 
    Name                                Version/Release      Status      Extension
    ----------------------------------- -------------------- ----------- ---------
    EnhancedSession-1-0.noarch.rpm      1/0                  A, NI       1        
    
    
    A: available | NA: not available | I: installed | NI: not installed | F: forced
    S: valid signature | NS: invalid signature
    The extensions are stored on internal flash (flash:)

Install the extension, and verify that the proper alias is created:

    arista#extension EnhancedSession-1-0.noarch.rpm
    arista#show aliases
    timercommit     bash /opt/EnhancedSession/bin/EnhancedSession.py
    
Include the extension in boot-extensions:

    arista#copy installed-extensions boot-extensions
    arista#wr
  
## How to use it

    arista#configure session 
    arista(config-s-sess-1)#int eth 1
    arista(config-s-sess-1-if-Et1)#description ITWORKS!
    arista(config-s-sess-1-if-Et1)#commit timer 00:01:00
    arista#show run sec eth 1
    interface Ethernet1
      description ITWORKS!
      no switchport
    arista#timercommit

If you have no timered config session commits:

    arista#timercommit
    There are no timered sessions to commit.
  

