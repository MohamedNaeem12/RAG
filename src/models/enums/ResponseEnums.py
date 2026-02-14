from enum import Enum

class ResponseStatus(Enum):
    FILE_VALIDATED_SUCCESS = "file validated successfully"
    FILE_TYPE_NOT_SUPPORTED = "file type not supported"
    FILE_SIZE_EXCEEDS_LIMIT = "file size exceeds the maximum limit"
    FILE_UPLOADED_SUCCESS = "success"
    FILE_UPLOAD_FAILED = "file upload failed"