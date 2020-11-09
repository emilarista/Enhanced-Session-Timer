#!/bin/bash
if [[ -e /etc/Eos-release ]] 
then
    echo -n "Found EOS - installing alias..." 
    FastCli -c "en
                conf
                alias timercommit bash /opt/EnhancedSession/bin/EnhancedSession.py "
    echo "done"
    echo -n "Saving Config..." 
    FastCli -c "enable
                write" 
    echo "done"
else
    echo 'Not EOS.' 
fi
