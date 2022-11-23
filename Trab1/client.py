import grpc
import unary_pb2_grpc as pb2_grpc
import unary_pb2 as pb2
import base

class UnaryClient(object):

    def __init__(self, port):
        self.host = 'localhost'
        self.server_port = port

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.UnaryStub(self.channel)

    def getProductList(self, cid):
        cid = pb2.CID(cid=cid)
        print(cid)
        return self.stub.DemandProductList(cid)
    
    def addOrder(self, pedido):
        return self.stub.DemandOrderInsertion(pedido)

    def alterOrder(self, alteration):
        return self.stub.DemandOrderModification(alteration)

    def getOrderList(self, cid):
        cid = pb2.CID(cid=cid)
        return self.stub.DemandOrderList(cid)

    def getInformationOID(self, cid, oid):
        s = pb2.CID_OID(cid=cid, oid=oid)
        return self.stub.DemandOrderInformation(s)

    def getPrice(self, oid):
        oid = pb2.OID(oid=oid)
        return self.stub.DemandOrderPrice(oid)

    def cancelOrder(self, cid, oid):
        s = pb2.CID_OID(cid=cid, oid=oid)
        return self.stub.DemandOrderCancelation(s)

def OrderData(cid):
    print("Informe os dados do Pedido:\n")
    num = int(input("Numero de produtos diferentes que deseja: "))
    l = []
    for _ in range(num):
        pid = input("Código de Barras do produto desejado: ")
        qtd = int(input("Quantidade: "))
        l.append(pb2.IndOrder(pid=pid, qtd=qtd))
    return pb2.Order(cid=cid, products=l)

def ModOrderData(cid, oid):
    c = UnaryClient(base.PORTB)
    lista = c.getProductList(cid)
    base.showProductsTable(lista)


    print("Informe os dados do Pedido:\n")
    num = int(input("Numero de produtos diferentes que deseja: "))
    l = []
    for _ in range(num):
        pid = input("Código de Barras do produto desejado: ")
        qtd = int(input("Quantidade: "))
        l.append(pb2.IndOrder(pid=pid, qtd=qtd))
    return pb2.ModOrder(cid=cid, oid=oid, products=l)

class Data():

    def __init__(self):
        self.myOrders = []
        self.clientsBD = []
    
    def InsertOrder(self, oid):
        oid = oid.oid
        if oid not in self.myOrders:
            self.myOrders.append(oid)

    def InsertClients(self, cid):
        cid = cid.cid
        if cid not in self.clientsBD:
            self.clientsBD.append(cid)


if __name__ == '__main__':
    D = Data()

    while True:
        base.showMenuClient()
        chosen = int(input("\nDigite o número de sua escolha: "))

        if chosen == 1:
            cid = input("Digite seu CPF: ")
            c = UnaryClient(base.PORTB)
            lista = c.getProductList(cid)
            base.showProductsTable(lista)

            pedido = OrderData(cid)
            print("\n")
            print(pedido)
            d = UnaryClient(base.PORTB)
            print("aqui tbm")
            oid = d.addOrder(pedido)
            if(oid.oid=="-2"):
                print("CPF não cadastrado!")
            elif(oid.oid=="-1"):
                print("Pedido Inválido!")
            else:
                print("Pedido cadastrado com sucesso!")
                D.InsertOrder(oid)

        elif chosen == 2:
            cid = input("Digite seu CPF: ")
            c = UnaryClient(base.PORTB)
            aux = c.getOrderList(cid)
            
            l = []
            for x in aux.orList:
                l.append(x)
            if(len(l)==0):
                print("Não há pedidos!")
                continue

            if(l[0]=='-1'):
                print("CPF não cadastrado!")
                continue
            if(l[0]=='-2'):
                print("Não há pedidos para esse CPF!")
                continue

            print(f"Pedidos: {l}")
            oid = input("Digite o código do pedido que deseja modificar: ")
            if oid not in l:
                print("Código inválido")
                continue

            p = ModOrderData(cid, oid)
            print(p)
            result = c.alterOrder(p)
            if result.b:
                print("Alteração concluída com sucesso!")
            else:
                print("ALteração inválida!")
        
        elif chosen == 3:
            cid = input("Digite seu CPF: ")
            c = UnaryClient(base.PORTB)
            l = c.getOrderList(cid).orList

            print(f"Pedidos relacionados a esse CPF: {l}")
            oid = input("Deseja informações de qual pedido: ")
            result = c.getInformationOID(cid, oid)
            if(result.cid=="-1"):
                print("Pedido e/ou cliente inválido(s)!")
                continue

            print("Informações do pedido: ")
            for x in result.products:
                print(f'PID: {x.pid}, quantidade: {x.qtd}')

            price = c.getPrice(oid)
            print(f"Preço Total: {price}")

        elif chosen == 4:
            cid = input("Digite seu CPF: ")
            c = UnaryClient(base.PORTB)
            l = c.getOrderList(cid).orList
            
            if l[0]=="-1" or l[0]=="-2":
                print("CID inválido!")
                continue
            
            print("\nPedidos desse cliente: ")
            for x in l:
                print(f"OID: {x}, preço: {c.getPrice(x)}")

        elif chosen == 5:
            cid = input("Digite seu CPF: ")
            c = UnaryClient(base.PORTB)
            l = c.getOrderList(cid).orList
            if len(l)==0:
                print("Não há pedidos para esse CPF!")
                continue

            print(f"Pedidos relacionados a esse CPF: {l}")
            oid = input("Deseja cancelar qual pedido: ")

            result = c.cancelOrder(cid, oid)
            if(result.b):
                print("Pedido removido com sucesso!")
            else:
                print("Pedido inexistente!")


            

    # client = UnaryClient(base.PORTA)
    # result = client.getProductList(cid="mateus")
    # print(f'{result}')
