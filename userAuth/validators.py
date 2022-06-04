from validate_docbr import CPF
from re import findall as fall

def cpf_valido(cpf):
  return CPF().validate(cpf)

def username_valido(username):
  return username.isalpha()

def rg_valido(rg):
  return len(rg) == 9

def tel_valido(tel):
  modelo = '[(][0-9]{2}[)] [0-9]{5}-[0-9]{4}'
  resposta =fall(modelo, tel)
  return resposta
  
def senha_valida(password, password_confirm):
  return password == password_confirm
   