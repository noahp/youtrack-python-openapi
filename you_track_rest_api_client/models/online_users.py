from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OnlineUsers")


@attr.s(auto_attribs=True)
class OnlineUsers:
    """Stores number of online user.

    Attributes:
        id (Union[Unset, str]):
        users (Union[Unset, int]):
        type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    users: Union[Unset, int] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        users = self.users
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if users is not UNSET:
            field_dict["users"] = users
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        users = d.pop("users", UNSET)

        type = d.pop("$type", UNSET)

        online_users = cls(
            id=id,
            users=users,
            type=type,
        )

        online_users.additional_properties = d
        return online_users

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
