import grpc
from concurrent import futures
import time
import unary_pb2_grpc as pb2_grpc
import unary_pb2 as pb2
import base

products = dict()
products["1"] = pb2.Product(pid=pb2.PID(pid="2332"), name="iphone", price=1200.99, stock=4)
products["2"] = pb2.Product(pid=pb2.PID(pid="6543"), name="arroz", price=20.99, stock=34)
products["3"] = pb2.Product(pid=pb2.PID(pid="575"), name="vectra", price=80000.00, stock=1)

class UnaryService(pb2_grpc.UnaryServicer):

    def __init__(self, *args, **kwargs):
        pass

    def DemandResponse(self, request, context):

        print("Chegou aqui")
        b = [x for x in range(1,8)]
        a = {'a': b}

        return pb2.MessageResponse(**a)

    def DemandProductList(self, request, context):
        print("entrou")
        l = []
        for x in products:
            l.append(products[x])
        p = pb2.ProductList(PL=l)
        return p


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_UnaryServicer_to_server(UnaryService(), server)
    server.add_insecure_port(f'[::]:{base.PORTB}')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
