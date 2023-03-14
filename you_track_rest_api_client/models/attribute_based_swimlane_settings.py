from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_field import FilterField
    from ..models.swimlane_entity_attribute_value import SwimlaneEntityAttributeValue


T = TypeVar("T", bound="AttributeBasedSwimlaneSettings")


@attr.s(auto_attribs=True)
class AttributeBasedSwimlaneSettings:
    """
    Attributes:
        id (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        type (Union[Unset, str]):
        field (Union[Unset, FilterField]): Represents an issue property, which can be a predefined field, a custom
            field, a link, and so on.
        values (Union[Unset, List['SwimlaneEntityAttributeValue']]):
    """

    id: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    type: Union[Unset, str] = UNSET
    field: Union[Unset, "FilterField"] = UNSET
    values: Union[Unset, List["SwimlaneEntityAttributeValue"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        enabled = self.enabled
        type = self.type
        field: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field, Unset):
            field = self.field.to_dict()

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
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if type is not UNSET:
            field_dict["$type"] = type
        if field is not UNSET:
            field_dict["field"] = field
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.filter_field import FilterField
        from ..models.swimlane_entity_attribute_value import SwimlaneEntityAttributeValue

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        enabled = d.pop("enabled", UNSET)

        type = d.pop("$type", UNSET)

        _field = d.pop("field", UNSET)
        field: Union[Unset, FilterField]
        if isinstance(_field, Unset):
            field = UNSET
        else:
            field = FilterField.from_dict(_field)

        values = []
        _values = d.pop("values", UNSET)
        for values_item_data in _values or []:
            values_item = SwimlaneEntityAttributeValue.from_dict(values_item_data)

            values.append(values_item)

        attribute_based_swimlane_settings = cls(
            id=id,
            enabled=enabled,
            type=type,
            field=field,
            values=values,
        )

        attribute_based_swimlane_settings.additional_properties = d
        return attribute_based_swimlane_settings

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
