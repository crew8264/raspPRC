#BIS 정보 확인 프로그램

def print_stop(stopk) :
    print( stopk.find('LINE_NAME').text, end = "")
    # 저상인 경우 '(저)' 추가
    if( stopk.find('LOW_BUS').text == '1') :
        print("(저)", end = "")
    else :
        print("\t", end = "")
    # end

    # 계산해서 tab 맞춰주는 함수
    namelen = len(stopk.find('BUSSTOP_NAME').text)
    if(namelen > 9) :
        print("\t" + stopk.find('BUSSTOP_NAME').text + "\t ", end = "" )
    elif(namelen > 7) :
        print("\t" + stopk.find('BUSSTOP_NAME').text + "\t\t ", end = "" )
    else :
        print("\t" + stopk.find('BUSSTOP_NAME').text + "\t\t\t ", end = "" )
    

    # 곧 도착인 경우 print문 다르게.
    if(stopk.find('ARRIVE_FLAG').text == '1') :
        print("곧 도착", end = '')
    else :
        print("약 " + stopk.find('REMAIN_MIN').text + " 분", end = "")
    # end

    print("\t    " + 
          stopk.find('REMAIN_STOP').text + "\t\t " +
          stopk.find('DIR_END').text )


import requests
import xml.etree.ElementTree as ET

url = 'http://api.gwangju.go.kr/xml/arriveInfo'
params ={'serviceKey' : '복사한 서비스 키', 
         'serviceKey' : '', 
         'BUSSTOP_ID' : '2831' }

response = requests.get(url, params=params)
xmlStr = response.content
r = ET.fromstring(xmlStr)


stop1 = r.find('ARRIVE_LIST').find('ARRIVE')
stop2 = r.find('ARRIVE_LIST').find('ARRIVE[2]')
stop3 = r.find('ARRIVE_LIST').find('ARRIVE[3]')

# 첫 번째 라인 출력.
print("<정류소: 시청>")
print("버스번호\t 현재위치\t\t\t도착예상시간\t남은정류소\t  행선지")

print_stop(stop1)
print_stop(stop2)
print_stop(stop3)

# print(response.content)
