#!/usr/bin/env python2
# -*- coding:utf-8 -*-

import cv as python_opencv_modulu
import Key as anahtar
import random as rasgele

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
 	         #########################################################
   		 #              DEVELOPER : İSMAİL TAŞDELEN              #                       
   		 #        Mail Address : pentestdatabase@gmail.com       #
   		 # LINKEDIN : https://www.linkedin.com/in/ismailtasdelen #
   		 #           Whatsapp : + 90 534 295 94 31               #
  	         #########################################################
"""

class Hedef:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.hiz = (0,1)
        self.aktif = True

    def getDimensions(self):
        return (self.x, self.y, self.width, self.height)

    def centerOrigin(self):
        return (self.x - self.width/2, self.y - self.height/2)

    def update(self):
        self.x += self.hiz[0]
        self.y += self.hiz[1]

python_opencv_modulu.NamedWindow("Python - Bahçeşehir University Game", python_opencv_modulu.CV_WINDOW_AUTOSIZE)
elips_sekil_kalibi = python_opencv_modulu.CreateStructuringElementEx(9,9, 4, 4, python_opencv_modulu.CV_SHAPE_ELLIPSE)
kamera = python_opencv_modulu.CaptureFromCAM(-1)
cerceve_boyutu = (int(python_opencv_modulu.GetCaptureProperty(kamera, python_opencv_modulu.CV_CAP_PROP_FRAME_WIDTH)),int(python_opencv_modulu.GetCaptureProperty(kamera, python_opencv_modulu.CV_CAP_PROP_FRAME_HEIGHT)))
yazdir_goruntuyu = False
fourcc_degeri = python_opencv_modulu.FOURCC('M', 'J', 'P', 'G')
fps_degeri = 30

if yazdir_goruntuyu:
    video_yazdir = python_opencv_modulu.CreateVideoWriter("film.avi", fourcc_degeri, fps_degeri, cerceve_boyutu)

previous = python_opencv_modulu.CreateImage(cerceve_boyutu, 8L, 3)
python_opencv_modulu.SetZero(previous)
difference = python_opencv_modulu.CreateImage(cerceve_boyutu, 8L, 3)
python_opencv_modulu.SetZero(difference)
current = python_opencv_modulu.CreateImage(cerceve_boyutu, 8L, 3)
python_opencv_modulu.SetZero(current)
logo_bau_original = python_opencv_modulu.LoadImage("img/logo-bau.png")
logo_bau = python_opencv_modulu.CreateImage((64,64), logo_bau_original.depth, logo_bau_original.channels)
python_opencv_modulu.Resize(logo_bau_original, logo_bau)
logo_design_original = python_opencv_modulu.LoadImage("img/logo-design.png")
logo_design = python_opencv_modulu.CreateImage((64,64), logo_design_original.depth, logo_design_original.channels)
python_opencv_modulu.Resize(logo_design_original, logo_design)

def hit_value(resim, hedef):
    roi = python_opencv_modulu.GetSubRect(resim, hedef.getDimensions())
    return python_opencv_modulu.CountNonZero(roi)

def hedefleri_olustur(deger_say):
    hedefler = list()
    for i in range(deger_say):
        hedef_konumu = Hedef(rasgele.randint(0, cerceve_boyutu[0]-logo_bau.width), 0)
        hedef_konumu.width = logo_bau.width
        hedef_konumu.height = logo_bau.height
        hedefler.append(hedef_konumu)

    return hedefler

sayi = 5
hedefler = hedefleri_olustur(sayi)
gecikme_zamani = 100
skor = 0
yazi_tipi = python_opencv_modulu.InitFont(python_opencv_modulu.CV_FONT_HERSHEY_SIMPLEX, 1, 1)

while True:
    goruntu_yakala = python_opencv_modulu.QueryFrame(kamera)
    python_opencv_modulu.Flip(goruntu_yakala, goruntu_yakala, flipMode=1)
    python_opencv_modulu.Smooth(goruntu_yakala, current, python_opencv_modulu.CV_BLUR, 15,15)
    python_opencv_modulu.AbsDiff(current, previous, difference)
    cerceve = python_opencv_modulu.CreateImage(cerceve_boyutu, 8, 1)
    python_opencv_modulu.CvtColor(difference, cerceve, python_opencv_modulu.CV_BGR2GRAY)
    python_opencv_modulu.Threshold(cerceve, cerceve, 10, 0xff, python_opencv_modulu.CV_THRESH_BINARY)
    python_opencv_modulu.Dilate(cerceve, cerceve, element=elips_sekil_kalibi, iterations=3)

    if gecikme_zamani <= 0:
        for toplam in hedefler:
            if toplam.aktif:
                sifir = hit_value(cerceve, toplam)
                if sifir < 1000:
                    python_opencv_modulu.SetImageROI(goruntu_yakala, toplam.getDimensions())
                    python_opencv_modulu.Copy(logo_bau, goruntu_yakala, logo_design)
                    python_opencv_modulu.ResetImageROI(goruntu_yakala)
                    toplam.update()
                    if toplam.y + toplam.height >= cerceve_boyutu[1]:
                        toplam.aktif = False
                        sayi -= 1
                else:
                    toplam.y = 0
                    toplam.x = rasgele.randint(0, cerceve_boyutu[0]-logo_bau.width)
                    if toplam.hiz[1] < 15:
                        toplam.hiz = (0, toplam.hiz[1]+1)
                    skor += sayi

    python_opencv_modulu.PutText(goruntu_yakala, "Skorunuz : %d" % skor, (10,cerceve_boyutu[1]-10), yazi_tipi, python_opencv_modulu.RGB(0,0,0))
    python_opencv_modulu.ShowImage("Python - Bahçeşehir University Game", cerceve)
    if yazdir_goruntuyu:
        python_opencv_modulu.WriteFrame(video_yazdir, goruntu_yakala)
    python_opencv_modulu.ShowImage("Python - Bahçeşehir University Game", goruntu_yakala)
    previous = python_opencv_modulu.CloneImage(current)
    beklenen_anahtar = anahtar.WaitKey(2)
    if beklenen_anahtar == 27:
        break

    gecikme_zamani -= 1

print skor
