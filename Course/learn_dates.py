
import datetime

print(datetime.MAXYEAR)
print(datetime.MINYEAR)
print(datetime.datetime.now())

begin = datetime.datetime.now()
begin = begin.replace(hour=16, minute=0, second=0)
print(begin)

event = datetime.datetime(2019, 1, 1, 0)
print(event)

datestr = '31/12/2018'
datestr = datestr.split('/')
datestr = datetime.datetime(int(datestr[2]), int(datestr[1]), int(datestr[0]))
print(datestr)


today = datetime.datetime.now()
birth = datetime.datetime(2019,3,3,0)

delta = today - birth
print(delta)

today = datetime.datetime.today()
print(today)

maintain = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(maintain)
print(maintain.weekday())

today_formatted = today.strftime('%d/%m/%Y')
print(today_formatted)


somedate = datetime.datetime.strptime('10/04/1998', '%d/%m/%Y')
print(somedate)



import timeit

timedelay = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(timedelay)
