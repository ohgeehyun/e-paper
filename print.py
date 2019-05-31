import pymysql

error = 0

db = pymysql.connect(host='localhost',user='pi',passwd='1111',db='pot_db')
cur = db.cursor()
sql = 'select * from value ORDER BY data DESC limit 1'
sql2 = 'select value from current'
cur.execute(sql)
data = cur.fetchone()
lightHigh = data[1]
lightLow = data[2]
dust_v = data[3]
moisture_v = data[4]
tempHigh = data[5]
tempLow = data[6]

sql1 = 'select * from plant ORDER BY date DESC limit 1'
cur.execute(sql1)
data1 = cur.fetchone()
dust = data1[1]
light = data1[2]
moisture = data1[3]
temporature = data1[5]



if light > lightHigh:
    error +=1
elif light < lightLow:
    error +=1
if dust_v > dust:
    error +=1
if moisture < moisture_v:
    error +=1
if temporature > tempHigh:
    error +=1
elif temporature < tempLow:
    error +=1

if error >=2:
    now = 0
elif light < lightLow:
    now = 1
elif moisture <= moisture_v:
    now = 2
elif light > lightHigh:
    now = 3
elif temporature <= tempLow:
    now = 4
elif temporature >= tempHigh:
    now = 5
elif dust >= dust_v:
    now = 6
else:
    now = 7

cur.execute(sql2)
current = cur.fetchone()



if now!=current:
    if now == 0:
        import skeleton
    elif now == 1:
        import sleep
    elif now == 2:
        import thirsty
    elif now == 3:
        import bright
    elif now == 4:
        import cold
    elif now == 5:
        import hot
    elif now == 6:
        import dust
    elif now == 7:
        import normal

sql3 = 'update current set value = %s'
cur.execute(sql3,current)
db.commit()
db.close()

