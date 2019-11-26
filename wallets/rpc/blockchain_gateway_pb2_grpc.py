# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import blockchain_gateway_pb2 as blockchain__gateway__pb2


class BlockchainGatewayServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Health = channel.unary_unary(
        '/blockchain_gateway.BlockchainGatewayService/Health',
        request_serializer=blockchain__gateway__pb2.EmptyRequest.SerializeToString,
        response_deserializer=blockchain__gateway__pb2.EmptyRequest.FromString,
        )
    self.GetAvailableCurrencies = channel.unary_unary(
        '/blockchain_gateway.BlockchainGatewayService/GetAvailableCurrencies',
        request_serializer=blockchain__gateway__pb2.EmptyRequest.SerializeToString,
        response_deserializer=blockchain__gateway__pb2.AvailableCurrenciesResponse.FromString,
        )
    self.GetBalance = channel.unary_unary(
        '/blockchain_gateway.BlockchainGatewayService/GetBalance',
        request_serializer=blockchain__gateway__pb2.GetBalanceRequest.SerializeToString,
        response_deserializer=blockchain__gateway__pb2.GetBalanceResponse.FromString,
        )
    self.GetWallet = channel.unary_unary(
        '/blockchain_gateway.BlockchainGatewayService/GetWallet',
        request_serializer=blockchain__gateway__pb2.GetWalletRequest.SerializeToString,
        response_deserializer=blockchain__gateway__pb2.GetWalletResponse.FromString,
        )
    self.SendTransaction = channel.unary_unary(
        '/blockchain_gateway.BlockchainGatewayService/SendTransaction',
        request_serializer=blockchain__gateway__pb2.SendTransactionMessage.SerializeToString,
        response_deserializer=blockchain__gateway__pb2.SendTransactionMessage.FromString,
        )
    self.GetTransactionsList = channel.unary_unary(
        '/blockchain_gateway.BlockchainGatewayService/GetTransactionsList',
        request_serializer=blockchain__gateway__pb2.GetTransactionsListRequest.SerializeToString,
        response_deserializer=blockchain__gateway__pb2.GetTransactionsListResponse.FromString,
        )
    self.GetTransaction = channel.unary_unary(
        '/blockchain_gateway.BlockchainGatewayService/GetTransaction',
        request_serializer=blockchain__gateway__pb2.GetTransactionRequest.SerializeToString,
        response_deserializer=blockchain__gateway__pb2.GetTransactionResponse.FromString,
        )
    self.SendFromColdWallet = channel.unary_unary(
        '/blockchain_gateway.BlockchainGatewayService/SendFromColdWallet',
        request_serializer=blockchain__gateway__pb2.SendFromColdWalletRequest.SerializeToString,
        response_deserializer=blockchain__gateway__pb2.SendFromColdWalletResponse.FromString,
        )
    self.SendToColdWallet = channel.unary_unary(
        '/blockchain_gateway.BlockchainGatewayService/SendToColdWallet',
        request_serializer=blockchain__gateway__pb2.SendToColdWalletRequest.SerializeToString,
        response_deserializer=blockchain__gateway__pb2.SendToColdWalletResponse.FromString,
        )
    self.CheckAddress = channel.unary_unary(
        '/blockchain_gateway.BlockchainGatewayService/CheckAddress',
        request_serializer=blockchain__gateway__pb2.CheckAddressRequest.SerializeToString,
        response_deserializer=blockchain__gateway__pb2.CheckAddressResponse.FromString,
        )


class BlockchainGatewayServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Health(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAvailableCurrencies(self, request, context):
    """GetAvailableCurrencies returns list of currencies and tokens supproted by service
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBalance(self, request, context):
    """GetBalance returns balance of wallet from request
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetWallet(self, request, context):
    """GetWallet returns new wallet for selected currency, or returns address, if ID in
    request specified
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendTransaction(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTransactionsList(self, request, context):
    """GetTransactionsList returns filtered transactions list for specified wallet
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTransaction(self, request, context):
    """GetTransaction returns transaction by hash and currencySlug
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendFromColdWallet(self, request, context):
    """SendFromColdWallet sends currency from platfrom to specified wallet
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendToColdWallet(self, request, context):
    """SendToColdWallet grabs amount from pledge wallet to platform's main wallet
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CheckAddress(self, request, context):
    """GetBalance returns balance of wallet from request
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BlockchainGatewayServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Health': grpc.unary_unary_rpc_method_handler(
          servicer.Health,
          request_deserializer=blockchain__gateway__pb2.EmptyRequest.FromString,
          response_serializer=blockchain__gateway__pb2.EmptyRequest.SerializeToString,
      ),
      'GetAvailableCurrencies': grpc.unary_unary_rpc_method_handler(
          servicer.GetAvailableCurrencies,
          request_deserializer=blockchain__gateway__pb2.EmptyRequest.FromString,
          response_serializer=blockchain__gateway__pb2.AvailableCurrenciesResponse.SerializeToString,
      ),
      'GetBalance': grpc.unary_unary_rpc_method_handler(
          servicer.GetBalance,
          request_deserializer=blockchain__gateway__pb2.GetBalanceRequest.FromString,
          response_serializer=blockchain__gateway__pb2.GetBalanceResponse.SerializeToString,
      ),
      'GetWallet': grpc.unary_unary_rpc_method_handler(
          servicer.GetWallet,
          request_deserializer=blockchain__gateway__pb2.GetWalletRequest.FromString,
          response_serializer=blockchain__gateway__pb2.GetWalletResponse.SerializeToString,
      ),
      'SendTransaction': grpc.unary_unary_rpc_method_handler(
          servicer.SendTransaction,
          request_deserializer=blockchain__gateway__pb2.SendTransactionMessage.FromString,
          response_serializer=blockchain__gateway__pb2.SendTransactionMessage.SerializeToString,
      ),
      'GetTransactionsList': grpc.unary_unary_rpc_method_handler(
          servicer.GetTransactionsList,
          request_deserializer=blockchain__gateway__pb2.GetTransactionsListRequest.FromString,
          response_serializer=blockchain__gateway__pb2.GetTransactionsListResponse.SerializeToString,
      ),
      'GetTransaction': grpc.unary_unary_rpc_method_handler(
          servicer.GetTransaction,
          request_deserializer=blockchain__gateway__pb2.GetTransactionRequest.FromString,
          response_serializer=blockchain__gateway__pb2.GetTransactionResponse.SerializeToString,
      ),
      'SendFromColdWallet': grpc.unary_unary_rpc_method_handler(
          servicer.SendFromColdWallet,
          request_deserializer=blockchain__gateway__pb2.SendFromColdWalletRequest.FromString,
          response_serializer=blockchain__gateway__pb2.SendFromColdWalletResponse.SerializeToString,
      ),
      'SendToColdWallet': grpc.unary_unary_rpc_method_handler(
          servicer.SendToColdWallet,
          request_deserializer=blockchain__gateway__pb2.SendToColdWalletRequest.FromString,
          response_serializer=blockchain__gateway__pb2.SendToColdWalletResponse.SerializeToString,
      ),
      'CheckAddress': grpc.unary_unary_rpc_method_handler(
          servicer.CheckAddress,
          request_deserializer=blockchain__gateway__pb2.CheckAddressRequest.FromString,
          response_serializer=blockchain__gateway__pb2.CheckAddressResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'blockchain_gateway.BlockchainGatewayService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
