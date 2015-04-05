
import argparse
from evdev import InputDevice, list_devices, categorize, ecodes

parser = argparse.ArgumentParser(description='Take picture when a key is pressed :o')
parser.add_argument('inputfile', help='input file from which read keypress')
parser.add_argument('-l', '--list',
					dest='list_devices',
					action='store_const',
					const=True,
					default=False,
					help='list connected devices')
args = parser.parse_args()

if args.list_devices:
	devices = [InputDevice(d) for d in list_devices()]
	if len(devices) == 0:
		print "[-] No devices ... Maybe try with root rights ?"
	else:
		print "[+] %d devices :" % len(devices)
		for device in devices:
			print "\t - " + device.fn, device.name, device.phys
else:
	device = InputDevice(args.inputfile)
	print "[+] monitoring device : " + device.fn, device.name, device.phys
	for event in device.read_loop():
		if event.type == ecodes.EV_KEY:
			print categorize(event)
