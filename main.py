# vamos criar uma classe  para cliente da Netflix

class Client():
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_plano = ['basic', "premium"]
        if plano in self.lista_plano:
            self.plano = plano
        else:
            Exception('Plano inválido')

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_plano:
            self.plano = novo_plano
        else:
            print(f'Novo plano inválido, plano atual {self.plano}.')

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Ver filme {filme}.')
        elif self.plano == 'premium':
            print(f'Ver filme {filme}.')
        elif self.plano == 'basic' and plano_filme == 'premium':
            print('Faça upgrade para premium para ver esse filme')
        else:
            print('Plano inválido')


cliente = Client('Rodrigo', 'rodrigo@gmail.com', 'basic')

print(cliente.plano)
cliente.ver_filme('Poderoso Chefão', 'premium')


# No botão upgrade
cliente.mudar_plano('premium')
print(cliente.plano)
cliente.ver_filme('Poderoso Chefão', 'premium')
