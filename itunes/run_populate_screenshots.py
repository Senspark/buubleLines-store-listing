#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os, os.path

cmd = "../../../store-listing-toolkit/populate-v2.py screenshots -platform iOS -prj-path . -screenshots-path ../src/itunes/screenshots"
print cmd
os.system(cmd)
