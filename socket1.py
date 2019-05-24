import socket
import pymysql
import threading
import epd5in83b
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

epd = epd5in83b.EPD()
epd.init()

host = '192.168.43.231'
port = 4444
su = socket.socket(socket.AF_INET)
su.bind((host,port))
su.listen(1)
connect,address = su.accept()
print('Connected by',address)

def send():
    db = pymysql.connect(host='localhost',user='pi',passwd='1111',db='pot_db')
    cur = db.cursor()
    sql = 'SELECT light,dust,moisture,temperature FROM plant ORDER BY date DESC limit 1'
    while True:
        cur.execute(sql)
        data = cur.fetchone()
        connect.send('ok'+'/'+data[0]+'/'+data[1]+'/'+data[2]+'/'+data[3])
    print(data)
    connect.close()
    db.close()
    
def recv():
    while True:
        data = connect.recv(1024)
        if not data:
            break
        else:
            print(data)
            if data.split('/')[0] == 'ok':
                epd.Clear(0xFF)
                blackimage1=Image.new('1',(epd5in83b.EPD_HEIGHT,epd5in83b.EPD_WIDTH),255)
                redimage1=Image.new('1',(epd5in83b.EPD_HEIGHT,epd5in83b.EPD_WIDTH),255)
                newimage = Image.open('marv_black.png')
                newimage1 = Image.open('marv_red.png')

                blackimage1.paste(newimage,(50,10))
                redimage1.paste(newimage,(50,10))
    
                epd.display(epd.getbuffer(blackimage1), epd.getbuffer(redimage1))
                epd.sleep()


    connect.close()
    
threading._start_new_thread(send,())
threading._start_new_thread(recv,())

       


while True:
    pass

