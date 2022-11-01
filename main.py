from documentos import Documento
from telefone import TelefoneBr
from datasBr import DatasBr
from acesso_cep import BuscaEndereco

cpf = 17979191056
cnpj = 99023862000105
telefone = "553599074999"
cep = "01001000"

objeto_cpf = Documento.cria_documento(cpf)
objeto_cnpj = Documento.cria_documento(cnpj)
objeto_telefone = TelefoneBr(telefone)
hoje = DatasBr()
objeto_cep = BuscaEndereco(cep)
bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(hoje)
print(objeto_cnpj)
print(objeto_cpf)
print(objeto_telefone)
print(bairro, cidade, uf)
