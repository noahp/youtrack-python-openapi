from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="JabberSettings")


@attr.s(auto_attribs=True)
class JabberSettings:
    """Represents jabber settings for this YouTrack installation.

    Attributes:
        id (Union[Unset, str]):
        is_enabled (Union[Unset, bool]):
        host (Union[Unset, str]):
        port (Union[Unset, int]):
        login (Union[Unset, str]):
        service_name (Union[Unset, str]):
        type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    is_enabled: Union[Unset, bool] = UNSET
    host: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    login: Union[Unset, str] = UNSET
    service_name: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        is_enabled = self.is_enabled
        host = self.host
        port = self.port
        login = self.login
        service_name = self.service_name
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
        if login is not UNSET:
            field_dict["login"] = login
        if service_name is not UNSET:
            field_dict["serviceName"] = service_name
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        is_enabled = d.pop("isEnabled", UNSET)

        host = d.pop("host", UNSET)

        port = d.pop("port", UNSET)

        login = d.pop("login", UNSET)

        service_name = d.pop("serviceName", UNSET)

        type = d.pop("$type", UNSET)

        jabber_settings = cls(
            id=id,
            is_enabled=is_enabled,
            host=host,
            port=port,
            login=login,
            service_name=service_name,
            type=type,
        )

        jabber_settings.additional_properties = d
        return jabber_settings

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
