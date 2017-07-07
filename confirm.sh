#!/bin/bash
echo ""
echo Attemptingng to confirm Tomcat is installed on: $1 
echo ""
isinst=$(wget -t 5 --timeout=5 -q -O /dev/stdout http://$1:8080 | head -n 2| grep -o 'Apache')
echo instance id is : $isinst
if [ "$isinst" != "Apache" ]
then
    echo trying again with longer timeout
    isinst=$(wget -t 7 --timeout=7 -q -O /dev/stdout http://$1:8080 | head -n 2| grep -o 'Apache')
fi
if [ "$isinst" == "Apache" ]; then echo 'Tomcat installed'; else echo 'not confirmed'; fi

