from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bundle_element import BundleElement


T = TypeVar("T", bound="BaseBundle")


@attr.s(auto_attribs=True)
class BaseBundle:
    """Represents a set of field values in YouTrack.

    Attributes:
        id (Union[Unset, str]):
        is_updateable (Union[Unset, bool]):
        type (Union[Unset, str]):
        values (Union[Unset, List['BundleElement']]):
    """

    id: Union[Unset, str] = UNSET
    is_updateable: Union[Unset, bool] = UNSET
    type: Union[Unset, str] = UNSET
    values: Union[Unset, List["BundleElement"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        is_updateable = self.is_updateable
        type = self.type
        values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()

                values.append(values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_updateable is not UNSET:
            field_dict["isUpdateable"] = is_updateable
        if type is not UNSET:
            field_dict["$type"] = type
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bundle_element import BundleElement

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        is_updateable = d.pop("isUpdateable", UNSET)

        type = d.pop("$type", UNSET)

        values = []
        _values = d.pop("values", UNSET)
        for values_item_data in _values or []:
            values_item = BundleElement.from_dict(values_item_data)

            values.append(values_item)

        base_bundle = cls(
            id=id,
            is_updateable=is_updateable,
            type=type,
            values=values,
        )

        base_bundle.additional_properties = d
        return base_bundle

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
