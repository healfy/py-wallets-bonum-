# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wallets.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_swagger.options import annotations_pb2 as protoc__gen__swagger_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='wallets.proto',
  package='wallets',
  syntax='proto3',
  serialized_options=_b('\222AE\022\026\n\017Wallets service2\0031.0\"\004/api*\001\0012\020application/json:\020application/json'),
  serialized_pb=_b('\n\rwallets.proto\x12\x07wallets\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/api/annotations.proto\x1a,protoc-gen-swagger/options/annotations.proto\"N\n\x0eResponseHeader\x12\'\n\x06status\x18\x01 \x01(\x0e\x32\x17.wallets.ResponseStatus\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"\x10\n\x0eHealthzRequest\":\n\x0fHealthzResponse\x12\'\n\x06header\x18\x01 \x01(\x0b\x32\x17.wallets.ResponseHeader\"f\n\x06Wallet\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x15\n\rcurrency_slug\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12\x13\n\x0bis_platform\x18\x04 \x01(\x08\x12\x13\n\x0b\x65xternal_id\x18\x05 \x01(\x03\"4\n\x11MonitoringRequest\x12\x1f\n\x06wallet\x18\x01 \x01(\x0b\x32\x0f.wallets.Wallet\"0\n\rWalletRequest\x12\x1f\n\x06wallet\x18\x01 \x01(\x0b\x32\x0f.wallets.Wallet\"9\n\x0eWalletResponse\x12\'\n\x06header\x18\x01 \x01(\x0b\x32\x17.wallets.ResponseHeader\"=\n\x12MonitoringResponse\x12\'\n\x06header\x18\x01 \x01(\x0b\x32\x17.wallets.ResponseHeader\"A\n\x13\x43heckBalanceRequest\x12\x15\n\rbody_currency\x18\x01 \x01(\t\x12\x13\n\x0b\x62ody_amount\x18\x02 \x01(\t\"?\n\x14\x43heckBalanceResponse\x12\'\n\x06header\x18\x01 \x01(\x0b\x32\x17.wallets.ResponseHeader*J\n\x0eResponseStatus\x12\x0b\n\x07NOT_SET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\x13\n\x0fINVALID_REQUEST\x10\x03\x32\xf3\x02\n\x07Wallets\x12>\n\x07Healthz\x12\x17.wallets.HealthzRequest\x1a\x18.wallets.HealthzResponse\"\x00\x12>\n\tGetWallet\x12\x16.wallets.WalletRequest\x1a\x17.wallets.WalletResponse\"\x00\x12L\n\x0fStartMonitoring\x12\x1a.wallets.MonitoringRequest\x1a\x1b.wallets.MonitoringResponse\"\x00\x12K\n\x0eStopMonitoring\x12\x1a.wallets.MonitoringRequest\x1a\x1b.wallets.MonitoringResponse\"\x00\x12M\n\x0c\x43heckBalance\x12\x1c.wallets.CheckBalanceRequest\x1a\x1d.wallets.CheckBalanceResponse\"\x00\x42H\x92\x41\x45\x12\x16\n\x0fWallets service2\x03\x31.0\"\x04/api*\x01\x01\x32\x10\x61pplication/json:\x10\x61pplication/jsonb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,protoc__gen__swagger_dot_options_dot_annotations__pb2.DESCRIPTOR,])

_RESPONSESTATUS = _descriptor.EnumDescriptor(
  name='ResponseStatus',
  full_name='wallets.ResponseStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOT_SET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_REQUEST', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=787,
  serialized_end=861,
)
_sym_db.RegisterEnumDescriptor(_RESPONSESTATUS)

ResponseStatus = enum_type_wrapper.EnumTypeWrapper(_RESPONSESTATUS)
NOT_SET = 0
SUCCESS = 1
ERROR = 2
INVALID_REQUEST = 3



_RESPONSEHEADER = _descriptor.Descriptor(
  name='ResponseHeader',
  full_name='wallets.ResponseHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='wallets.ResponseHeader.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='wallets.ResponseHeader.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=167,
  serialized_end=245,
)


_HEALTHZREQUEST = _descriptor.Descriptor(
  name='HealthzRequest',
  full_name='wallets.HealthzRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=247,
  serialized_end=263,
)


_HEALTHZRESPONSE = _descriptor.Descriptor(
  name='HealthzResponse',
  full_name='wallets.HealthzResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='wallets.HealthzResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=265,
  serialized_end=323,
)


_WALLET = _descriptor.Descriptor(
  name='Wallet',
  full_name='wallets.Wallet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='wallets.Wallet.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currency_slug', full_name='wallets.Wallet.currency_slug', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='wallets.Wallet.address', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_platform', full_name='wallets.Wallet.is_platform', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='external_id', full_name='wallets.Wallet.external_id', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=325,
  serialized_end=427,
)


_MONITORINGREQUEST = _descriptor.Descriptor(
  name='MonitoringRequest',
  full_name='wallets.MonitoringRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wallet', full_name='wallets.MonitoringRequest.wallet', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=429,
  serialized_end=481,
)


_WALLETREQUEST = _descriptor.Descriptor(
  name='WalletRequest',
  full_name='wallets.WalletRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wallet', full_name='wallets.WalletRequest.wallet', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=483,
  serialized_end=531,
)


_WALLETRESPONSE = _descriptor.Descriptor(
  name='WalletResponse',
  full_name='wallets.WalletResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='wallets.WalletResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=533,
  serialized_end=590,
)


_MONITORINGRESPONSE = _descriptor.Descriptor(
  name='MonitoringResponse',
  full_name='wallets.MonitoringResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='wallets.MonitoringResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=592,
  serialized_end=653,
)


_CHECKBALANCEREQUEST = _descriptor.Descriptor(
  name='CheckBalanceRequest',
  full_name='wallets.CheckBalanceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='body_currency', full_name='wallets.CheckBalanceRequest.body_currency', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body_amount', full_name='wallets.CheckBalanceRequest.body_amount', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=655,
  serialized_end=720,
)


_CHECKBALANCERESPONSE = _descriptor.Descriptor(
  name='CheckBalanceResponse',
  full_name='wallets.CheckBalanceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='wallets.CheckBalanceResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=722,
  serialized_end=785,
)

_RESPONSEHEADER.fields_by_name['status'].enum_type = _RESPONSESTATUS
_HEALTHZRESPONSE.fields_by_name['header'].message_type = _RESPONSEHEADER
_MONITORINGREQUEST.fields_by_name['wallet'].message_type = _WALLET
_WALLETREQUEST.fields_by_name['wallet'].message_type = _WALLET
_WALLETRESPONSE.fields_by_name['header'].message_type = _RESPONSEHEADER
_MONITORINGRESPONSE.fields_by_name['header'].message_type = _RESPONSEHEADER
_CHECKBALANCERESPONSE.fields_by_name['header'].message_type = _RESPONSEHEADER
DESCRIPTOR.message_types_by_name['ResponseHeader'] = _RESPONSEHEADER
DESCRIPTOR.message_types_by_name['HealthzRequest'] = _HEALTHZREQUEST
DESCRIPTOR.message_types_by_name['HealthzResponse'] = _HEALTHZRESPONSE
DESCRIPTOR.message_types_by_name['Wallet'] = _WALLET
DESCRIPTOR.message_types_by_name['MonitoringRequest'] = _MONITORINGREQUEST
DESCRIPTOR.message_types_by_name['WalletRequest'] = _WALLETREQUEST
DESCRIPTOR.message_types_by_name['WalletResponse'] = _WALLETRESPONSE
DESCRIPTOR.message_types_by_name['MonitoringResponse'] = _MONITORINGRESPONSE
DESCRIPTOR.message_types_by_name['CheckBalanceRequest'] = _CHECKBALANCEREQUEST
DESCRIPTOR.message_types_by_name['CheckBalanceResponse'] = _CHECKBALANCERESPONSE
DESCRIPTOR.enum_types_by_name['ResponseStatus'] = _RESPONSESTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResponseHeader = _reflection.GeneratedProtocolMessageType('ResponseHeader', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEHEADER,
  __module__ = 'wallets_pb2'
  # @@protoc_insertion_point(class_scope:wallets.ResponseHeader)
  ))
