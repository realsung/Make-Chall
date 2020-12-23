#!/usr/bin/python
#-*-coding:utf-8-*-
import qrcode
import random
import string
import time
import signal
import sys
import os
from PIL import Image

FLAG = "Defenit{QQu!_3sC4p3_FR0m_D3v1l!_n1c3_C0gN1z3!}"
STRS = string.ascii_letters + string.digits
MENU = '''@  ###   ####           ####                                      #                  @
@ #   #  #   #         #       ###   # ##    ###   # ##    ####  ####    ###   # ##  @
@ #   #  ####          #  ##  #####  ##  #  #####  ##     #   #   #     #   #  ##    @
@ #   #  # #           #   #  #      #   #  #      #      #  ##   #     #   #  #     @
@  ###   #  ##          ####   ###   #   #   ###   #       ## #    ##    ###   #     @
@    ##                                                                              @'''.replace(' ','.')

MENU2 = '''
Hi, Here is Defenit QR Generator.
I heard the QR devil made 100 stages.'''
# word_lists = []

def print_menu():
	write('@'*86)
	write(MENU)
	write('@'*86)
	write(MENU2)

def generateQR(randString):
	qr = qrcode.QRCode(
	version=random.randint(1,10), # version RANDOM!?
	error_correction=qrcode.constants.ERROR_CORRECT_L,
	box_size=1,
	border=0,)

	qr.add_data(randString)
	
	qr.make(fit=True)
	
	img = qr.make_image(fill_color="black", back_color="white")
	
	img.save(randString+'.png') # 경로 랜덤으로 tmp에 지정해야할듯 # /tmp/QR/

def generateSTR(length):
	res = ""
	for _ in range(length):
		res += random.choice(STRS)
	return res

def makeQR(randString):
	img = Image.open(randString+'.png') # /tmp/QR/
	img = img.convert('RGB')
	img_pix = img.load()
	# r,g,b = img_pix[0,0]
	# (width, height) = im.size
	black = (0,0,0)
	white = (255,255,255)

	text = ''

	for i in range(0, img.width):
		for j in range(0, img.height):
			if img_pix[i,j] == black:
				text += '1 '
			elif img_pix[i,j] == white:
				text += '0 '
		text += '\n'

	write('< QR >')
	write(text)

def handler(signum, frame):
	write("Time Over!")
	sys.exit(0)

def write(data, endl='\n'):
	sys.stdout.write(data + endl)
	sys.stdout.flush()

def generateLEN():
	return random.randint(30,150)

# def delFile():
# 	for i in word_lists:
# 		os.remove(i)

def delFile(filename):
	os.remove(filename+'.png')

if __name__ == '__main__':
	# POW?
	print_menu()
	time.sleep(1)
	try:
		signal.signal(signal.SIGALRM, handler)
		signal.alarm(5)
		sys.stdout.write("What is your Hero's name? ")
		sys.stdout.flush()
		hero = sys.stdin.readline().strip()
	except:
		exit(0)
	CHECK = 1

	time.sleep(0.5)
	write('Thank you so much *'+ hero +'* please escape from the QR devil')
	time.sleep(0.5)
	write("Let's START!")
	while True:
		try:
			sys.stdout.write('\n')
			sys.stdout.flush()
			if CHECK == 101: # Number
				write('Thank you *' + hero + '* I will give you FLAG!')
				write(FLAG)
				exit(0)
			randLen = generateLEN()
			randStr = generateSTR(randLen)
			# write(randStr) # 주석
			generateQR(randStr)
			makeQR(randStr)
			delFile(randStr)
			signal.signal(signal.SIGALRM, handler)
			signal.alarm(10)

			write('STAGE ' + str(CHECK))
			
			sys.stdout.write('>> ')
			sys.stdout.flush()
			inputStr = sys.stdin.readline().strip()
			if inputStr == randStr:
				CHECK += 1
				write('Correct!')
			else:
				write('Try again')
				exit(0)
		except:
			exit(0)
