import sqlite3
def criar_tabela():
    con = sqlite3.connect('person.db')

    cur = con.cursor()
    sql_create = 'create table IF NOT EXISTS personagem'\
    '( ID INTEGER PRIMARY KEY AUTOINCREMENT not null,'\
    'nome varchar(45) not null unique,'\
    'classe varchar(30) not null,'\
    'level int not null,'\
    'xp INT NOT NULL,'\
    'hp int not null,'\
    'power int not null,'\
    'for int not null,'\
    'con int not null,'\
    'des int not null,'\
    'intel int not null,'\
    'pontos int not null)'

    cur.execute(sql_create)
    

    cur.close()
    con.close()


def scan(nome):
    bd = sqlite3.connect('person.db')
    cur = bd.cursor()

    item = '"'+nome+'"'
    sql_select = 'select *\
                from personagem as p\
                where p.nome = '
    sql_select += item
    cur.execute(sql_select)
    
    for i in cur.fetchall():
        if i[1] == nome:
            return 1
        else :
            return 0 

    cur.close()
    bd.close()

def buscar(nome):
    bd = sqlite3.connect('person.db')
    cur = bd.cursor()

    item = '"'+nome+'"'
    sql_select = 'select *\
                from personagem as p\
                where p.nome = '
    sql_select+=item
    cur.execute(sql_select)

    for linha in cur.fetchall():
        if linha[1] == nome:
            print('Nome:',linha[1],'    ',linha[2],'Nv.',linha[3],' ',linha[4],'/',linha[5],'XP\n',\
                'HP:',linha[6],'        ','Power:',linha[7],'\n',\
                'For:',linha[8],'       ','Con:',linha[9],'\n',\
                'Des:',linha[10],'       ','Int:',linha[11],'\n',\
                'Pontos:',linha[12])
    cur.close()
    bd.close()

def buscar_tds():  
    bd = sqlite3.connect('person.db')
    cur = bd.cursor()

    sql_select = 'select *\
                from personagem '
    
    cur.execute(sql_select)

    for linha in cur.fetchall():
        print(linha[1],'  ',linha[2],' Nv.',linha[3])
    
    cur.close()
    bd.close()

def insert (lista):
    bd = sqlite3.connect('person.db')
    cur = bd.cursor()
    
    sql_insert='INSERT INTO personagem (nome,classe,level,xp,xp_up,hp,power,for,con,des,intel,pontos) \
                values(?,?,?,?,?,?,?,?,?,?,?,?)'
    cur.execute(sql_insert,lista)
    bd.commit()
    cur.close()
    bd.close()

def select (nome):
    bd = sqlite3.connect('person.db')
    cur = bd.cursor()

    item = '"'+nome+'"'
    sql_select = 'select p.ID, p.classe ,p.level, p.xp, p.for, p.con, p.des, p.intel, p.pontos\
                from personagem as p \
                    where p.nome = '
    
    sql_select+=item
    cur.execute(sql_select)
    for lista in cur.fetchall():
        return [lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],lista[8],lista[0]]
    cur.close()
    bd.close()

def guardar(lista):
    bd = sqlite3.connect('person.db')
    cur = bd.cursor()
    #print(lista)
    sql_up = 'UPDATE personagem SET level = ?, xp = ?,xp_up = ?, hp= ?, power = ?, for = ?, con = ?, des = ?, intel = ?, pontos = ? \
        WHERE ID = ?'
    

    cur.execute(sql_up,lista)
    bd.commit()

    cur.close()
    bd.close()

criar_tabela()