_sym_db.RegisterMessage(ResponseHeader)

HealthzRequest = _reflection.GeneratedProtocolMessageType('HealthzRequest', (_message.Message,), dict(
  DESCRIPTOR = _HEALTHZREQUEST,
  __module__ = 'wallets_pb2'
  # @@protoc_insertion_point(class_scope:wallets.HealthzRequest)
  ))
_sym_db.RegisterMessage(HealthzRequest)

HealthzResponse = _reflection.GeneratedProtocolMessageType('HealthzResponse', (_message.Message,), dict(
  DESCRIPTOR = _HEALTHZRESPONSE,
  __module__ = 'wallets_pb2'
  # @@protoc_insertion_point(class_scope:wallets.HealthzResponse)
  ))
_sym_db.RegisterMessage(HealthzResponse)

Wallet = _reflection.GeneratedProtocolMessageType('Wallet', (_message.Message,), dict(
  DESCRIPTOR = _WALLET,
  __module__ = 'wallets_pb2'
  # @@protoc_insertion_point(class_scope:wallets.Wallet)
  ))
_sym_db.RegisterMessage(Wallet)

MonitoringRequest = _reflection.GeneratedProtocolMessageType('MonitoringRequest', (_message.Message,), dict(
  DESCRIPTOR = _MONITORINGREQUEST,
  __module__ = 'wallets_pb2'
  # @@protoc_insertion_point(class_scope:wallets.MonitoringRequest)
  ))
