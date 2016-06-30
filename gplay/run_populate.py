#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os, os.path

cmd = "../../../store-listing-toolkit/populate-v2.py metadata -platform android -prj-path . -sheet 1VwJOD_d8jV4VWZOX1gvT_mwbCTBpZXY9JSl7y8yEARQ -customized-metadata-path ../src/gplay/metadata"
print cmd
os.system(cmd)
