# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import currencies_pb2 as currencies__pb2


class CurrenciesServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Health = channel.unary_unary(
        '/currencies.CurrenciesService/Health',
        request_serializer=currencies__pb2.Empty.SerializeToString,
        response_deserializer=currencies__pb2.Empty.FromString,
        )
    self.Get = channel.unary_unary(
        '/currencies.CurrenciesService/Get',
        request_serializer=currencies__pb2.CurrenciesRequest.SerializeToString,
        response_deserializer=currencies__pb2.CurrenciesResponse.FromString,
        )


class CurrenciesServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Health(self, request, context):
    """Health is empty method for checking service started
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get(self, request, context):
    """Get returns list of currencies with current exchange rates and pledge coefficients
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CurrenciesServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Health': grpc.unary_unary_rpc_method_handler(
          servicer.Health,
          request_deserializer=currencies__pb2.Empty.FromString,
          response_serializer=currencies__pb2.Empty.SerializeToString,
      ),
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=currencies__pb2.CurrenciesRequest.FromString,
          response_serializer=currencies__pb2.CurrenciesResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'currencies.CurrenciesService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
