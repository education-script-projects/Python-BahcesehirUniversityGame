#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import cv
import Key

ESC = 27

def WaitKey(delay = 0):
    c = cv.WaitKey(delay)
    if c == -1:
        ret = -1
    else:
        ret = c & ~0b100000000000000000000 

    return ret

if __name__ == '__main__':
    cv.NamedWindow("GH0ST-S0FTWARE", cv.CV_WINDOW_AUTOSIZE)
    cv.ShowImage("GH0ST-S0FTWARE", None)
    c = cv.WaitKey()
    print "%d - %d" % (c & ~0b100000000000000000000,c)
