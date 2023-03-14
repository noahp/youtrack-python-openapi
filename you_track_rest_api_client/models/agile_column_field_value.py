from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgileColumnFieldValue")


@attr.s(auto_attribs=True)
class AgileColumnFieldValue:
    """Represents a field value or values, parameterizing agile column.

    Attributes:
        id (Union[Unset, str]):
        type (Union[Unset, str]):
        name (Union[Unset, str]):
        is_resolved (Union[Unset, bool]):
    """

    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    is_resolved: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type
        name = self.name
        is_resolved = self.is_resolved

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["$type"] = type
        if name is not UNSET:
            field_dict["name"] = name
        if is_resolved is not UNSET:
            field_dict["isResolved"] = is_resolved

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        type = d.pop("$type", UNSET)

        name = d.pop("name", UNSET)

        is_resolved = d.pop("isResolved", UNSET)

        agile_column_field_value = cls(
            id=id,
            type=type,
            name=name,
            is_resolved=is_resolved,
        )

        agile_column_field_value.additional_properties = d
        return agile_column_field_value

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
