from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.email_settings_mail_protocol import EmailSettingsMailProtocol
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.storage_entry import StorageEntry


T = TypeVar("T", bound="EmailSettings")


@attr.s(auto_attribs=True)
class EmailSettings:
    """Represents email settings for this YouTrack installation.

    Attributes:
        id (Union[Unset, str]):
        is_enabled (Union[Unset, bool]):
        host (Union[Unset, str]):
        port (Union[Unset, int]):
        mail_protocol (Union[Unset, EmailSettingsMailProtocol]):
        anonymous (Union[Unset, bool]):
        login (Union[Unset, str]):
        ssl_key (Union[Unset, StorageEntry]): SSL key representation.
        from_ (Union[Unset, str]):
        reply_to (Union[Unset, str]):
        type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    is_enabled: Union[Unset, bool] = UNSET
    host: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    mail_protocol: Union[Unset, EmailSettingsMailProtocol] = UNSET
    anonymous: Union[Unset, bool] = UNSET
    login: Union[Unset, str] = UNSET
    ssl_key: Union[Unset, "StorageEntry"] = UNSET
    from_: Union[Unset, str] = UNSET
    reply_to: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        is_enabled = self.is_enabled
        host = self.host
        port = self.port
        mail_protocol: Union[Unset, str] = UNSET
        if not isinstance(self.mail_protocol, Unset):
            mail_protocol = self.mail_protocol.value

        anonymous = self.anonymous
        login = self.login
        ssl_key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ssl_key, Unset):
            ssl_key = self.ssl_key.to_dict()

        from_ = self.from_
        reply_to = self.reply_to
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if host is not UNSET:
            field_dict["host"] = host
        if port is not UNSET:
            field_dict["port"] = port
        if mail_protocol is not UNSET:
            field_dict["mailProtocol"] = mail_protocol
        if anonymous is not UNSET:
            field_dict["anonymous"] = anonymous
        if login is not UNSET:
            field_dict["login"] = login
        if ssl_key is not UNSET:
            field_dict["sslKey"] = ssl_key
        if from_ is not UNSET:
            field_dict["from"] = from_
        if reply_to is not UNSET:
            field_dict["replyTo"] = reply_to
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.storage_entry import StorageEntry

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        is_enabled = d.pop("isEnabled", UNSET)

        host = d.pop("host", UNSET)

        port = d.pop("port", UNSET)

        _mail_protocol = d.pop("mailProtocol", UNSET)
        mail_protocol: Union[Unset, EmailSettingsMailProtocol]
        if isinstance(_mail_protocol, Unset):
            mail_protocol = UNSET
        else:
            mail_protocol = EmailSettingsMailProtocol(_mail_protocol)

        anonymous = d.pop("anonymous", UNSET)

        login = d.pop("login", UNSET)

        _ssl_key = d.pop("sslKey", UNSET)
        ssl_key: Union[Unset, StorageEntry]
        if isinstance(_ssl_key, Unset):
            ssl_key = UNSET
        else:
            ssl_key = StorageEntry.from_dict(_ssl_key)

        from_ = d.pop("from", UNSET)

        reply_to = d.pop("replyTo", UNSET)

        type = d.pop("$type", UNSET)

        email_settings = cls(
            id=id,
            is_enabled=is_enabled,
            host=host,
            port=port,
            mail_protocol=mail_protocol,
            anonymous=anonymous,
            login=login,
            ssl_key=ssl_key,
            from_=from_,
            reply_to=reply_to,
            type=type,
        )

        email_settings.additional_properties = d
        return email_settings

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
