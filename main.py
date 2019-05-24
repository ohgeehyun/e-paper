#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd5in83b
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

try:
    epd = epd5in83b.EPD()
    epd.init()
    print("Clear...")
    epd.Clear(0xFF)
    
    
    print("read bmp file on window")
    blackimage1 = Image.new('1', (epd5in83b.EPD_HEIGHT, epd5in83b.EPD_WIDTH), 255)  # 298*126
    redimage1 = Image.new('1', (epd5in83b.EPD_HEIGHT, epd5in83b.EPD_WIDTH), 255)  # 298*126    
    newimage = Image.open('marv_black.png')
    newimage1 = Image.open('marv_red.png')
    blackimage1.paste(newimage, (50,10))
    redimage1.paste(newimage1,(50,10))
    epd.display(epd.getbuffer(blackimage1), epd.getbuffer(redimage1))
    
    epd.sleep()
        
except Exception, e:
    print('traceback.format_exc():\n%s',traceback.format_exc())
    exit()
