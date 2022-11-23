import grpc
import unary_pb2_grpc as pb2_grpc
import unary_pb2 as pb2
import base

class UnaryClient(object):

    def __init__(self, port):
        self.host = 'localhost'
        self.server_port = port

        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        self.stub = pb2_grpc.UnaryStub(self.channel)

    def getProductList(self, cid):
        cid = pb2.CID(cid=cid)
        print(cid)
        return self.stub.DemandProductList(cid)

    def addClient(self, client):
        return self.stub.DemandClientInsertion(client)

    def alterClient(self, client):
        return self.stub.DemandClientModification(client)

    def searchClient(self, cid):
        cid = pb2.CID(cid=cid)
        return self.stub.DemandClientSearch(cid)

    def removeClient(self, cid):
        cid = pb2.CID(cid=cid)
        return self.stub.DemandClientRemoval(cid)
    
    def addProduct(self, product):
        print(f"em cima: {product}")
        return self.stub.DemandProductInsertion(product)

    def alterProduct(self, product):
        return self.stub.DemandProductModification(product)

    def searchProduct(self, pid):
        pid = pb2.PID(pid=pid)
        return self.stub.DemandProductSearch(pid)

    def removeProduct(self, pid):
        pid = pb2.PID(pid=pid)
        return self.stub.DemandProductRemoval(pid)

def ClientData():
    print("Informe os dados do Cleinte:")
    name = input("Nome: ")
    surname = input("Sobrenome: ")
    cpf = input("CPF: ")
    return pb2.Client(name=name, surname=surname, cpf=cpf)

def ProductData():
    print("Informe os dados do Produto:")
    name = input("Nome: ")
    pid = input("Código de Barras: ")
    price = float(input("Preço: "))
    stock = int(input("Quantidade em estoque: "))
    pr = pb2.Product(CB=pid, name=name, price=price, stock=stock)
    print(pr)
    return pr

def ClientAlter():
    cpf = input("CPF do cliente a ser modificado: ")
    name = input("Novo nome: ")
    surname = input("Novo Sobrenome: ")
    return pb2.Client(name=name, surname=surname, cpf=cpf)

def ProductAlter():
    cb = input("Código de Barras do produto a ser modificado: ")
    name = input("Novo nome: ")
    price = float(input("Novo preço: "))
    stock = int(input("Nova quantidade em estoque: "))
    return pb2.Product(CB=cb, name=name, price=price, stock=stock)


if __name__ == '__main__':

    while True:
        base.showMenuAdm()
        chosen = int(input("\nDigite o número de sua escolha: "))

        # Criar Cliente
        if chosen == 1:
            client = ClientData()
            c = UnaryClient(base.PORTA)
            result = c.addClient(client)
            if(result.b): print("Inserção bem sucedida!")
            else: print("Falha na inserção!")
        
        elif chosen == 2:
            client = ClientAlter()
            c = UnaryClient(base.PORTA)
            result = c.alterClient(client)
            if(result.b): print("Modificação bem sucedida!")
            else: print("Cliente Inexistente!")

        elif chosen == 3:
            cid = input("Digite CPF do cliente desejado: ")
            c = UnaryClient(base.PORTA)
            result = c.searchClient(cid)
            if(result.b): print("Cliente econtrado!")
            else: print("Cliente não encontrado!")

        elif chosen == 4:
            cid = input("Digite CPF do cliente a ser removido: ")
            c = UnaryClient(base.PORTA)
            result = c.removeClient(cid)
            if(result.b): print("Cliente removido!")
            else: print("Cliente não encontrado!")

        elif chosen == 5:
            product = ProductData()
            print(f"product: {product}")
            c = UnaryClient(base.PORTA)
            result = c.addProduct(product)
            if(result.b): print("Inserção bem sucedida!")
            else: print("Falha na inserção!")

        elif chosen == 6:
            product = ProductAlter()
            c = UnaryClient(base.PORTA)
            result = c.alterProduct(product)
            if(result.b): print("Modificação bem sucedida!")
            else: print("Produto Inexistente!")
        
        elif chosen == 7:
            pid = input("Digite Código de Barras do produto desejado: ")
            c = UnaryClient(base.PORTA)
            result = c.searchProduct(pid)
            if(result.b): print("Produto econtrado!")
            else: print("Produto não encontrado!")

        elif chosen == 8:
            pid = input("Digite Código de Barras do produto a ser removido: ")
            c = UnaryClient(base.PORTA)
            result = c.removeProduct(pid)
            if(result.b): print("Produto removido!")
            else: print("Produto não encontrado!")

        elif chosen == 9:
            break


    # client = UnaryClient(base.PORTA)
    # result = client.getProductList(cid="mateus")
    # print(f'{result}')
