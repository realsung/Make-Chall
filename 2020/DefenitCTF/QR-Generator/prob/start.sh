#!/bin/sh

while : 
do
	su -c "exec socat -d tcp-listen:9000,reuseaddr,fork exec:\"python3 /home/QRGenerator/build.py\",stderr" - QRGenerator;
done