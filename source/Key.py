#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import cv
import Key

bau_game_text_ico = """
▄▄▄▄·  ▄▄▄· ▄• ▄▌    ▄• ▄▌ ▐ ▄ ▪   ▌ ▐·▄▄▄ .▄▄▄  .▄▄ · ▪  ▄▄▄▄▄ ▄· ▄▌     ▄▄ •  ▄▄▄· • ▌ ▄ ·. ▄▄▄ .
▐█ ▀█▪▐█ ▀█ █▪██▌    █▪██▌•█▌▐███ ▪█·█▌▀▄.▀·▀▄ █·▐█ ▀. ██ •██  ▐█▪██▌    ▐█ ▀ ▪▐█ ▀█ ·██ ▐███▪▀▄.▀·
▐█▀▀█▄▄█▀▀█ █▌▐█▌    █▌▐█▌▐█▐▐▌▐█·▐█▐█•▐▀▀▪▄▐▀▀▄ ▄▀▀▀█▄▐█· ▐█.▪▐█▌▐█▪    ▄█ ▀█▄▄█▀▀█ ▐█ ▌▐▌▐█·▐▀▀▪▄
██▄▪▐█▐█ ▪▐▌▐█▄█▌    ▐█▄█▌██▐█▌▐█▌ ███ ▐█▄▄▌▐█•█▌▐█▄▪▐█▐█▌ ▐█▌· ▐█▀·.    ▐█▄▪▐█▐█ ▪▐▌██ ██▌▐█▌▐█▄▄▌
·▀▀▀▀  ▀  ▀  ▀▀▀      ▀▀▀ ▀▀ █▪▀▀▀. ▀   ▀▀▀ .▀  ▀ ▀▀▀▀ ▀▀▀ ▀▀▀   ▀ •     ·▀▀▀▀  ▀  ▀ ▀▀  █▪▀▀▀ ▀▀▀ 

   		 #########################################################
   		 #  PYTHON - Bahcesehir University Game - GH0ST S0FTWARE #
  		 ######################################################### 
   		 #                       CONTACT                         #
 	      ########################################################
   		 #              DEVELOPER : İSMAİL TAŞDELEN              #                       
   		 #        Mail Address : pentestdatabase@gmail.com       #
   		 # LINKEDIN : https://www.linkedin.com/in/ismailtasdelen #
   		 #           Whatsapp : + 90 534 295 94 31               #
  	     #########################################################
"""

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
