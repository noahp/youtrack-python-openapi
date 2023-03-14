from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bundle import Bundle
    from ..models.field_style import FieldStyle


T = TypeVar("T", bound="BundleElement")


@attr.s(auto_attribs=True)
class BundleElement:
    """Represents a field value in YouTrack.

    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        bundle (Union[Unset, Bundle]): Represents a set of custom field values in YouTrack.
        description (Union[Unset, str]):
        archived (Union[Unset, bool]):
        ordinal (Union[Unset, int]):
        color (Union[Unset, FieldStyle]): Represents the style settings of the field in YouTrack.
        has_running_job (Union[Unset, bool]):
        type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    bundle: Union[Unset, "Bundle"] = UNSET
    description: Union[Unset, str] = UNSET
    archived: Union[Unset, bool] = UNSET
    ordinal: Union[Unset, int] = UNSET
    color: Union[Unset, "FieldStyle"] = UNSET
    has_running_job: Union[Unset, bool] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        bundle: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bundle, Unset):
            bundle = self.bundle.to_dict()

        description = self.description
        archived = self.archived
        ordinal = self.ordinal
        color: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.to_dict()

        has_running_job = self.has_running_job
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if bundle is not UNSET:
            field_dict["bundle"] = bundle
        if description is not UNSET:
            field_dict["description"] = description
        if archived is not UNSET:
            field_dict["archived"] = archived
        if ordinal is not UNSET:
            field_dict["ordinal"] = ordinal
        if color is not UNSET:
            field_dict["color"] = color
        if has_running_job is not UNSET:
            field_dict["hasRunningJob"] = has_running_job
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bundle import Bundle
        from ..models.field_style import FieldStyle

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _bundle = d.pop("bundle", UNSET)
        bundle: Union[Unset, Bundle]
        if isinstance(_bundle, Unset):
            bundle = UNSET
        else:
            bundle = Bundle.from_dict(_bundle)

        description = d.pop("description", UNSET)

        archived = d.pop("archived", UNSET)

        ordinal = d.pop("ordinal", UNSET)

        _color = d.pop("color", UNSET)
        color: Union[Unset, FieldStyle]
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = FieldStyle.from_dict(_color)

        has_running_job = d.pop("hasRunningJob", UNSET)

        type = d.pop("$type", UNSET)

        bundle_element = cls(
            id=id,
            name=name,
            bundle=bundle,
            description=description,
            archived=archived,
            ordinal=ordinal,
            color=color,
            has_running_job=has_running_job,
            type=type,
        )

        bundle_element.additional_properties = d
        return bundle_element

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
