from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseStatus


class DataController(BaseController):
    def __init__(self):
        super().__init__()

    def validate_file_type(self, file: UploadFile):
        # Handle None content_type by treating it as text/plain
        content_type = file.content_type if file.content_type is not None else 'text/plain'
        if content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseStatus.FILE_TYPE_NOT_SUPPORTED.value

        # Note: UploadFile may not expose a `size` attribute; code assumes
        # callers provide files with accessible size, otherwise this check
        # will be skipped.
        file_size = getattr(file, 'size', None)
        if file_size is not None and file_size > self.app_settings.FILE_MAX_SIZE:
            return False, ResponseStatus.FILE_SIZE_EXCEEDS_LIMIT.value

        return True, ResponseStatus.FILE_VALIDATED_SUCCESS.value