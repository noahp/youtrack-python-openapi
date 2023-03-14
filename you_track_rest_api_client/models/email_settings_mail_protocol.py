from enum import Enum


class EmailSettingsMailProtocol(str, Enum):
    SMTP = "SMTP"
    SMTPS = "SMTPS"
    SMTP_TLS = "SMTP_TLS"

    def __str__(self) -> str:
        return str(self.value)
