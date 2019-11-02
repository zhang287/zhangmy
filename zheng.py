import re
from django.http import HttpResponse
import time
# s='123hello \n word___'
# r=re.findall('1',s)
# print(r)

# def getday(request,year,date,times):
#     print(year)
#     print(date)
#     print(times)
#     return HttpResponse('%s年%s月%s日'%(year,date,times))
r=time.localtime()
# print(r)
def getday(request,year,moth,data):
    # data=year+'-'+moth+'-'+dat
    r = time.strftime('%j',time.strptime((year+'-'+moth+'-'+data),'%Y-%m-%d'))
    # return HttpResponse('{}年{}月{}日是第{}天'.format(year,moth,dat))
    return HttpResponse('{}年{}月{}日是今年的第{}天'.format(year,moth,data,r))




