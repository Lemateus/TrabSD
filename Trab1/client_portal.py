import grpc
from concurrent import futures
import time
import unary_pb2_grpc as pb2_grpc
import unary_pb2 as pb2
import base
import json
from threading import Thread
from google.protobuf.json_format import MessageToJson
from paho.mqtt import client as mqtt_client
import random
import time

class Data():
    def __init__(self) -> None:
        self.ordersClient = dict()
        self.clientsBD = []
        self.clientsBD.append("12345")
        self.clientsBD.append("45678")
        self.ordersBD = dict()
        self.productsBD = dict()
        self.productsBD["456"] = {'CB':"456", 'name':"iphone", 'price':1200.99, 'stock':4}
        self.productsBD["789"] = {'CB':"789", 'name':"arroz", 'price':20.99, 'stock':34}
        self.productsBD["123"] = {'CB':"123", 'name':"vectra", 'price':80000.00, 'stock':1}
    
    def insertOrderClient(self, cid, oid):
        if cid not in self.ordersClient:
            self.ordersClient[cid] = {'orders':[oid]}
        else:
            self.ordersClient[cid]['orders'].append(oid)


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
        l = []
        for x in D.productsBD:
            l.append(D.productsBD[x])
        p = pb2.ProductList(PL=l)
        return p

class UnaryService(pb2_grpc.UnaryServicer):

    def __init__(self, *args, **kwargs):
        pass

    def DemandResponse(self, request, context):

        print("Chegou aqui")
        b = [x for x in range(1,8)]
        a = {'a': b}

        return pb2.MessageResponse(**a)

    def DemandOrderList(self, request, context):
        cid = request.cid
        result = []

        if cid not in D.clientsBD:
            result.append("-1")
        elif cid not in D.ordersClient:
            result.append("-2")
        else:
            result = D.ordersClient[cid]['orders']
        
        p = pb2.OrderList(orList=result)
        print("aqui")
        return p
    
    def DemandProductList(self, request, context):
        print("client_portal - DemandProductList")
        l = []
        for x in D.productsBD:
            l.append(D.productsBD[x])
        p = pb2.ProductList(PL=l)
        return p

    def DemandOrderInsertion(self, request, context):
        print("it got here")
        oid = str(len(D.ordersBD)+1)
        validOrder = True

        if request.cid not in D.clientsBD:
            validOrder = False
            return pb2.OID(oid="-2")

        for x in request.products:
            print(f"x.qtd = {x.qtd}")
            if x.pid not in D.productsBD:
                validOrder = False
                break
            elif D.productsBD[x.pid]['stock'] < x.qtd:
                validOrder = False
                break
        
        if validOrder == False:
            return pb2.OID(oid="-1") # Falha no pedido
        
        for x in request.products:
            D.productsBD[x.pid]['stock'] -= x.qtd
        
        D.insertOrderClient(request.cid, oid)
        print(f"ordersClient: {D.ordersClient}")
        D.ordersBD[oid] = {'cid':request.cid, 'products':request.products}
        print(f"ordersBD: {D.ordersBD}")
        return pb2.OID(oid=oid)

    def DemandOrderModification(self, request, context):
        oid = request.oid
        print(f'Prim -> {D.ordersBD[oid]["products"]}')
        for x in D.ordersBD[oid]['products']:
            qtd = x.qtd
            print(f'qtd: {qtd}')
            pid = x.pid
            print(f'D.productsBD[pid]["stock"]: {D.productsBD[pid]["stock"]}')
            D.productsBD[pid]['stock'] += qtd
        
        possible = True
        for x in request.products:
            qtd = x.qtd
            pid = x.pid
            if D.productsBD[pid]['stock'] < qtd:
                possible = False
                break

        if not possible:
            for x in D.ordersBD[oid]['products']:
                qtd = x.qtd
                pid = x.pid
                D.productsBD[pid]['stock'] -= qtd

            return pb2.Confirmation(b=False)
        
        for x in request.products:
            qtd = x.qtd
            pid = x.pid
            D.productsBD[pid]['stock'] -= qtd

        D.ordersBD[oid]['products'] = request.products
        print(f'Seg -> {D.ordersBD[oid]["products"]}')

        # print(f'products[0]: {products[0].pid}')
        return pb2.Confirmation(b=True)

    def DemandOrderInformation(self, request, context):
        cid = request.cid
        oid = request.oid
        print(f'D.clientsBD = {D.clientsBD}')
        print(f'D.ordersClient[cid] = {D.ordersClient[cid]}')
        if cid not in D.clientsBD or oid not in D.ordersClient[cid]['orders']:
            return pb2.Order(cid="-1", products=[])

        return pb2.Order(cid=cid, products=D.ordersBD[oid]["products"])

    def DemandOrderPrice(self, request, context):
        oid = request.oid
        order = D.ordersBD[oid]["products"]
        price = 0
        for x in order:
            qtd = x.qtd
            pid = x.pid
            pr = D.productsBD[pid]['price']
            price += (pr*qtd)

        return pb2.Price(price=price)

    def DemandOrderCancelation(self, request, context):
        cid = request.cid
        oid = request.oid

        # print(f'-> {D.ordersClient[oid]}')
        # print(f'oid: {oid}')
        if oid not in D.ordersBD:
            return pb2.Confirmation(b=False)
        del D.ordersBD[oid]

        if cid not in D.ordersClient:
            return pb2.Confirmation(b=False)
        D.ordersClient[cid]['orders'].remove(oid)
        # print(f'--> {D.ordersClient[cid]}')

        return pb2.Confirmation(b=True)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_UnaryServicer_to_server(UnaryService(), server)
    server.add_insecure_port(f'[::]:{base.PORTB}')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    D = Data()

    serve()
    client = UnaryClient()
    result = client.getProductList(cid="Hello Server you there?")
    print(f'{result}')