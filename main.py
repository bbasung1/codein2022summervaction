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
    # 0. centerYn:중앙차로 여부
    # 1. districtCd: 구역 번호
    # 2. moblieNo: 정류장 번호
    # 3. regionName: 지역 이름
    # 4. stationId: api에서 사용되는 정류장idct
    # 5. stationName: 정류장 이름
    # 6. x: 정류장의 x좌표
    # 7. y: 정류장의 y좌표
    # 8. stationSeq: 정류장 순번
    # 9. turnYn: 회자지점 여부
