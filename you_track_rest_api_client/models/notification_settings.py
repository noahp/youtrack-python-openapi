from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.email_settings import EmailSettings
    from ..models.jabber_settings import JabberSettings


T = TypeVar("T", bound="NotificationSettings")


@attr.s(auto_attribs=True)
class NotificationSettings:
    """Represents the Notifications settings of the YouTrack service.

    Attributes:
        id (Union[Unset, str]):
        email_settings (Union[Unset, EmailSettings]): Represents email settings for this YouTrack installation.
        jabber_settings (Union[Unset, JabberSettings]): Represents jabber settings for this YouTrack installation.
        type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    email_settings: Union[Unset, "EmailSettings"] = UNSET
    jabber_settings: Union[Unset, "JabberSettings"] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        email_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.email_settings, Unset):
            email_settings = self.email_settings.to_dict()

        jabber_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.jabber_settings, Unset):
            jabber_settings = self.jabber_settings.to_dict()

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if email_settings is not UNSET:
            field_dict["emailSettings"] = email_settings
        if jabber_settings is not UNSET:
            field_dict["jabberSettings"] = jabber_settings
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.email_settings import EmailSettings
        from ..models.jabber_settings import JabberSettings

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _email_settings = d.pop("emailSettings", UNSET)
        email_settings: Union[Unset, EmailSettings]
        if isinstance(_email_settings, Unset):
            email_settings = UNSET
        else:
            email_settings = EmailSettings.from_dict(_email_settings)

        _jabber_settings = d.pop("jabberSettings", UNSET)
        jabber_settings: Union[Unset, JabberSettings]
        if isinstance(_jabber_settings, Unset):
            jabber_settings = UNSET
        else:
            jabber_settings = JabberSettings.from_dict(_jabber_settings)

        type = d.pop("$type", UNSET)

        notification_settings = cls(
            id=id,
            email_settings=email_settings,
            jabber_settings=jabber_settings,
            type=type,
        )

        notification_settings.additional_properties = d
        return notification_settings

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
