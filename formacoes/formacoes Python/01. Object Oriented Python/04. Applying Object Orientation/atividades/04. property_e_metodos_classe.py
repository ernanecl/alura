# EXERCICIO 1
print('1. Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.')

class ContaBancaria1:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

pessoa1_conta_bancaria1 = ContaBancaria1('Raissa',200)

print(f'A conta de {pessoa1_conta_bancaria1.titular} esta com status {pessoa1_conta_bancaria1._ativo} e tem saldo de {pessoa1_conta_bancaria1.saldo} bitcoins')

#####################################################################################################################################################################################

# EXERCICIO 2
print('\n2. Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.')

class ContaBancaria2:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'A conta de {self.titular} esta com status {self._ativo} e tem saldo de {self.saldo} bitcoin'
    
pessoa1_conta_bancaria2 = ContaBancaria2('Zahira', 500)
pessoa2_conta_bancaria2 = ContaBancaria2('Aada', 100)

print(pessoa1_conta_bancaria2)
print(pessoa2_conta_bancaria2)

#####################################################################################################################################################################################

# EXERCICIO 3
print('\n3. Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.')

class ContaBancaria3:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'A conta de {self.titular} esta com status {self._ativo} e tem saldo de {self.saldo} bitcoin'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

pessoa1_conta_bancaria3 = ContaBancaria3('Emma',150)
print(pessoa1_conta_bancaria3)

ContaBancaria3.ativar_conta(pessoa1_conta_bancaria3)
print(pessoa1_conta_bancaria3)

#####################################################################################################################################################################################

# EXERCICIO 4
print('\n4. Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.')

class ContaBancaria4:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'A conta de {self.titular} esta com status {self._ativo} e tem saldo de {self.saldo} bitcoin'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo

#####################################################################################################################################################################################

# EXERCICIO 5
print('\n5. Crie uma instância da classe e imprima o valor da propriedade titular.')

class ContaBancaria5:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'A conta de {self.titular} esta com status {self._ativo} e tem saldo de {self.saldo} bitcoin'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo

pessoa1_conta_bancaria5 = ContaBancaria5('Sofia', 450)
print(f'O titular da conta bancaria: {pessoa1_conta_bancaria5.titular}')

#####################################################################################################################################################################################

# EXERCICIO 6
print('\n6. Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.')

class ClienteBanco1:
    def __init__(self, nome, conta, idade, origem, profissao):
        self._nome = nome.title()
        self._conta = conta
        self._idade = idade
        self._origem = origem.title()
        self._profissao = profissao.upper()

conta1_cliente_banco1 = ClienteBanco1('Caitlyn', 87245, 38, 'irlanda', 'biologa')
conta2_cliente_banco1 = ClienteBanco1('Elizabeth', 3901, 35, 'inglaterra', 'investidora')
conta3_cliente_banco1 = ClienteBanco1('Chloe', 65812, 25, 'gracia', 'atleta olimpica')

print(f'{vars(conta1_cliente_banco1)}\n{vars(conta2_cliente_banco1)}\n{vars(conta3_cliente_banco1)}')

# EXERCICIO 7
print('\n7. Crie um método de classe para a conta ClienteBanco.')

class ClienteBanco2:
    def __init__(self, nome, conta, idade, origem, profissao):
        self._nome = nome.title()
        self._conta = conta
        self._idade = idade
        self._origem = origem.upper()
        self._profissao = profissao.upper()

    @classmethod
    def conta(cls, titular, saldo):
        conta = ClienteBanco2(titular, saldo)
        return conta

conta1_cliente_banco2 = ClienteBanco2('Charlotte', 427, 43, 'franca', 'CEO')
conta2_cliente_banco2 = ClienteBanco2('Emily', 98630, 21, 'alemanha', 'duble')

print(f'{vars(conta1_cliente_banco2)}\n{vars(conta2_cliente_banco2)}\n')
