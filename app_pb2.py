# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: app.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'app.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

from google.protobuf.empty_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tapp.proto\x12\x08glossary\x1a\x1bgoogle/protobuf/empty.proto\"4\n\x04Word\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\ndefinition\x18\x03 \x01(\t\"1\n\x11\x43reateWordRequest\x12\x1c\n\x04word\x18\x01 \x01(\x0b\x32\x0e.glossary.Word\"\x1f\n\x11\x44\x65leteWordRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"\x1e\n\x0eGetWordRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"1\n\x11UpdateWordRequest\x12\x1c\n\x04word\x18\x01 \x01(\x0b\x32\x0e.glossary.Word\",\n\x0cWordResponse\x12\x1c\n\x04word\x18\x01 \x01(\x0b\x32\x0e.glossary.Word\"-\n\x0cListResponse\x12\x1d\n\x05words\x18\x01 \x03(\x0b\x32\x0e.glossary.Word2\xd7\x02\n\x0fGlossaryService\x12\x41\n\nCreateWord\x12\x1b.glossary.CreateWordRequest\x1a\x16.glossary.WordResponse\x12;\n\x07GetWord\x12\x18.glossary.GetWordRequest\x1a\x16.glossary.WordResponse\x12\x41\n\nDeleteWord\x12\x1b.glossary.DeleteWordRequest\x1a\x16.google.protobuf.Empty\x12\x41\n\nUpdateWord\x12\x1b.glossary.UpdateWordRequest\x1a\x16.glossary.WordResponse\x12>\n\x0cListAllWords\x12\x16.google.protobuf.Empty\x1a\x16.glossary.ListResponseP\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_WORD']._serialized_start=52
  _globals['_WORD']._serialized_end=104
  _globals['_CREATEWORDREQUEST']._serialized_start=106
  _globals['_CREATEWORDREQUEST']._serialized_end=155
  _globals['_DELETEWORDREQUEST']._serialized_start=157
  _globals['_DELETEWORDREQUEST']._serialized_end=188
  _globals['_GETWORDREQUEST']._serialized_start=190
  _globals['_GETWORDREQUEST']._serialized_end=220
  _globals['_UPDATEWORDREQUEST']._serialized_start=222
  _globals['_UPDATEWORDREQUEST']._serialized_end=271
  _globals['_WORDRESPONSE']._serialized_start=273
  _globals['_WORDRESPONSE']._serialized_end=317
  _globals['_LISTRESPONSE']._serialized_start=319
  _globals['_LISTRESPONSE']._serialized_end=364
  _globals['_GLOSSARYSERVICE']._serialized_start=367
  _globals['_GLOSSARYSERVICE']._serialized_end=710
# @@protoc_insertion_point(module_scope)
