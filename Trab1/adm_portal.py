import grpc
from concurrent import futures
import time
import unary_pb2_grpc as pb2_grpc
import unary_pb2 as pb2
import base

clientsBD = dict()
productsBD = dict()
clientsCache = base.Cache()
productsCache = base.Cache()

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
        print("funcao de cima")
        print(cid)
        return self.stub.DemandProductList(cid)

class UnaryService(pb2_grpc.UnaryServicer):

    def __init__(self, *args, **kwargs):
        pass

    def DemandResponse(self, request, context):

        print("Chegou aqui")
        b = [x for x in range(1,8)]
        a = {'a': b}

        return pb2.MessageResponse(**a)
    
    def DemandProductList(self, request, context):
        print("client_portal - DemandProductList")
        cid = request.cid
        client_portal_as_client = UnaryClient(base.PORTB)
        print(cid)
        result = client_portal_as_client.getProductList(request)
        return result

    def DemandClientInsertion(self, request, context):
        cid = request.cpf
        result = 0
        if(cid in clientsBD):
            result = pb2.Confirmation(b=False)
        else:
            clientsBD[cid] = {'name': request.name, 'surname':request.surname, 'cpf':request.cpf}
            print(clientsBD)
            result = pb2.Confirmation(b=True)
            clientsCache.Insertion(request)
            print(clientsCache.cache)
        return result
    
    def DemandClientModification(self, request, context):
        cid = request.cpf
        result = 0
        if(cid in clientsBD):
            clientsBD[cid]['name'] = request.name
            clientsBD[cid]['surname'] = request.surname
            result = pb2.Confirmation(b=True)
            clientsCache.Insertion(request)
            print(clientsBD)
        else:
            result = pb2.Confirmation(b=False)
        return result

    def DemandClientSearch(self, request, context):
        cid = request.cid
        found = False
        for x in clientsCache.cache:
            if x.cpf == cid:
                found = True
        if not found and cid in clientsBD:
            found = True
            clientsCache.Insertion(clientsBD[cid])
        return pb2.Confirmation(b=found)

    def DemandClientRemoval(self, request, context):
        cid = request.cid
        found = False
        if cid in clientsBD:
            del clientsBD[cid]
            clientsCache.ClientRemoval(cid)
            found = True
        return pb2.Confirmation(b=found)

    def DemandProductInsertion(self, request, context):
        print("passou aqui")
        print(f'em portal: {request}')
        pid = request.CB
        print(f'pid = {pid}')

        result = 0
        if(pid in productsBD):
            result = pb2.Confirmation(b=False)
        else:
            productsBD[pid] = {'CB':request.CB, 'name':request.name, 'price':request.price, 'stock':request.stock}
            print(productsBD)
            result = pb2.Confirmation(b=True)
            productsCache.Insertion(request)
            print(productsCache.cache)
        return result

    def DemandProductModification(self, request, context):
        pid = request.CB
        result = 0
        if(pid in productsBD):
            productsBD[pid]['name'] = request.name
            productsBD[pid]['price'] = request.price
            productsBD[pid]['stock'] = request.stock
            result = pb2.Confirmation(b=True)
            productsCache.Insertion(request)
            print(productsBD)
        else:
            result = pb2.Confirmation(b=False)
        return result

    def DemandProductSearch(self, request, context):
        pid = request.pid
        found = False
        for x in productsCache.cache:
            if x.CB == pid:
                found = True
        if not found and pid in productsBD:
            found = True
            clientsCache.Insertion(productsBD[pid])
        return pb2.Confirmation(b=found)

    def DemandProductRemoval(self, request, context):
        pid = request.pid
        found = False
        print("entrou nesse bem aqui")
        if pid in productsBD:
            del productsBD[pid]
            productsCache.ProdutcRemoval(pid)
            found = True
        return pb2.Confirmation(b=found)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_UnaryServicer_to_server(UnaryService(), server)
    server.add_insecure_port(f'[::]:{base.PORTA}')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
    client = UnaryClient()
    result = client.getProductList(cid="Hello Server you there?")
    print(f'{result}')