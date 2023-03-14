from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemSettings")


@attr.s(auto_attribs=True)
class SystemSettings:
    """Represents the System settings that affect core functionality of YouTrack.

    Attributes:
        id (Union[Unset, str]):
        base_url (Union[Unset, str]):
        max_upload_file_size (Union[Unset, int]):
        max_export_items (Union[Unset, int]):
        administrator_email (Union[Unset, str]):
        allow_statistics_collection (Union[Unset, bool]):
        is_application_read_only (Union[Unset, bool]):
        type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    base_url: Union[Unset, str] = UNSET
    max_upload_file_size: Union[Unset, int] = UNSET
    max_export_items: Union[Unset, int] = UNSET
    administrator_email: Union[Unset, str] = UNSET
    allow_statistics_collection: Union[Unset, bool] = UNSET
    is_application_read_only: Union[Unset, bool] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        base_url = self.base_url
        max_upload_file_size = self.max_upload_file_size
        max_export_items = self.max_export_items
        administrator_email = self.administrator_email
        allow_statistics_collection = self.allow_statistics_collection
        is_application_read_only = self.is_application_read_only
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if base_url is not UNSET:
            field_dict["baseUrl"] = base_url
        if max_upload_file_size is not UNSET:
            field_dict["maxUploadFileSize"] = max_upload_file_size
        if max_export_items is not UNSET:
            field_dict["maxExportItems"] = max_export_items
        if administrator_email is not UNSET:
            field_dict["administratorEmail"] = administrator_email
        if allow_statistics_collection is not UNSET:
            field_dict["allowStatisticsCollection"] = allow_statistics_collection
        if is_application_read_only is not UNSET:
            field_dict["isApplicationReadOnly"] = is_application_read_only
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        base_url = d.pop("baseUrl", UNSET)

        max_upload_file_size = d.pop("maxUploadFileSize", UNSET)

        max_export_items = d.pop("maxExportItems", UNSET)

        administrator_email = d.pop("administratorEmail", UNSET)

        allow_statistics_collection = d.pop("allowStatisticsCollection", UNSET)

        is_application_read_only = d.pop("isApplicationReadOnly", UNSET)

        type = d.pop("$type", UNSET)

        system_settings = cls(
            id=id,
            base_url=base_url,
            max_upload_file_size=max_upload_file_size,
            max_export_items=max_export_items,
            administrator_email=administrator_email,
            allow_statistics_collection=allow_statistics_collection,
            is_application_read_only=is_application_read_only,
            type=type,
        )

        system_settings.additional_properties = d
        return system_settings

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
