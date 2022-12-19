__author__ = 'daveb'
import sys
import os

# yes, this works
#                     jcmanage       test          __init__.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib
