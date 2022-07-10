import urllib.request
import xml.etree.ElementTree as et
import module
# 만들어야 할것
# 1. apiget을 이용하여 버스의 운행정보 불려오기
# 2. 버스의 운행 정보 수집. 이때 출발 정류소와 도착 정류소의 버스 도착시간을 모두 수집해야 함
# 3. 수집된 정보를 기반으로, 조회를 원하면 조회 시간으로 부터 가장 가까운 버스 도착 시작대와 목적지까지의 도착 시간을 출력 해야 함
# 추가사항
# 버스 관련 api는 https://www.data.go.kr 에서 추가로 구할수 있음. 현재 추가되어 있는 api도 상세 설명을 볼 수 있음.
# 모듈화(함수)는 왠만하면 module.py에 넣을것
# 병렬화, gui 추가 등으로 py파일이 필요하면 추가할 수 있음
busname=input("버스 번호를 입력하세요")
tmp=module.getapi(busname,1)
for i in tmp[2]:
    print(i[1].text)
routenum=int(input("해당되는 노선은 몇번째에 있습니까?"))-1
routeid=tmp[2][routenum][2].text
print(routeid)
tmp=module.getapi(routeid,2)
for i in tmp[2]:
    print(i.findtext("stationName"),i.findtext("stationSeq"))
start,fin=input("원하시는 정류장 옆에 써저있는 번호를 출발 정류장, 도착 정류장 순서대로 입력하시요(띄어쓰기로 구분):").split()