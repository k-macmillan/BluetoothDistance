# BluetoothDistance
Project to find location in a room based on Bluetooth LE signal strength to multiple beacons

## Bluetooth LE scan
The script requires a recent sudo in order get useful information from `btmgmt find`, so log into:
```
sudo su
exit
```
**Note:** If you fail to do this step it will hang and print the password prompt to `sensor_data.csv`.

Next run:
```
./get_data.sh x y z
```
Where x, y, and z represent the coordinates in a room. This portion of the project is to gather data points.
