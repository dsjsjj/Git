import pymssql
def getstu():
    print('-----')
    conn = pymssql.connect(host='127.0.0.1',user='U1',password='123456',database='St',charset='UTF-8')
    print(conn)
    print('连接成功！')
    cursor = conn.cursor()
    sql = "select * from Student"
    cursor.execute(sql)
    rsone = cursor.fetchone()
    print(rsone)
    list = cursor.fetchall()
    for row in list:
        print(row[0],row[1].encode('latin-1').decode('gbk'))
        

if __name__=='__main__':
    getstu()
    