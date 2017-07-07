echo starting
echo ""
keyfile=MadhanAssignmentKeys
keypath=/Users/Happy/Downloads

ipandinstid=$(python start.py)
echo ""

ipaddr=$(echo $ipandinstid | cut -f 1 -d ,)
echo $ipaddr

instid=$(echo $ipandinstid | cut -f 2 -d ,)
echo $instid

echo ip=$ipaddr
echo ""

rtn=$(python install.py $ipaddr $keyfile $keypath)
echo ""
slp=100
echo sleep $slp seconds
sleep $slp
echo \nwake up\n
echo confirming tomcat installation on $ipaddr
echo ""



bash -x ./confirm.sh $ipaddr

term=$(python terminate.py $instid)
echo ""
slp=100
echo sleep mode $slp seconds
echo confirming termination
echo""




