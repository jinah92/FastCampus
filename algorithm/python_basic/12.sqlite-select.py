# 파이썬 데이터베이스 연동(SQLite3)
# 테이블 조회

import sqlite3

# DB파일 조회(없으면 새로 생성)
conn = sqlite3.connect(
    'D:/study/FastCam/algorithm/python_basic/resource/database.db')

# 커서 바인딩
c = conn.cursor()

# 데이터 조회
c.execute("SELECT * FROM users")

# 커서 위치가 변경
# 1개 row를 선택
# print('One -> \n', c.fetchone())

# 지정한 row만큼을 선택
# print('Three -> \n', c.fetchmany(size=3))

# 전체 row 선택
# print('All -> \n', c.fetchall())
# print(c.fetchall())   # []


# 테이블 데이터 순회
# rows = c.fetchall()
# ex 1
# for row in rows:
#     print('retrieve 1 > ', row)

# ex 2
# for row in c.fetchall():
#     print('retrieve 2 > ', row)

# ex 3
# for row in c.execute('SELECT * FROM users ORDER BY id DESC'):
#     print('retrieve 3 > ', row)


# Where Retrieve 1
param1 = (3, )
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1', c.fetchone())
print('param1', c.fetchall())   # 데이터 없음 (한개만 조회한지를 확인)

# Where Retrieve 2
param2 = 4
c.execute('SELECT * FROM users WHERE id="%s"' % param2) # %s, %f, %d
print('param2', c.fetchone())
print('param2', c.fetchall())   # 데이터 없음 (한개만 조회한지를 확인)

# Where Retrieve 3
c.execute('SELECT * FROM users WHERE id=:Id', {"Id": 5})
print('param3', c.fetchone())
print('param3', c.fetchall())   # 데이터 없음 (한개만 조회한지를 확인)


# Where Retrieve 4
param4 = (3, 5)
c.execute("SELECT * FROM users WHERE id IN(?,?)", param4)
print('param4', c.fetchall())

# Where Retrieve 5
c.execute("SELECT * FROM users WHERE id IN('%d', '%d')" % (3, 4))
print('param5', c.fetchall())

# Where Retrieve 6
c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2", {"id1": 2, "id2": 5})
print('param6', c.fetchall())


# Dump 출력
with conn:
    with open('D:/study/FastCam/algorithm/python_basic/resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)

        print('dump print complte')

# f.close(), conn.close()
