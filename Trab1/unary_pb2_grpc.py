# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import unary_pb2 as unary__pb2


class UnaryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DemandResponse = channel.unary_unary(
                '/unary.Unary/DemandResponse',
                request_serializer=unary__pb2.Message.SerializeToString,
                response_deserializer=unary__pb2.MessageResponse.FromString,
                )
        self.DemandClientInsertion = channel.unary_unary(
                '/unary.Unary/DemandClientInsertion',
                request_serializer=unary__pb2.Client.SerializeToString,
                response_deserializer=unary__pb2.Confirmation.FromString,
                )
        self.DemandClientModification = channel.unary_unary(
                '/unary.Unary/DemandClientModification',
                request_serializer=unary__pb2.Client.SerializeToString,
                response_deserializer=unary__pb2.Confirmation.FromString,
                )
        self.DemandClientSearch = channel.unary_unary(
                '/unary.Unary/DemandClientSearch',
                request_serializer=unary__pb2.CID.SerializeToString,
                response_deserializer=unary__pb2.Confirmation.FromString,
                )
        self.DemandClientRemoval = channel.unary_unary(
                '/unary.Unary/DemandClientRemoval',
                request_serializer=unary__pb2.CID.SerializeToString,
                response_deserializer=unary__pb2.Confirmation.FromString,
                )
        self.DemandProductInsertion = channel.unary_unary(
                '/unary.Unary/DemandProductInsertion',
                request_serializer=unary__pb2.Product.SerializeToString,
                response_deserializer=unary__pb2.Confirmation.FromString,
                )
        self.DemandProductModification = channel.unary_unary(
                '/unary.Unary/DemandProductModification',
                request_serializer=unary__pb2.Product.SerializeToString,
                response_deserializer=unary__pb2.Confirmation.FromString,
                )
        self.DemandProductSearch = channel.unary_unary(
                '/unary.Unary/DemandProductSearch',
                request_serializer=unary__pb2.PID.SerializeToString,
                response_deserializer=unary__pb2.Confirmation.FromString,
                )
        self.DemandProductRemoval = channel.unary_unary(
                '/unary.Unary/DemandProductRemoval',
                request_serializer=unary__pb2.PID.SerializeToString,
                response_deserializer=unary__pb2.Confirmation.FromString,
                )
        self.DemandProductList = channel.unary_unary(
                '/unary.Unary/DemandProductList',
                request_serializer=unary__pb2.CID.SerializeToString,
                response_deserializer=unary__pb2.ProductList.FromString,
                )
        self.DemandOrderInsertion = channel.unary_unary(
                '/unary.Unary/DemandOrderInsertion',
                request_serializer=unary__pb2.Order.SerializeToString,
                response_deserializer=unary__pb2.OID.FromString,
                )
        self.DemandOrderModification = channel.unary_unary(
                '/unary.Unary/DemandOrderModification',
                request_serializer=unary__pb2.ModOrder.SerializeToString,
                response_deserializer=unary__pb2.Confirmation.FromString,
                )
        self.DemandOrderList = channel.unary_unary(
                '/unary.Unary/DemandOrderList',
                request_serializer=unary__pb2.CID.SerializeToString,
                response_deserializer=unary__pb2.OrderList.FromString,
                )
        self.DemandOrderInformation = channel.unary_unary(
                '/unary.Unary/DemandOrderInformation',
                request_serializer=unary__pb2.CID_OID.SerializeToString,
                response_deserializer=unary__pb2.Order.FromString,
                )
        self.DemandOrderPrice = channel.unary_unary(
                '/unary.Unary/DemandOrderPrice',
                request_serializer=unary__pb2.OID.SerializeToString,
                response_deserializer=unary__pb2.Price.FromString,
                )
        self.DemandOrderCancelation = channel.unary_unary(
                '/unary.Unary/DemandOrderCancelation',
                request_serializer=unary__pb2.CID_OID.SerializeToString,
                response_deserializer=unary__pb2.Confirmation.FromString,
                )


class UnaryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def DemandResponse(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DemandClientInsertion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DemandClientModification(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DemandClientSearch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DemandClientRemoval(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DemandProductInsertion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DemandProductModification(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DemandProductSearch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DemandProductRemoval(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DemandProductList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DemandOrderInsertion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DemandOrderModification(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DemandOrderList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DemandOrderInformation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DemandOrderPrice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DemandOrderCancelation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UnaryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DemandResponse': grpc.unary_unary_rpc_method_handler(
                    servicer.DemandResponse,
                    request_deserializer=unary__pb2.Message.FromString,
                    response_serializer=unary__pb2.MessageResponse.SerializeToString,
            ),
            'DemandClientInsertion': grpc.unary_unary_rpc_method_handler(
                    servicer.DemandClientInsertion,
                    request_deserializer=unary__pb2.Client.FromString,
                    response_serializer=unary__pb2.Confirmation.SerializeToString,
            ),
            'DemandClientModification': grpc.unary_unary_rpc_method_handler(
                    servicer.DemandClientModification,
                    request_deserializer=unary__pb2.Client.FromString,
                    response_serializer=unary__pb2.Confirmation.SerializeToString,
            ),
            'DemandClientSearch': grpc.unary_unary_rpc_method_handler(
                    servicer.DemandClientSearch,
                    request_deserializer=unary__pb2.CID.FromString,
                    response_serializer=unary__pb2.Confirmation.SerializeToString,
            ),
            'DemandClientRemoval': grpc.unary_unary_rpc_method_handler(
                    servicer.DemandClientRemoval,
                    request_deserializer=unary__pb2.CID.FromString,
                    response_serializer=unary__pb2.Confirmation.SerializeToString,
            ),
            'DemandProductInsertion': grpc.unary_unary_rpc_method_handler(
                    servicer.DemandProductInsertion,
                    request_deserializer=unary__pb2.Product.FromString,
                    response_serializer=unary__pb2.Confirmation.SerializeToString,
            ),
            'DemandProductModification': grpc.unary_unary_rpc_method_handler(
                    servicer.DemandProductModification,
                    request_deserializer=unary__pb2.Product.FromString,
                    response_serializer=unary__pb2.Confirmation.SerializeToString,
            ),
            'DemandProductSearch': grpc.unary_unary_rpc_method_handler(
                    servicer.DemandProductSearch,
                    request_deserializer=unary__pb2.PID.FromString,
                    response_serializer=unary__pb2.Confirmation.SerializeToString,
            ),
            'DemandProductRemoval': grpc.unary_unary_rpc_method_handler(
                    servicer.DemandProductRemoval,
                    request_deserializer=unary__pb2.PID.FromString,
                    response_serializer=unary__pb2.Confirmation.SerializeToString,
            ),
            'DemandProductList': grpc.unary_unary_rpc_method_handler(
                    servicer.DemandProductList,
                    request_deserializer=unary__pb2.CID.FromString,
                    response_serializer=unary__pb2.ProductList.SerializeToString,
            ),
            'DemandOrderInsertion': grpc.unary_unary_rpc_method_handler(
                    servicer.DemandOrderInsertion,
                    request_deserializer=unary__pb2.Order.FromString,
                    response_serializer=unary__pb2.OID.SerializeToString,
            ),
            'DemandOrderModification': grpc.unary_unary_rpc_method_handler(
                    servicer.DemandOrderModification,
                    request_deserializer=unary__pb2.ModOrder.FromString,
                    response_serializer=unary__pb2.Confirmation.SerializeToString,
            ),
            'DemandOrderList': grpc.unary_unary_rpc_method_handler(
                    servicer.DemandOrderList,
                    request_deserializer=unary__pb2.CID.FromString,
                    response_serializer=unary__pb2.OrderList.SerializeToString,
            ),
            'DemandOrderInformation': grpc.unary_unary_rpc_method_handler(
                    servicer.DemandOrderInformation,
                    request_deserializer=unary__pb2.CID_OID.FromString,
                    response_serializer=unary__pb2.Order.SerializeToString,
            ),
            'DemandOrderPrice': grpc.unary_unary_rpc_method_handler(
                    servicer.DemandOrderPrice,
                    request_deserializer=unary__pb2.OID.FromString,
                    response_serializer=unary__pb2.Price.SerializeToString,
            ),
            'DemandOrderCancelation': grpc.unary_unary_rpc_method_handler(
                    servicer.DemandOrderCancelation,
                    request_deserializer=unary__pb2.CID_OID.FromString,
                    response_serializer=unary__pb2.Confirmation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'unary.Unary', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Unary(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def DemandResponse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.Unary/DemandResponse',
            unary__pb2.Message.SerializeToString,
            unary__pb2.MessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DemandClientInsertion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.Unary/DemandClientInsertion',
            unary__pb2.Client.SerializeToString,
            unary__pb2.Confirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DemandClientModification(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.Unary/DemandClientModification',
            unary__pb2.Client.SerializeToString,
            unary__pb2.Confirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DemandClientSearch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.Unary/DemandClientSearch',
            unary__pb2.CID.SerializeToString,
            unary__pb2.Confirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DemandClientRemoval(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.Unary/DemandClientRemoval',
            unary__pb2.CID.SerializeToString,
            unary__pb2.Confirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DemandProductInsertion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.Unary/DemandProductInsertion',
            unary__pb2.Product.SerializeToString,
            unary__pb2.Confirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DemandProductModification(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.Unary/DemandProductModification',
            unary__pb2.Product.SerializeToString,
            unary__pb2.Confirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DemandProductSearch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.Unary/DemandProductSearch',
            unary__pb2.PID.SerializeToString,
            unary__pb2.Confirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DemandProductRemoval(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.Unary/DemandProductRemoval',
            unary__pb2.PID.SerializeToString,
            unary__pb2.Confirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DemandProductList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.Unary/DemandProductList',
            unary__pb2.CID.SerializeToString,
            unary__pb2.ProductList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DemandOrderInsertion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.Unary/DemandOrderInsertion',
            unary__pb2.Order.SerializeToString,
            unary__pb2.OID.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DemandOrderModification(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.Unary/DemandOrderModification',
            unary__pb2.ModOrder.SerializeToString,
            unary__pb2.Confirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DemandOrderList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.Unary/DemandOrderList',
            unary__pb2.CID.SerializeToString,
            unary__pb2.OrderList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DemandOrderInformation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.Unary/DemandOrderInformation',
            unary__pb2.CID_OID.SerializeToString,
            unary__pb2.Order.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DemandOrderPrice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.Unary/DemandOrderPrice',
            unary__pb2.OID.SerializeToString,
            unary__pb2.Price.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DemandOrderCancelation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.Unary/DemandOrderCancelation',
            unary__pb2.CID_OID.SerializeToString,
            unary__pb2.Confirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
