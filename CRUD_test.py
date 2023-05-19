import mysql.connector
from prettytable import PrettyTable

# Conexão global para o CRUD
cnx = mysql.connector.connect(user='#', password='#', \
                            host='#', \
                            database='nome do nosso data base')

'''
CREATE TABLE tb_dis(
 idt_dis INT AUTO_INCREMENT PRIMARY KEY,
 sgl_dis VARCHAR(10) NOT NULL,
 nme_dis VARCHAR(50) NOT NULL,
 num_ch_dis INT NOT NULL);

 sgl_dis -> Sigla da Disciplina
nme_dis -> Nome da Disciplina
num_ch_dis -> Carga horária da disciplina


'''
#   sgl_dis -> Sigla da Disciplina
# nme_dis -> Nome da Disciplina
# num_ch_dis -> Carga horária da disciplina

def incluir():
  print("Incluir Disciplina")

  print("-------------------------------------------------")
  sigla = input("Digite a sigla da Sigla da Disciplina [XXX]: ")
  nome = input("Nome da Disciplina: ")
  carga_h_d = input("Carga horária da disciplina : ")
  sql = "INSERT INTO tb_dis(sgl_dis, nme_dis, num_ch_dis) VALUES(%s, %s, %s);"
  cursor = cnx.cursor()
  cursor.execute(sql, (sigla, nome, carga_h_d))
  idt = cursor.lastrowid
  print("Criada a Disciplina =", idt)
  cnx.commit()
  cursor.close()
  print("-------------------------------------------------")
  input("[Enter] para menu")


def consultar():
  print("Consultar Disciplina")
  print("-------------------------------------------------")
  cursor = cnx.cursor()
  sql = "SELECT * FROM tb_dis;"
  cursor.execute(sql)
  tab = PrettyTable(["Identificador", "Sigla", "Nome", "Carga horária"])
  for reg in cursor:
      tab.add_row(reg)
  cursor.close()
  print(tab)
  print("-------------------------------------------------")
  input("[Enter] para menu")

def alterar():
  print("Alterar Disciplina")
  print("-------------------------------------------------")
  idt = int(input("Qual o identificador da UF para alterar? "))
  cursor = cnx.cursor()
  sql = "SELECT * FROM tb_dis W" \
        "HERE idt_dis=%s;"
  cursor.execute(sql, [idt])
  dados = cursor.fetchone()
  cursor.close()
  if dados == None:
      print('UF não existe')
  else:
      (idt, sgl, nme, carga ) = dados
      sigla =  input("Digite a nova sigla da UF [" + sgl + "]: ")
      nome = input("Digite o novo nome da UF [" + nme + "]: ")
      carga_h_d = input("Digite o novo Carga horária da disciplina [" + str(carga) + "]: ")
      sql = "UPDATE tb_dis SET sgl_dis=%s, nme_dis=%s , num_ch_dis=%s WHERE idt_dis=%s;"
      cursor = cnx.cursor()
      cursor.execute(sql, (sigla, nome, carga_h_d, idt))
      print("Disciplina alterada!")
      cnx.commit()
      cursor.close()


  print("-------------------------------------------------")
  input("[Enter] para menu")

  # sgl_dis -> SigladaDisciplina idt_dis
  # nme_dis -> Nome da Disciplina tb_dis
  # num_ch_dis -> Carga horária da disciplina carga_h_d
def excluir():
  print("Excluir UF")
  print("-------------------------------------------------")
  idt = int(input("Qual o identificador da UF para excluir? "))
  cursor = cnx.cursor()
  sql = "SELECT * FROM tb_dis WHERE idt_dis=%s;"
  cursor.execute(sql, [idt])
  dados = cursor.fetchone()
  cursor.close()
  if dados == None:
      print('UF não existe')
  else:
      (idt, sgl, nme , carga ) = dados
      print("Identificador:", idt)
      print("Sigla:", sgl)
      print("Nome:", nme)
      print(" Carga horária da disciplina : ", carga )
      exc = input("Deseja realmente excluir [S/N]: ")
      if exc == "S" or exc == 's':
          sql = "DELETE FROM tb_dis WHERE idt_dis=%s;"
          cursor = cnx.cursor()
          cursor.execute(sql, [idt])
          print("UF excluída!")
          cnx.commit()
          cursor.close()

  print("-------------------------------------------------")
  input("[Enter] para menu")
# Menu do CRUD
continuar = True
while continuar:
   # Imprimindo 30 linhas em branco (limpar o console Fake)
   print('\n' * 30)

   print("CRUD de Disciplina")
   print("1 - Incluir")
   print("2 - Consultar")
   print("3 - Alterar")
   print("4 - Excluir")
   print("5 - Sair")
   opcao = int(input("Qual a sua opção? "))

   # Imprimindo 30 linhas em branco (limpar o console Fake)
   print('\n' * 30)
   # Imprimindo 30 linhas em branco (limpar o console Fake)
   print('\n' * 30)
   if opcao == 1: incluir()
   elif opcao == 2: consultar()
   elif opcao == 3: alterar()
   elif opcao == 4: excluir()
   elif opcao == 5:
       print("--- FIM DO CRUD ---")
       continuar = False
       cnx.close()