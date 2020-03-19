import pymysql

def num(n):
    #print(n)
    if n[len(n)-1] == '万':

        return float(n[0:len(n)-1])*10000
    else:
        return int(n)

def csv_to_mysql():
    print('csv2mysql')
    db = pymysql.connect("localhost","root","password","pb")
    cursor = db.cursor()
    delete_sql = "truncate table contents "

    cursor.execute(delete_sql)
    #print("清空数据")
    sql = "INSERT INTO contents(title, \
       author, author_des, date, views, loves,zans,comment_num,url ) \
       VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
    print('insert')
    
    file = open('./data.csv','r').readlines()
    for f in file:
        val = []
        f = f.split(',')
        

        if len(f) ==9 and f[0] != 'title': 
            #print(f)
            #处理数据中 1.3 万这种情况
            f[4] = num(f[4])
            f[5] = num(f[5])
            f[6] = num(f[6])
            f[7] = num(f[7])
            val.append(f)
            # 执行sql语句
            cursor.executemany(sql,val)
        elif len(f) > 9 and f[0] != 'title': 
            #print('f[0:4]:{}'.format(f[0:3]))
            #print('f[-6:-1]:{}'.format(f[-6:]))

            f_9 = f[0:3]+f[-6:]
            #处理数据中 1.3 万这种情况
            f_9[4] = num(f_9[4])
            f_9[5] = num(f_9[5])
            f_9[6] = num(f_9[6])
            f_9[7] = num(f_9[7])
            #print("if len(f) > 9:{}",format(f_9))
            val.append(f_9)
            cursor.executemany(sql,val)
            continue
    db.commit()
    # 关闭数据库连接
    db.close()  