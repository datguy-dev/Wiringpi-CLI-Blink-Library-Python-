#!/usr/bin/python3

import sh
import threading
from time import sleep

threads = []
def blink_thread(rgb_object, color, interval, stop_event):
	t = threading.currentThread()
	while getattr(t, 'do_blink', True):
		for x in range(len(rgb_object.pins)):
			if rgb_object.colors[color][x]:
				sh.gpio('-g', 'write', rgb_object.pins[x], 1)
				rgb_object.state = color
			else:
				sh.gpio('-g', 'write', rgb_object.pins[x], 0)
				rgb_object.state = color
		sleep(interval)
		sh.gpio('-g', 'write', rgb_object.pins[0], 0)
		sh.gpio('-g', 'write', rgb_object.pins[1], 0)
		sh.gpio('-g', 'write', rgb_object.pins[2], 0)
		sleep(interval)
	return

class rgbled:
	def __init__(self):
			    	#RGB
		self.colors = {
			'red'    : [1, 0, 0],
			'green'  : [0, 1, 0],
			'blue'   : [0, 0, 1],
			'yellow' : [1, 1, 0],
			'magenta': [1, 0, 1],
			'teal'   : [0, 1, 1],
			'white'  : [1, 1, 1],
			'off'    : [0, 0, 0]
		}
		#gpio readall - BCM_GPIO
		self.pins = [225,229,231]
		self.state= 'off'


	def setup(self):
		for p in self.pins:
			sh.gpio('-g', 'mode', p, 'out')
			sh.gpio('-g', 'write', p, 0)
		return
	
	def blink(self, color, interval):
		for t in threads:
			t.do_blink = False
			threads.pop()
		if color != 'off' and interval > 0:
			t_stop = threading.Event()
			t = threading.Thread(target = blink_thread, args=(self, color, interval, t_stop))
			threads.append(t)
			t.start()
			t.do_blink = True
		return

	def write(self, color):
		if self.state != color:
			for x in range(len(self.pins)):
				if self.colors[color][x]:
					sh.gpio('-g', 'write', self.pins[x], 1)
					self.state = color
				else:
					sh.gpio('-g', 'write', self.pins[x], 0)
					self.state = color
		return

