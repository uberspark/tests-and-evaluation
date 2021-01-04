#!/usr/bin/env python3
import time

from sys import argv, exit


def print_usage():
	"""Print the usage string if script was used improperly"""
	print('Usage: \
		\t$ {} <pid> <heap_addr from heap start> <byte0> <byte1> <byte2> <byte3> <byte4>'.format(argv[0]))
	print("e.g. : \t$ python3 mem_attack.py 21566 0x64ed88 0 0 0 0 0")
	exit(1)


def read_write_heap(pid, offset, byte0, byte1, byte2, byte3, byte4):
	"""Find @read_str in the heap of @pid and replace it with @write_str"""
	try:
		maps_file = open("/proc/{}/maps".format(pid), 'r')
	except IOError as e:
		print("Can't open file /proc/{}/maps: IOError: {}".format(pid, e))
		exit(1)
	heap_info = None
	for line in maps_file:
		if 'heap' in line:
			heap_info = line.split()
	maps_file.close()
	if 'heap' == None:
		print('No heap found!')
		exit(1)
	addr = heap_info[0].split('-')
	perms = heap_info[1]
	if 'r' not in perms or 'w' not in perms:
		print('Heap does not have read and/or write permission')
		exit(0)
	try:
		mem_file = open("/proc/{}/mem".format(pid), 'rb+')
	except IOError as e:
		print("Can't open file /proc/{}/maps: IOError: {}".format(pid, e))
		exit(1)
	heap_start = int(addr[0], 16)
	heap_end = int(addr[1], 16)
	mem_file.seek(heap_start)
	heap = mem_file.read(heap_end - heap_start)
	int_offset = int(offset,16)
	print(hex(int_offset))
	while True:
		mem_file.seek(int_offset)
		mem_file.write(b0.to_bytes(4,byteorder='little'))
		mem_file.write(b1.to_bytes(4,byteorder='little'))
		mem_file.write(b2.to_bytes(4,byteorder='little'))
		mem_file.write(b3.to_bytes(4,byteorder='little'))
		mem_file.write(b4.to_bytes(4,byteorder='little'))
		mem_file.flush()
		time.sleep(0.005)
	mem_file.close()


if (len(argv) == 8):
	pid = argv[1]
	offset = argv[2]
	b0 = int(argv[3])
	b1 = int(argv[4])
	b2 = int(argv[5])
	b3 = int(argv[6])
	b4 = int(argv[7])
	read_write_heap(pid, offset, b0, b1, b2, b3, b4)
else:
	print_usage()
