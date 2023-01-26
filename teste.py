import pymysql
conexao = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='cadastro'
)

cursor = conexao.cursor()
cursor.execute("select * from gafanhotos")
print(f'\033[35m{"ID":<3}| {"Nome":<30}| {"Sexo":<10}| {"Profissão":<25}| {"Nascimento"}  | {"Peso":<8}| {"Altura":<8}|'
      f' {"Nacionalidade":>3}\033[m')
print('-'*123)
for x in cursor:
    print(f'{x[0]:<3}| {x[1]:<30}| {x[4]:<10}| {x[2]:<25}| {x[3]}  | {x[5]:<8}| {x[6]:<8}| {x[7]:>3}')
