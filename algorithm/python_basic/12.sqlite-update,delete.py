# 파이썬 데이터베이스 연동(SQLite)
# 테이블 데이터 수정 및 삭제

import sqlite3

# DB 생성(파일)
conn = sqlite3.connect(
    'D:/study/FastCam/algorithm/python_basic/resource/database.db')

# Cursor 연결
c = conn.cursor()

#데이터 수정 1
# c.execute("UPDATE users SET username = ? WHERE id = ?", ('niceman', 2))

#데이터 수정 2
# c.execute("UPDATE users SET username = :name WHERE id = :id", {"name" : 'goodman', "id" : 5})

#데이터 수정 3
# c.execute("UPDATE users SET username = '%s' WHERE id = '%s'" % ('badboy', 3))


# 중간 데이터 확인 1
for user in c.execute("SELECT * FROM users"):
    print(user)

# Delete 1
# c.execute("DELETE FROM users WHERE id = ?", (2,))

# Delete 2
# c.execute("DELETE FROM users WHERE id = :id", {"id" : 5})

# Delete 3
# c.execute("DELETE FROM users WHERE id = '%s'" % 4)

print()

# 중간 데이터 확인 2
for user in c.execute("SELECT * FROM users"):
    print(user)

# 테이블 전체 데이터 삭제
print("user db deleted : ", conn.execute("DELETE FROM users").rowcount, " rows")

conn.commit()   # 커밋해야 반영
conn.close()    # 접속 해제