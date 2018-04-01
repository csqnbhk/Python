import pymysql
conn = pymysql.connect(host='localhost', user='root', password='123456', db='stories', port=3306, charset='utf8')
cur = conn.cursor()

answer_list = []
if __name__ == '__main__':
    with open('C:\\Users\\Administrator\\Desktop\\answer.text', 'r',encoding='utf-8') as f:
        line = f.readline()
        while line:
            answer_list.append(line)
            line = f.readline()
    print('answer如下,总有行数:{}'.format(answer_list.__len__()))
    id = 1
    sql = ""
    cur.execute('set sql_safe_updates=0;')
    conn.commit()  # 只有提交才可以，对下面生效
    cur.execute('set sql_safe_updates=0;')
    for item in answer_list:
        sql = "update  horror_story set answer='{}' where id={};".format(item, id)
        print(sql)
        cur.execute(sql)
        id = id+1
        print(item)
    cur.execute('set sql_safe_updates=1')
    conn.commit()
    conn.close()

