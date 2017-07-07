#! /bin/bash
for i in {1..3}
do
    echo Loop :  $i 
    ./main.sh $i
done
