from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ParsedCommand")


@attr.s(auto_attribs=True)
class ParsedCommand:
    """Represents the command that was parsed from the provided query.

    Attributes:
        id (Union[Unset, str]):
        description (Union[Unset, str]):
        error (Union[Unset, bool]):
        delete (Union[Unset, bool]):
        type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    error: Union[Unset, bool] = UNSET
    delete: Union[Unset, bool] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        description = self.description
        error = self.error
        delete = self.delete
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if error is not UNSET:
            field_dict["error"] = error
        if delete is not UNSET:
            field_dict["delete"] = delete
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        error = d.pop("error", UNSET)

        delete = d.pop("delete", UNSET)

        type = d.pop("$type", UNSET)

        parsed_command = cls(
            id=id,
            description=description,
            error=error,
            delete=delete,
            type=type,
        )

        parsed_command.additional_properties = d
        return parsed_command

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
