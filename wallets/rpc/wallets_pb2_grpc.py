# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import wallets_pb2 as wallets__pb2


class WalletsStub(object):
  """WalletsService server
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Healthz = channel.unary_unary(
        '/wallets.Wallets/Healthz',
        request_serializer=wallets__pb2.HealthzRequest.SerializeToString,
        response_deserializer=wallets__pb2.HealthzResponse.FromString,
        )
    self.GetWallet = channel.unary_unary(
        '/wallets.Wallets/GetWallet',
        request_serializer=wallets__pb2.WalletRequest.SerializeToString,
        response_deserializer=wallets__pb2.WalletResponse.FromString,
        )
    self.StartMonitoring = channel.unary_unary(
        '/wallets.Wallets/StartMonitoring',
        request_serializer=wallets__pb2.MonitoringRequest.SerializeToString,
        response_deserializer=wallets__pb2.MonitoringResponse.FromString,
        )
    self.StopMonitoring = channel.unary_unary(
        '/wallets.Wallets/StopMonitoring',
        request_serializer=wallets__pb2.MonitoringRequest.SerializeToString,
        response_deserializer=wallets__pb2.MonitoringResponse.FromString,
        )
    self.CheckBalance = channel.unary_unary(
        '/wallets.Wallets/CheckBalance',
        request_serializer=wallets__pb2.CheckBalanceRequest.SerializeToString,
        response_deserializer=wallets__pb2.CheckBalanceResponse.FromString,
        )


class WalletsServicer(object):
  """WalletsService server
  """

  def Healthz(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetWallet(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartMonitoring(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StopMonitoring(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CheckBalance(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_WalletsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Healthz': grpc.unary_unary_rpc_method_handler(
          servicer.Healthz,
          request_deserializer=wallets__pb2.HealthzRequest.FromString,
          response_serializer=wallets__pb2.HealthzResponse.SerializeToString,
      ),
      'GetWallet': grpc.unary_unary_rpc_method_handler(
          servicer.GetWallet,
          request_deserializer=wallets__pb2.WalletRequest.FromString,
          response_serializer=wallets__pb2.WalletResponse.SerializeToString,
      ),
      'StartMonitoring': grpc.unary_unary_rpc_method_handler(
          servicer.StartMonitoring,
          request_deserializer=wallets__pb2.MonitoringRequest.FromString,
          response_serializer=wallets__pb2.MonitoringResponse.SerializeToString,
      ),
      'StopMonitoring': grpc.unary_unary_rpc_method_handler(
          servicer.StopMonitoring,
          request_deserializer=wallets__pb2.MonitoringRequest.FromString,
          response_serializer=wallets__pb2.MonitoringResponse.SerializeToString,
      ),
      'CheckBalance': grpc.unary_unary_rpc_method_handler(
          servicer.CheckBalance,
          request_deserializer=wallets__pb2.CheckBalanceRequest.FromString,
          response_serializer=wallets__pb2.CheckBalanceResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'wallets.Wallets', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
