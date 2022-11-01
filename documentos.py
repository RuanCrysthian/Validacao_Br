from validate_docbr import CPF, CNPJ

# Factory que cria objetos passando o tamanho da string
# Exemplos: CPF tem 11 dígitos
class Documento:

    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        if (len(documento) == 11):
            return DocCpf(documento)
        elif(len(documento) == 14):
            return DocCnpj(documento)
        else:
            raise ValueError("QUANTIDADE DE DÍGITOS INVÁLIDA!")

class DocCpf:

    def __init__(self, documento):
        if(self.valida(documento)):
            self.cpf = documento
        else:
            raise ValueError("CPF INVÁLIDO!")

    def __str__(self):
        return self.formata_cpf()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def formata_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCnpj:

    def __init__(self, documento):
        if(self.valida(documento)):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ INVÁLIDO!")

    def __str__(self):
        return self.formata_cnpj()

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def formata_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
