# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: communication.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="communication.proto",
    package="",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x13\x63ommunication.proto"\x97\x01\n\x05State\x12\x1d\n\x06status\x18\x01 \x01(\x0e\x32\r.State.Status\x12\x0f\n\x07message\x18\x02 \x01(\t"^\n\x06Status\x12\x10\n\x0c\x43LIENT_READY\x10\x01\x12\x10\n\x0cSERVER_READY\x10\x02\x12\x16\n\x12\x45XECUTION_COMPLETE\x10\x03\x12\x18\n\x14\x42\x41\x43KTRACING_COMPLETE\x10\x04"\x1c\n\x08Location\x12\x10\n\x08location\x18\x01 \x01(\t"$\n\x0e\x46rameBackTrace\x12\x12\n\nback_trace\x18\x01 \x01(\t2c\n\rCommunication\x12\x1f\n\tSyncState\x12\x06.State\x1a\x06.State"\x00\x30\x01\x12\x31\n\x11GetFrameBackTrace\x12\t.Location\x1a\x0f.FrameBackTrace"\x00',
)


_STATE_STATUS = _descriptor.EnumDescriptor(
    name="Status",
    full_name="State.Status",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="CLIENT_READY",
            index=0,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="SERVER_READY",
            index=1,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="EXECUTION_COMPLETE",
            index=2,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="BACKTRACING_COMPLETE",
            index=3,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=81,
    serialized_end=175,
)
_sym_db.RegisterEnumDescriptor(_STATE_STATUS)


_STATE = _descriptor.Descriptor(
    name="State",
    full_name="State",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="status",
            full_name="State.status",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=1,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="message",
            full_name="State.message",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_STATE_STATUS],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=24,
    serialized_end=175,
)


_LOCATION = _descriptor.Descriptor(
    name="Location",
    full_name="Location",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="location",
            full_name="Location.location",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=177,
    serialized_end=205,
)


_FRAMEBACKTRACE = _descriptor.Descriptor(
    name="FrameBackTrace",
    full_name="FrameBackTrace",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="back_trace",
            full_name="FrameBackTrace.back_trace",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=207,
    serialized_end=243,
)

_STATE.fields_by_name["status"].enum_type = _STATE_STATUS
_STATE_STATUS.containing_type = _STATE
DESCRIPTOR.message_types_by_name["State"] = _STATE
DESCRIPTOR.message_types_by_name["Location"] = _LOCATION
DESCRIPTOR.message_types_by_name["FrameBackTrace"] = _FRAMEBACKTRACE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

State = _reflection.GeneratedProtocolMessageType(
    "State",
    (_message.Message,),
    {
        "DESCRIPTOR": _STATE,
        "__module__": "communication_pb2"
        # @@protoc_insertion_point(class_scope:State)
    },
)
_sym_db.RegisterMessage(State)

Location = _reflection.GeneratedProtocolMessageType(
    "Location",
    (_message.Message,),
    {
        "DESCRIPTOR": _LOCATION,
        "__module__": "communication_pb2"
        # @@protoc_insertion_point(class_scope:Location)
    },
)
_sym_db.RegisterMessage(Location)

FrameBackTrace = _reflection.GeneratedProtocolMessageType(
    "FrameBackTrace",
    (_message.Message,),
    {
        "DESCRIPTOR": _FRAMEBACKTRACE,
        "__module__": "communication_pb2"
        # @@protoc_insertion_point(class_scope:FrameBackTrace)
    },
)
_sym_db.RegisterMessage(FrameBackTrace)


_COMMUNICATION = _descriptor.ServiceDescriptor(
    name="Communication",
    full_name="Communication",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=245,
    serialized_end=344,
    methods=[
        _descriptor.MethodDescriptor(
            name="SyncState",
            full_name="Communication.SyncState",
            index=0,
            containing_service=None,
            input_type=_STATE,
            output_type=_STATE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="GetFrameBackTrace",
            full_name="Communication.GetFrameBackTrace",
            index=1,
            containing_service=None,
            input_type=_LOCATION,
            output_type=_FRAMEBACKTRACE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_COMMUNICATION)

DESCRIPTOR.services_by_name["Communication"] = _COMMUNICATION

# @@protoc_insertion_point(module_scope)