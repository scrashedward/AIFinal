#! /usr/bin/env python

import os
import random
import Image, ImageFont, ImageDraw
projectDir = "/home/edward/ai/"
fontDir = "/home/edward/ai/font/"
picDir = "/home/edward/ai/data/"
LINEWID = 4

def point(times):
	toReturn = []
	for i in range(times):
		toReturn.append(random.randint(0,120))
	return tuple(toReturn)

def noise(draw,number):
	for i in range(number):
		case = random.randint(0,3)
		if case==0:
			draw.line(point(4),fill="#000000", width=random.randint(1,LINEWID))
			return
		if case==1:
			draw.arc(point(4), start = random.randint(0,360), end = random.randint(0,360) ,fill="#000000")
			return
		if case==2:
			draw.rectangle(point(4), outline="#000000", fill="#ffffff")
			return

def dotnoise(draw, number):
		draw.point(point(number*2), fill="#000000")


for filename in os.listdir(fontDir):
	for j in range(3):
		print j
		for i in range(1):
			im = Image.new("RGB", (120,120), "#ffffff")
			draw = ImageDraw.Draw(im)
			font = ImageFont.truetype(fontDir+filename, 70)
			#noise(draw, random.randint(1,4))
			#dotnoise(draw, random.randint(1000, 3000))
			draw.text((40,5),chr(0x41+i),font=font,fill = "#000000")
			name = filename[:-4]+"_nonoise_nodot_"+str(j)+"_"+str(0x41+i)
			im.save(picDir+name+".jpg")

		for i in range(26):
			im = Image.new("RGB",(120,120), "#ffffff")
			draw = ImageDraw.Draw(im)
			font = ImageFont.truetype(fontDir+filename, 70)
			#noise(draw, random.randint(1,4))
			#dotnoise(draw, random.randint(1000, 3000))
			draw.text((40,5),chr(0x61+i),font=font,fill = "#000000")
			name = filename[:-4]+"_nonoise_nodot_"+str(j)+"_"+str(0x61+i)
			#print picDir+name+".jpg"
			im.save(picDir+name+".jpg")

		for i in range(10):
			im = Image.new("RGB",(120,120), "#ffffff")
			draw = ImageDraw.Draw(im)
			font = ImageFont.truetype(fontDir+filename, 70)
			#noise(draw, random.randint(1,4))
			#dotnoise(draw, random.randint(1000, 3000))
			draw.text((40,5),chr(0x30+i),font=font,fill = "#000000")
			name = filename[:-4]+"_nonoise_nodot_"+str(j)+"_"+str(0x30+i)
			#print picDir+name+".jpg"
			im.save(picDir+name+".jpg")
