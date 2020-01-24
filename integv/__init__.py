import mimetypes as _mimetypes
import os as _os
from ._base import _IntegrityVerifierBase
import integv.video
import integv.image

_mimetypes.init([_os.path.join(_os.split(__file__)[0], "mime.types")])


class FileIntegrityVerifier(_IntegrityVerifierBase):
    def guess_type(self, filename):
        return _mimetypes.guess_type(filename)[0]

    def verify(self, file, file_type=None):
        if file_type is None:
            file_type = self.guess_type(file)
        verifier = self._MIME_MAPPING[file_type]()
        return verifier.verify(file)
