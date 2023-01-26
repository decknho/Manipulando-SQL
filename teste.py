import pymysql
conexao = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='cadastro'
)

cursor = conexao.cursor()
cursor.execute("select * from gafanhotos")

for x in cursor:
    print(x)
