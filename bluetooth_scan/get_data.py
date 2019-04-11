import sys
import math

rssi_offset = 6

def read_addresses(args):
    # args[1] = input data file
    # args[2] = devices
    # args[3] = csv output file
    # args[4] = x
    # args[5] = y
    # args[6] = z
    print('Raw to CSV conversion...')
    csv = args[3]
    xyz = float(args[4]), float(args[5]), float(args[6])
    device_data = dict.fromkeys(('name', 'uuid', 'xyz'))
    log_data = dict.fromkeys(('uuid', 'rssi', 'dist'))
    devices = []
    uuid_list = []
    with open(args[2], 'r') as d_file:
        for line in d_file:
            if line.count(',') == 4:
                # Clean line:
                line = line.replace('\n', '').replace(' ', '')
                name, uuid, x, y, z = line.split(',')
                device = dict.fromkeys(device_data)
                device['name'] = name
                device['uuid'] = uuid
                device['xyz'] = float(x), float(y), float(z)
                devices.append(device)
                uuid_list.append(uuid)
            else:
                if line != '\n':
                    print('Devices setup incorrectly, please check \"devices\" file')
                    exit()

    rssi_data = []
    with open(args[1], 'r') as file:
        for line in file:
            info = get_address_rssi(line)
            if info is not None and info[0] in uuid_list:
                # Add distance to each device
                for device in devices:
                    rssi_data.append((info[0], info[1], get_distance(device['xyz'], xyz)))
    
    with open(csv + '.csv', 'a') as file:
        for item in rssi_data:
            file.write(','.join(str(x) for x in item) + '\n')

def get_distance(a, b):
    return math.sqrt((b[0] - a[0]) * (b[0] - a[0]) +
                     (b[1] - a[1]) * (b[1] - a[1]) +
                     (b[2] - a[2]) * (b[2] - a[2]))


def get_address_rssi(string):
    # Find first ':'
    colon = string.find(':')
    if colon != -1:
        # address = string[colon + 2:colon + addr_offset]
        try:
            address = string[colon:].split(' ')[1]
            rssi = string.find('rssi')
            if rssi != -1:
                # Grab RSSI value
                rssi =  abs(int(string[rssi:].split(' ')[1]))
            else:
                # For some reason there was a colon but not RSSI
                return None
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            # Some oddity I missed
            print('String invalid: {}'.format(string))
            return None
    else:
        return None

    return address, rssi


def test():
    with open(device_list, 'r') as d_file:
        devices = {}
        for line in d_file:
            name, uuid = line.split(',')
            devices[name] = uuid

        print(devices)

# test()

# read_addresses()

if __name__ == '__main__':
    read_addresses(sys.argv)
    # get_distance((0, 0, 0), (10, 10, 10))