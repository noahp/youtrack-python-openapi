from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IssueLinkType")


@attr.s(auto_attribs=True)
class IssueLinkType:
    """Represents the settings of a link type in YouTrack.

    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        localized_name (Union[Unset, str]):
        source_to_target (Union[Unset, str]):
        localized_source_to_target (Union[Unset, str]):
        target_to_source (Union[Unset, str]):
        localized_target_to_source (Union[Unset, str]):
        directed (Union[Unset, bool]):
        aggregation (Union[Unset, bool]):
        read_only (Union[Unset, bool]):
        type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    localized_name: Union[Unset, str] = UNSET
    source_to_target: Union[Unset, str] = UNSET
    localized_source_to_target: Union[Unset, str] = UNSET
    target_to_source: Union[Unset, str] = UNSET
    localized_target_to_source: Union[Unset, str] = UNSET
    directed: Union[Unset, bool] = UNSET
    aggregation: Union[Unset, bool] = UNSET
    read_only: Union[Unset, bool] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        localized_name = self.localized_name
        source_to_target = self.source_to_target
        localized_source_to_target = self.localized_source_to_target
        target_to_source = self.target_to_source
        localized_target_to_source = self.localized_target_to_source
        directed = self.directed
        aggregation = self.aggregation
        read_only = self.read_only
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if localized_name is not UNSET:
            field_dict["localizedName"] = localized_name
        if source_to_target is not UNSET:
            field_dict["sourceToTarget"] = source_to_target
        if localized_source_to_target is not UNSET:
            field_dict["localizedSourceToTarget"] = localized_source_to_target
        if target_to_source is not UNSET:
            field_dict["targetToSource"] = target_to_source
        if localized_target_to_source is not UNSET:
            field_dict["localizedTargetToSource"] = localized_target_to_source
        if directed is not UNSET:
            field_dict["directed"] = directed
        if aggregation is not UNSET:
            field_dict["aggregation"] = aggregation
        if read_only is not UNSET:
            field_dict["readOnly"] = read_only
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        localized_name = d.pop("localizedName", UNSET)

        source_to_target = d.pop("sourceToTarget", UNSET)

        localized_source_to_target = d.pop("localizedSourceToTarget", UNSET)

        target_to_source = d.pop("targetToSource", UNSET)

        localized_target_to_source = d.pop("localizedTargetToSource", UNSET)

        directed = d.pop("directed", UNSET)

        aggregation = d.pop("aggregation", UNSET)

        read_only = d.pop("readOnly", UNSET)

        type = d.pop("$type", UNSET)

        issue_link_type = cls(
            id=id,
            name=name,
            localized_name=localized_name,
            source_to_target=source_to_target,
            localized_source_to_target=localized_source_to_target,
            target_to_source=target_to_source,
            localized_target_to_source=localized_target_to_source,
            directed=directed,
            aggregation=aggregation,
            read_only=read_only,
            type=type,
        )

        issue_link_type.additional_properties = d
        return issue_link_type

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
