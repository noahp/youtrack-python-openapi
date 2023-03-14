from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.date_format_descriptor import DateFormatDescriptor
    from ..models.locale_descriptor import LocaleDescriptor
    from ..models.time_zone_descriptor import TimeZoneDescriptor


T = TypeVar("T", bound="GeneralUserProfile")


@attr.s(auto_attribs=True)
class GeneralUserProfile:
    """Represents the user profile in YouTrack.

    Attributes:
        id (Union[Unset, str]):
        date_field_format (Union[Unset, DateFormatDescriptor]): Represents date format.
        timezone (Union[Unset, TimeZoneDescriptor]): Represents a time zone.
        locale (Union[Unset, LocaleDescriptor]): Represents a language locale that is used in UI.
        type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    date_field_format: Union[Unset, "DateFormatDescriptor"] = UNSET
    timezone: Union[Unset, "TimeZoneDescriptor"] = UNSET
    locale: Union[Unset, "LocaleDescriptor"] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        date_field_format: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.date_field_format, Unset):
            date_field_format = self.date_field_format.to_dict()

        timezone: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.timezone, Unset):
            timezone = self.timezone.to_dict()

        locale: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.locale, Unset):
            locale = self.locale.to_dict()

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if date_field_format is not UNSET:
            field_dict["dateFieldFormat"] = date_field_format
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if locale is not UNSET:
            field_dict["locale"] = locale
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.date_format_descriptor import DateFormatDescriptor
        from ..models.locale_descriptor import LocaleDescriptor
        from ..models.time_zone_descriptor import TimeZoneDescriptor

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _date_field_format = d.pop("dateFieldFormat", UNSET)
        date_field_format: Union[Unset, DateFormatDescriptor]
        if isinstance(_date_field_format, Unset):
            date_field_format = UNSET
        else:
            date_field_format = DateFormatDescriptor.from_dict(_date_field_format)

        _timezone = d.pop("timezone", UNSET)
        timezone: Union[Unset, TimeZoneDescriptor]
        if isinstance(_timezone, Unset):
            timezone = UNSET
        else:
            timezone = TimeZoneDescriptor.from_dict(_timezone)

        _locale = d.pop("locale", UNSET)
        locale: Union[Unset, LocaleDescriptor]
        if isinstance(_locale, Unset):
            locale = UNSET
        else:
            locale = LocaleDescriptor.from_dict(_locale)

        type = d.pop("$type", UNSET)

        general_user_profile = cls(
            id=id,
            date_field_format=date_field_format,
            timezone=timezone,
            locale=locale,
            type=type,
        )

        general_user_profile.additional_properties = d
        return general_user_profile

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