_sym_db.RegisterMessage(MonitoringRequest)

WalletRequest = _reflection.GeneratedProtocolMessageType('WalletRequest', (_message.Message,), dict(
  DESCRIPTOR = _WALLETREQUEST,
  __module__ = 'wallets_pb2'
  # @@protoc_insertion_point(class_scope:wallets.WalletRequest)
  ))
_sym_db.RegisterMessage(WalletRequest)

WalletResponse = _reflection.GeneratedProtocolMessageType('WalletResponse', (_message.Message,), dict(
  DESCRIPTOR = _WALLETRESPONSE,
  __module__ = 'wallets_pb2'
  # @@protoc_insertion_point(class_scope:wallets.WalletResponse)
  ))
_sym_db.RegisterMessage(WalletResponse)

MonitoringResponse = _reflection.GeneratedProtocolMessageType('MonitoringResponse', (_message.Message,), dict(
  DESCRIPTOR = _MONITORINGRESPONSE,
  __module__ = 'wallets_pb2'
  # @@protoc_insertion_point(class_scope:wallets.MonitoringResponse)
  ))
_sym_db.RegisterMessage(MonitoringResponse)

CheckBalanceRequest = _reflection.GeneratedProtocolMessageType('CheckBalanceRequest', (_message.Message,), dict(
  DESCRIPTOR = _CHECKBALANCEREQUEST,
  __module__ = 'wallets_pb2'
  # @@protoc_insertion_point(class_scope:wallets.CheckBalanceRequest)
  ))
_sym_db.RegisterMessage(CheckBalanceRequest)

CheckBalanceResponse = _reflection.GeneratedProtocolMessageType('CheckBalanceResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHECKBALANCERESPONSE,
  __module__ = 'wallets_pb2'
  # @@protoc_insertion_point(class_scope:wallets.CheckBalanceResponse)
  ))
_sym_db.RegisterMessage(CheckBalanceResponse)


DESCRIPTOR._options = None

_WALLETS = _descriptor.ServiceDescriptor(
  name='Wallets',
  full_name='wallets.Wallets',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=864,
  serialized_end=1235,
  methods=[
  _descriptor.MethodDescriptor(
    name='Healthz',
    full_name='wallets.Wallets.Healthz',
    index=0,
    containing_service=None,
    input_type=_HEALTHZREQUEST,
    output_type=_HEALTHZRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetWallet',
    full_name='wallets.Wallets.GetWallet',
    index=1,
    containing_service=None,
    input_type=_WALLETREQUEST,
    output_type=_WALLETRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StartMonitoring',
    full_name='wallets.Wallets.StartMonitoring',
    index=2,
    containing_service=None,
    input_type=_MONITORINGREQUEST,
    output_type=_MONITORINGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StopMonitoring',
    full_name='wallets.Wallets.StopMonitoring',
    index=3,
    containing_service=None,
    input_type=_MONITORINGREQUEST,
    output_type=_MONITORINGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CheckBalance',
    full_name='wallets.Wallets.CheckBalance',
    index=4,
    containing_service=None,
    input_type=_CHECKBALANCEREQUEST,
    output_type=_CHECKBALANCERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_WALLETS)

DESCRIPTOR.services_by_name['Wallets'] = _WALLETS

# @@protoc_insertion_point(module_scope)
