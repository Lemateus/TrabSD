import grpc
import pandas as pd
from concurrent import futures
import time
import unary_pb2_grpc as pb2_grpc
import unary_pb2 as pb2
import hashlib
from concurrent import futures
from collections import deque


PORTA = 4567
PORTB = 4568
PORTC = 4569
PORTD = 4570

def showMenuAdm():
    print("\nMenu:")
    print("1 - Inserir Cliente")
    print("2 - Modificar Cliente")
    print("3 - Recuperar Cliente")
    print("4 - Remover Cliente")
    print("5 - Inserir Produto")
    print("6 - Modificar Produto")
    print("7 - Recuperar Produto")
    print("8 - Remover Produto")
    print("9 - Fechar Menu")

def showMenuClient():
    print("\nMenu")
    print("1 - Inserir Pedido")
    print("2 - Modificar Pedido")
    print("3 - Enumerar Pedido")
    print("4 - Enumerar Pedidos")
    print("5 - Cancelar Pedido")

def showProductsTable(lista):
    l = []
    for x in lista.PL:
        l.append(pd.Series({'Nome': x.name, 'Preço':x.price, 'Estoque':x.stock, 'CB':x.CB}))
    df = pd.DataFrame(l)
    if(l.__len__==0): print("Não há produtos cadastrados!")
    else:
        print("\t\tProdutos Disponíveis:")
        print(df)
    print("\n")
    

class Cache():
    def __init__(self) -> None:
        self.cache = deque(maxlen=3)

    def inCache(self, aux):
        if aux in self.cache:
            return True
        else:
            return False
    
    def Insertion(self, aux):
        if self.inCache(aux):
            self.cache.remove(aux)
        self.cache.append(aux)

    def ClientRemoval(self, cid):
        for x in self.cache:
            if x.cpf == cid:
                self.cache.remove(x)
                break

    def ProdutcRemoval(self, pid):
        for x in self.cache:
            if x.CB == pid:
                self.cache.remove(x)
                break


# c = Cache()
# c.Insertion(pb2.Client(name="Mateus", surname="Lemos", cpf="12345"))
# c.Insertion(pb2.Client(name="casa", surname="rtyu", cpf="4565"))
# c.Insertion(pb2.Client(name="hj", surname="ole", cpf="147"))
# print(c.cache)
# print("\n\n")
# # for x in c.cache:
# #     if(x.cpf=="4565"):
# #         print(x)
# c.Removal("12345")
# print(c.cache)