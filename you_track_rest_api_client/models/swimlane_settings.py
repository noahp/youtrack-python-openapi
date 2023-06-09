from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SwimlaneSettings")


@attr.s(auto_attribs=True)
class SwimlaneSettings:
    """Base entity for different swimlane settings

    Attributes:
        id (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        enabled = self.enabled
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        enabled = d.pop("enabled", UNSET)

        type = d.pop("$type", UNSET)

        swimlane_settings = cls(
            id=id,
            enabled=enabled,
            type=type,
        )

        swimlane_settings.additional_properties = d
        return swimlane_settings

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
