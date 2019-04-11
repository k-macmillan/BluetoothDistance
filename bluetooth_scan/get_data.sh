#!/bin/bash

MISSING="Missing x, y, z variables"
DATA=bt_data
DEVICES=devices
CSV=sensor_data.csv
RUN=get_data.py
SOUND=transfer_complete.wav
SCAN="Running Bluetooth LE scan..."
RUNNING="\r\033[1A\033[0K"$SCAN
JOBSDONE="Job's done..."

if [ "$#" -ne 3 ]; then
    echo $MISSING
    exit 1
fi

echo $SCAN

for i in {1..5}
do
    echo -e ${RUNNING}${i}
    sudo -S btmgmt find &>> $DATA
done

python3 $RUN $DATA $DEVICES $CSV $1 $2 $3
rm $DATA
echo $JOBSDONE
aplay -q -c 1 -t wav $SOUND &