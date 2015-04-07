#!/usr/bin/env python2
#encoding: utf-8

import argparse
from tweetbot import *
from evdev import InputDevice, list_devices, ecodes

parser = argparse.ArgumentParser(description='Take picture when a key is pressed :o')
parser.add_argument('-i', '--input',
					dest='input_file',
					help='input file from which read keypress')
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
	try:
		device = InputDevice(args.input_file)
		print "[+] monitoring device : " + device.fn, device.name, device.phys
		last_pix = 0
		for event in device.read_loop():
			if event.type == ecodes.EV_KEY and event.timestamp()-5 > last_pix:
				last_pix = event.timestamp()
				print "pix !"
				print event.timestamp()
	except Exception, e:
		print "[-] Error : " + str(e)
