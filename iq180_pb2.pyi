from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SubmitAnswerRequest(_message.Message):
    __slots__ = ["token", "time", "answer"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    token: str
    time: str
    answer: bytes
    def __init__(self, token: _Optional[str] = ..., time: _Optional[str] = ..., answer: _Optional[bytes] = ...) -> None: ...

class SubmitAnswerResponse(_message.Message):
    __slots__ = ["status_code"]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    status_code: int
    def __init__(self, status_code: _Optional[int] = ...) -> None: ...

class GetTimeRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetTimeResponse(_message.Message):
    __slots__ = ["time"]
    TIME_FIELD_NUMBER: _ClassVar[int]
    time: str
    def __init__(self, time: _Optional[str] = ...) -> None: ...

class HandCheckRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class HandCheckResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class EnterGameRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class EnterGameResponse(_message.Message):
    __slots__ = ["status_code", "token"]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    status_code: int
    token: str
    def __init__(self, status_code: _Optional[int] = ..., token: _Optional[str] = ...) -> None: ...
