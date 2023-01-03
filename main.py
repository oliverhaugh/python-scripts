#!/usr/bin/env python3

import os

from time import sleep

from ctypes import *

import sys



 # Determine the amount of RAM needed to run this program.

# The value is in bytes, so it should be a number between 0 and 4294967295.

RAM_SIZE = 8192



 # You need two functions to create the virtual machine: one to open the disk image, and one to create a new process. We'll call these functions load_disk() and start_process(), respectively.



 # Load the disk image, which is located at "msdos.img" on your computer's hard drive, by calling load_disk() with the path to it as an argument. If everything goes well, you should see output like this:

print('Loading disk image...')

with open ( 'msdos.img' , 'wb' ) as fh :

# This will write bytes from file descriptor 3 into memory space starting at byte offset 0x000006000 and ending at byte offset 0x000007000 which is where our disk begins (the first sector).

    fh.write( b, ' \x00 '* RAM_SIZE )