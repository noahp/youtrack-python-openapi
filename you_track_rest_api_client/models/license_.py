from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="License")


@attr.s(auto_attribs=True)
class License:
    """Represents the current license of the YouTrack service.

    Attributes:
        id (Union[Unset, str]):
        username (Union[Unset, str]):
        license_ (Union[Unset, str]):
        error (Union[Unset, str]):
        type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    license_: Union[Unset, str] = UNSET
    error: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        username = self.username
        license_ = self.license_
        error = self.error
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if username is not UNSET:
            field_dict["username"] = username
        if license_ is not UNSET:
            field_dict["license"] = license_
        if error is not UNSET:
            field_dict["error"] = error
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        username = d.pop("username", UNSET)

        license_ = d.pop("license", UNSET)

        error = d.pop("error", UNSET)

        type = d.pop("$type", UNSET)

        license_ = cls(
            id=id,
            username=username,
            license_=license_,
            error=error,
            type=type,
        )

        license_.additional_properties = d
        return license_

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
