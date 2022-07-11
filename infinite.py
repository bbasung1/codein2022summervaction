from curses import mouseinterval
import sys
import module
import sqlite3 as sql
import time
conn=sql.connect("route.db")
cur=conn.cursor()
cur.execute(f"create table if not exists R{sys.argv[3]}(reg_date datetime default (datetime(current_timestamp,'localtime')) not null, plateNo string, stationSeq integer,stationId integer);")
while(1):
    conn=sql.connect('route.db')
    cur=conn.cursor()
    try:
        tree=module.getapi(sys.argv[3],0)
    except Exception as e:
        print("에러발생, 30초후재접속 시도합니다.error code:"+str(e))
        time.sleep(30)
        continue
    if(len(tree)>=3):
        for i in range( len(tree[2])):
            print(tree[2][i][2].text,tree[2][i][7].text,tree[2][i][6].text)
            cur.execute(f"select * from R{sys.argv[3]} where plateNo=? order by reg_date desc limit 1;",(tree[2][i][2].text,))
            flag=0
            while(True):
                row=cur.fetchone()
                if row==None:
                    if(flag==0):
                        cur.execute(f"insert into R{sys.argv[3]} ('plateNo','stationSeq','stationId') values(?,?,?);",(tree[2][i][2].text,tree[2][i][7].text,tree[2][i][6].text))
                    break;
                print(int(row[2]),int(tree[2][i][7].text))
                flag+=1
                if(row[2]!=int(tree[2][i][7].text)):   
                    cur.execute(f"insert into R{sys.argv[3]} ('plateNo','stationSeq','stationId') values(?,?,?);",(tree[2][i][2].text,tree[2][i][7].text,tree[2][i][6].text))
            conn.commit()
    else:
        print("인덱스 오류")
    conn.close()
    print("60초 대기 시작. routeid=",busroute)
    time.sleep(60)
    print("60초 대기 완료")