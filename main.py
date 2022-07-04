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