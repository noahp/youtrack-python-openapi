from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.locale_descriptor import LocaleDescriptor


T = TypeVar("T", bound="LocaleSettings")


@attr.s(auto_attribs=True)
class LocaleSettings:
    """Represents the System Language settings.

    Attributes:
        id (Union[Unset, str]):
        locale (Union[Unset, LocaleDescriptor]): Represents a language locale that is used in UI.
        is_rtl (Union[Unset, bool]):
        type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    locale: Union[Unset, "LocaleDescriptor"] = UNSET
    is_rtl: Union[Unset, bool] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        locale: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.locale, Unset):
            locale = self.locale.to_dict()

        is_rtl = self.is_rtl
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if locale is not UNSET:
            field_dict["locale"] = locale
        if is_rtl is not UNSET:
            field_dict["isRTL"] = is_rtl
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.locale_descriptor import LocaleDescriptor

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _locale = d.pop("locale", UNSET)
        locale: Union[Unset, LocaleDescriptor]
        if isinstance(_locale, Unset):
            locale = UNSET
        else:
            locale = LocaleDescriptor.from_dict(_locale)

        is_rtl = d.pop("isRTL", UNSET)

        type = d.pop("$type", UNSET)

        locale_settings = cls(
            id=id,
            locale=locale,
            is_rtl=is_rtl,
            type=type,
        )

        locale_settings.additional_properties = d
        return locale_settings

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
