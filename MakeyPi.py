#!/usr/bin/env python2
#encoding: utf-8

import argparse
import picamera
from tweetbot import *
from messages import get_message
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
parser.add_argument('-d', '--dir',
					dest='dir_pix',
					default='/var/www/',
					help='directory where store images')
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
		api = connect_api()
		print "[+] Connected to twitter api"
		for event in device.read_loop():
			if event.type == ecodes.EV_KEY and event.timestamp()-5 > last_pix:
				last_pix = event.timestamp()
				last_pix_name = "no_log"
				filename = "%s/%s.jpg" % (args.dir_pix, str(last_pix_name))
				message = get_message()
				with picamera.PiCamera() as camera:
					camera.resolution = (1280, 720)
					camera.capture(filename)
					update_status_pix(api, message, filename)
					print "[+] pix sended : %f, %s, %s" % (last_pix, message, filename)
	except Exception, e:
		print "[-] Error : " + str(e)
