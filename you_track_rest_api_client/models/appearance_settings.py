from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.date_format_descriptor import DateFormatDescriptor
    from ..models.logo import Logo
    from ..models.time_zone_descriptor import TimeZoneDescriptor


T = TypeVar("T", bound="AppearanceSettings")


@attr.s(auto_attribs=True)
class AppearanceSettings:
    """Represents the Visual settings of the YouTrack service.

    Attributes:
        id (Union[Unset, str]):
        time_zone (Union[Unset, TimeZoneDescriptor]): Represents a time zone.
        date_field_format (Union[Unset, DateFormatDescriptor]): Represents date format.
        logo (Union[Unset, Logo]): Company logo that is used in YouTrack.
        type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    time_zone: Union[Unset, "TimeZoneDescriptor"] = UNSET
    date_field_format: Union[Unset, "DateFormatDescriptor"] = UNSET
    logo: Union[Unset, "Logo"] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        time_zone: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time_zone, Unset):
            time_zone = self.time_zone.to_dict()

        date_field_format: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.date_field_format, Unset):
            date_field_format = self.date_field_format.to_dict()

        logo: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.logo, Unset):
            logo = self.logo.to_dict()

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if date_field_format is not UNSET:
            field_dict["dateFieldFormat"] = date_field_format
        if logo is not UNSET:
            field_dict["logo"] = logo
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.date_format_descriptor import DateFormatDescriptor
        from ..models.logo import Logo
        from ..models.time_zone_descriptor import TimeZoneDescriptor

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _time_zone = d.pop("timeZone", UNSET)
        time_zone: Union[Unset, TimeZoneDescriptor]
        if isinstance(_time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = TimeZoneDescriptor.from_dict(_time_zone)

        _date_field_format = d.pop("dateFieldFormat", UNSET)
        date_field_format: Union[Unset, DateFormatDescriptor]
        if isinstance(_date_field_format, Unset):
            date_field_format = UNSET
        else:
            date_field_format = DateFormatDescriptor.from_dict(_date_field_format)

        _logo = d.pop("logo", UNSET)
        logo: Union[Unset, Logo]
        if isinstance(_logo, Unset):
            logo = UNSET
        else:
            logo = Logo.from_dict(_logo)

        type = d.pop("$type", UNSET)

        appearance_settings = cls(
            id=id,
            time_zone=time_zone,
            date_field_format=date_field_format,
            logo=logo,
            type=type,
        )

        appearance_settings.additional_properties = d
        return appearance_settings

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
