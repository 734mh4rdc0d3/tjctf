#!/bin/bash
a=0
fl= 0
while true
do
if [ -f $a.tar* ]
then
	tar -xf $a.tar*
	cat $fl.txt
elif [ -f $a.k* ] 
then
	mv $a.* $a.zip
	unzip $a.zip
	cat $fl.txt
else
	cat $fl.txt
	break
fi
cd $a
a=$((a+1))
fl=$((fl+1))
done
