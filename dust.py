#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd5in83b
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

try:
    #초기화 시작
    epd = epd5in83b.EPD()
    epd.init()
    print("Clear...")
    # Drawing on the Horizontal image
   # HBlackimage = Image.new('1', (epd5in83b.EPD_WIDTH, epd5in83b.EPD_HEIGHT), 255)  # 298*126
   # HRedimage = Image.new('1', (epd5in83b.EPD_WIDTH, epd5in83b.EPD_HEIGHT), 255)  # 298*126    
    
    
    # 여기 부터가 순서대로 이미지를 불러와서 뛰웁니다 
    print("read bmp file on window")
    blackimage1 = Image.new('1', (epd5in83b.EPD_HEIGHT, epd5in83b.EPD_WIDTH), 255)  # 298*126
    redimage1 = Image.new('1', (epd5in83b.EPD_HEIGHT, epd5in83b.EPD_WIDTH), 255)  # 298*126    
    newimage = Image.open('dust.png') # 이미지파일을 여기에등록만하기
    blackimage1.paste(newimage, (50,10))
    epd.display(epd.getbuffer(blackimage1), epd.getbuffer(redimage1))
    
    epd.sleep()
        
except Exception, e:
    print('traceback.format_exc():\n%s',traceback.format_exc())
    exit()
