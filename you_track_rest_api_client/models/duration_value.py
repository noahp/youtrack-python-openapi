from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DurationValue")


@attr.s(auto_attribs=True)
class DurationValue:
    """Represents the duration value and its visual presentation.

    Attributes:
        id (Union[Unset, str]):
        minutes (Union[Unset, int]):
        presentation (Union[Unset, str]):
        type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    minutes: Union[Unset, int] = UNSET
    presentation: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        minutes = self.minutes
        presentation = self.presentation
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if minutes is not UNSET:
            field_dict["minutes"] = minutes
        if presentation is not UNSET:
            field_dict["presentation"] = presentation
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        minutes = d.pop("minutes", UNSET)

        presentation = d.pop("presentation", UNSET)

        type = d.pop("$type", UNSET)

        duration_value = cls(
            id=id,
            minutes=minutes,
            presentation=presentation,
            type=type,
        )

        duration_value.additional_properties = d
        return duration_value

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
