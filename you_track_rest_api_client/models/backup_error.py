from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupError")


@attr.s(auto_attribs=True)
class BackupError:
    """Represents an error that appeared during the backup.

    Attributes:
        id (Union[Unset, str]):
        date (Union[Unset, int]):
        error_message (Union[Unset, str]):
        type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    date: Union[Unset, int] = UNSET
    error_message: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        date = self.date
        error_message = self.error_message
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if date is not UNSET:
            field_dict["date"] = date
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        date = d.pop("date", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        type = d.pop("$type", UNSET)

        backup_error = cls(
            id=id,
            date=date,
            error_message=error_message,
            type=type,
        )

        backup_error.additional_properties = d
        return backup_error

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
