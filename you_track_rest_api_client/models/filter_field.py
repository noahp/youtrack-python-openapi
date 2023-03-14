from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterField")


@attr.s(auto_attribs=True)
class FilterField:
    """Represents an issue property, which can be a predefined field, a custom field, a link, and so on.

    Attributes:
        id (Union[Unset, str]):
        presentation (Union[Unset, str]):
        name (Union[Unset, str]):
        type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    presentation: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        presentation = self.presentation
        name = self.name
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if presentation is not UNSET:
            field_dict["presentation"] = presentation
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        presentation = d.pop("presentation", UNSET)

        name = d.pop("name", UNSET)

        type = d.pop("$type", UNSET)

        filter_field = cls(
            id=id,
            presentation=presentation,
            name=name,
            type=type,
        )

        filter_field.additional_properties = d
        return filter_field

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
