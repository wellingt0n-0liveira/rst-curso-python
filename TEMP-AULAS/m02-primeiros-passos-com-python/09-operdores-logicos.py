# Operadores Lógicos
'''
##Validaom mais de uma condição
* AND = Se todas as condições forem verdadeiras
* OR = se uma ou outra condição for verdadeira
* NOT = Ao contrário da condição
'''
# Tabela Verdade
'''
AND
| A | B | A AND B|
|---|---|--------|
| V | V |    V   |
| V | F |    F   |
| F | V |    F   |
| V | F |    F   |

OR
| A | B | A OR B |
|---|---|--------|
| V | V |    V   |
| V | F |    V   |
| F | V |    V   |
| V | F |    F   |

NOT
| B |  NOT A |
|---|--------|
| V |    V   |
| F |    F   |
| V |    F   |
| F |    F   |

'''
pedido_1 = 100.00
pedido_2 = 150.00
pedido_1_pago = True
pedido_1_pago_cartao = True
pedido_2_pago = True
pedido_2_pago_cartao = True

print('-'*50)
print('Pedido 1 - Precisa levar maquin ade cartão?',not pedido_1_pago and pedido_1_pago_cartao)
print('De todos os pedidos algum é com cartão?', pedido_1_pago_cartao or pedido_2_pago_cartao)
print('Motoboy precisa levar máuina?', (not pedido_1_pago or not pedido_2_pago) and (pedido_1_pago_cartao or pedido_2_pago_cartao))
