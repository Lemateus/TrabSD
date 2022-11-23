# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unary.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bunary.proto\x12\x05unary\"\x19\n\x0c\x43onfirmation\x12\t\n\x01\x62\x18\x01 \x01(\x08\"\x16\n\x05Price\x12\r\n\x05price\x18\x01 \x01(\x02\"#\n\x07\x43ID_OID\x12\x0b\n\x03\x63id\x18\x01 \x01(\t\x12\x0b\n\x03oid\x18\x02 \x01(\t\"\x12\n\x03\x43ID\x12\x0b\n\x03\x63id\x18\x01 \x01(\t\"\x12\n\x03OID\x12\x0b\n\x03oid\x18\x01 \x01(\t\"\x12\n\x03PID\x12\x0b\n\x03pid\x18\x01 \x01(\t\"A\n\x07Product\x12\n\n\x02\x43\x42\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\x02\x12\r\n\x05stock\x18\x04 \x01(\x05\")\n\x0bProductList\x12\x1a\n\x02PL\x18\x01 \x03(\x0b\x32\x0e.unary.Product\"\x1a\n\x07Message\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1c\n\x0fMessageResponse\x12\t\n\x01\x61\x18\x01 \x03(\x05\"4\n\x06\x43lient\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07surname\x18\x02 \x01(\t\x12\x0b\n\x03\x63pf\x18\x03 \x01(\t\"$\n\x08IndOrder\x12\x0b\n\x03pid\x18\x01 \x01(\t\x12\x0b\n\x03qtd\x18\x02 \x01(\x05\"7\n\x05Order\x12\x0b\n\x03\x63id\x18\x01 \x01(\t\x12!\n\x08products\x18\x02 \x03(\x0b\x32\x0f.unary.IndOrder\"G\n\x08ModOrder\x12\x0b\n\x03\x63id\x18\x01 \x01(\t\x12\x0b\n\x03oid\x18\x02 \x01(\t\x12!\n\x08products\x18\x03 \x03(\x0b\x32\x0f.unary.IndOrder\"\x1b\n\tOrderList\x12\x0e\n\x06orList\x18\x01 \x03(\t2\xbd\x07\n\x05Unary\x12:\n\x0e\x44\x65mandResponse\x12\x0e.unary.Message\x1a\x16.unary.MessageResponse\"\x00\x12=\n\x15\x44\x65mandClientInsertion\x12\r.unary.Client\x1a\x13.unary.Confirmation\"\x00\x12@\n\x18\x44\x65mandClientModification\x12\r.unary.Client\x1a\x13.unary.Confirmation\"\x00\x12\x37\n\x12\x44\x65mandClientSearch\x12\n.unary.CID\x1a\x13.unary.Confirmation\"\x00\x12\x38\n\x13\x44\x65mandClientRemoval\x12\n.unary.CID\x1a\x13.unary.Confirmation\"\x00\x12?\n\x16\x44\x65mandProductInsertion\x12\x0e.unary.Product\x1a\x13.unary.Confirmation\"\x00\x12\x42\n\x19\x44\x65mandProductModification\x12\x0e.unary.Product\x1a\x13.unary.Confirmation\"\x00\x12\x38\n\x13\x44\x65mandProductSearch\x12\n.unary.PID\x1a\x13.unary.Confirmation\"\x00\x12\x39\n\x14\x44\x65mandProductRemoval\x12\n.unary.PID\x1a\x13.unary.Confirmation\"\x00\x12\x35\n\x11\x44\x65mandProductList\x12\n.unary.CID\x1a\x12.unary.ProductList\"\x00\x12\x32\n\x14\x44\x65mandOrderInsertion\x12\x0c.unary.Order\x1a\n.unary.OID\"\x00\x12\x41\n\x17\x44\x65mandOrderModification\x12\x0f.unary.ModOrder\x1a\x13.unary.Confirmation\"\x00\x12\x31\n\x0f\x44\x65mandOrderList\x12\n.unary.CID\x1a\x10.unary.OrderList\"\x00\x12\x38\n\x16\x44\x65mandOrderInformation\x12\x0e.unary.CID_OID\x1a\x0c.unary.Order\"\x00\x12.\n\x10\x44\x65mandOrderPrice\x12\n.unary.OID\x1a\x0c.unary.Price\"\x00\x12?\n\x16\x44\x65mandOrderCancelation\x12\x0e.unary.CID_OID\x1a\x13.unary.Confirmation\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'unary_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONFIRMATION._serialized_start=22
  _CONFIRMATION._serialized_end=47
  _PRICE._serialized_start=49
  _PRICE._serialized_end=71
  _CID_OID._serialized_start=73
  _CID_OID._serialized_end=108
  _CID._serialized_start=110
  _CID._serialized_end=128
  _OID._serialized_start=130
  _OID._serialized_end=148
  _PID._serialized_start=150
  _PID._serialized_end=168
  _PRODUCT._serialized_start=170
  _PRODUCT._serialized_end=235
  _PRODUCTLIST._serialized_start=237
  _PRODUCTLIST._serialized_end=278
  _MESSAGE._serialized_start=280
  _MESSAGE._serialized_end=306
  _MESSAGERESPONSE._serialized_start=308
  _MESSAGERESPONSE._serialized_end=336
  _CLIENT._serialized_start=338
  _CLIENT._serialized_end=390
  _INDORDER._serialized_start=392
  _INDORDER._serialized_end=428
  _ORDER._serialized_start=430
  _ORDER._serialized_end=485
  _MODORDER._serialized_start=487
  _MODORDER._serialized_end=558
  _ORDERLIST._serialized_start=560
  _ORDERLIST._serialized_end=587
  _UNARY._serialized_start=590
  _UNARY._serialized_end=1547
# @@protoc_insertion_point(module_scope)
