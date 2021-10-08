from distutils.core import setup # Need this to handle modules
import py2exe
import keyboard
import mouse
import time
from subprocess import Popen
import os
import configparser

global actionCounter

setup(console=['apm_manager.py']) # Calls setup function to indicate that we're dealing with a single console application