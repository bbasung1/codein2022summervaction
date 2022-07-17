import urllib.request
import xml.etree.ElementTree as et
import sqlite3
import pandas as pd


def getapi(url,param):
    qu=['http://apis.data.go.kr/6410000/buslocationservice/getBusLocationList?serviceKey=PT8WA9S%2BrAN3hvm6e2CSDvOaiWJlRWpu%2BvQ7qNtKAylxcLJILSF%2FLQyGWfsCNvLmCGnzjCAmULm57lZ8ayGC9g%3D%3D&routeId=','http://apis.data.go.kr/6410000/busrouteservice/getBusRouteList?serviceKey=PT8WA9S%2BrAN3hvm6e2CSDvOaiWJlRWpu%2BvQ7qNtKAylxcLJILSF%2FLQyGWfsCNvLmCGnzjCAmULm57lZ8ayGC9g%3D%3D&keyword=',
    'http://apis.data.go.kr/6410000/busrouteservice/getBusRouteStationList?serviceKey=PT8WA9S%2BrAN3hvm6e2CSDvOaiWJlRWpu%2BvQ7qNtKAylxcLJILSF%2FLQyGWfsCNvLmCGnzjCAmULm57lZ8ayGC9g%3D%3D&routeId=','http://apis.data.go.kr/6410000/busarrivalservice/getBusArrivalList?serviceKey=8OWMPYaTZ4PMgOeGsovqKTfjkWCuRlqB7OEgrvdvM4Ba8AxxStp500d3mnK0MsNlB32I6rBi4P7x2H6nI5JvHA%3D%3D&stationId=']
    #qu[0]:url에 해당하는 routeid를 가진 버스의 위치를 알려줍니다
    #qu[1]:url에 해당하는 번호를 가진 버스들의 목록을 가지고 옵니다.
    #qu[2]:url에 해당하는 routeid를 가진 버스의 노선 목록을 가지고 옵니다.
    #qu[3]:url에 해당하는 stationId를 통해 버스도착정보목록을 조회할 수 있다.
    #테스트를 할떄 사용할 버스 노선 목록
    #7770(routeid:233000031): 24시간 운영하는 버스임으로 정상 테스트 하기에 좋음
    #8147(routeid:241000820): 오후 10시 30분 경이면 운행이 종료됨으로 잘못된 정보 수신시 테스트 할 떄 좋음
    api=urllib.request.urlopen(urllib.request.Request(qu[param]+url))
    resbody=api.read().decode('utf-8')
    return et.fromstring(resbody)

def getRouteid():
    busname = input("버스 번호를 입력하세요: ")
    response = getapi(busname,1)
    for i in response[2]:
        print(i[1].text)
    routenum = int(input("해당되는 노선은 몇번째에 있습니까?: "))-1
    routeid = response[2][routenum][2].text
    print("버스 조회용 id는 "+routeid+"입니다.")
    return routeid

def bus_db():
    conn = sqlite3.connect("bustest1.db")
    cur = conn.cursor()
    conn.close()

def getStionId():
    mylocation = input("가장 가까운 역이름을 적으세요")


    #공통적으로 메인 정보는 [2][i][j]에 들어있음.
    #[j]정보
    #qu[0]
    # 0. endBus : 버스가 막차인가
    # 1. lowPlate: 버스가 저상버스인가
    # 2. platNno: 버스의 차 번호
    # 3. plateType: 버스의 종류(2층버스 등...) 3 = 대형승합차
    # 4. remainSeatCnt: 버스의 남은 좌석 수
    # 5. routeId: 버스 조회용 id
    # 6. stationId: 현재 정류장의 id
    # 7. stationSeq: 버스 노선에서 현재 정류장의 순서
    #qu[1]
    # 0. districtCd:운행 권역
    # 1. regionName:운행하는 지역
    # 2. routeId:노선의 api 조회용 id
    # 3. routeName:노선번호
    # 4. routeTypeCd:노선종류 번호
    # 5. routeTypeName: 노선 종류
    # qu[2]
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
    #qu[3]
    # 0. flag: 상태구분(run,pass: 운행중 / stop: 운행종료)
    # 1. locationNo1: 첫번째차량 위치 정보(몇번째전 정류소)
    # 2. locationNo2: 두번째차량 위치 정보
    # 3. lowPlate1: 첫번째차랑 저상버스여부
    # 4. lowPlate2: 두번째차랑 저상버스여부
    # 5. plateNo1: 첫번째차량 차량번호
    # 6. plateNo2: 두번째차량 차량번호
    # 7. predictTime1: 첫번째차량 도착예상시간
    # 8. predictTime2: 두번째차량 도착예상시간
    # 9. remainSeatCnt1: 첫번째차량 빈자리 수
    # 10. remainSeatCnt2: 두번째차량 빈자리 수
    # 11. routeId: 노선 아이디
    # 12. staOrder: 노선의 정류소순번
    # 13. stationId: 정류소 아이디
