from enum import Enum


class DatabaseBackupSettingsArchiveFormat(str, Enum):
    TAR_GZ = "TAR_GZ"
    ZIP = "ZIP"

    def __str__(self) -> str:
        return str(self.value)
