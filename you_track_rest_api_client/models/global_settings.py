from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.appearance_settings import AppearanceSettings
    from ..models.license_ import License
    from ..models.locale_settings import LocaleSettings
    from ..models.notification_settings import NotificationSettings
    from ..models.rest_cors_settings import RestCorsSettings
    from ..models.system_settings import SystemSettings


T = TypeVar("T", bound="GlobalSettings")


@attr.s(auto_attribs=True)
class GlobalSettings:
    """Represents application-wide settings.

    Attributes:
        id (Union[Unset, str]):
        system_settings (Union[Unset, SystemSettings]): Represents the System settings that affect core functionality of
            YouTrack.
        notification_settings (Union[Unset, NotificationSettings]): Represents the Notifications settings of the
            YouTrack service.
        rest_settings (Union[Unset, RestCorsSettings]): Represents the Resource Sharing (CORS) configuration of the
            service.
        appearance_settings (Union[Unset, AppearanceSettings]): Represents the Visual settings of the YouTrack service.
        locale_settings (Union[Unset, LocaleSettings]): Represents the System Language settings.
        license_ (Union[Unset, License]): Represents the current license of the YouTrack service.
        type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    system_settings: Union[Unset, "SystemSettings"] = UNSET
    notification_settings: Union[Unset, "NotificationSettings"] = UNSET
    rest_settings: Union[Unset, "RestCorsSettings"] = UNSET
    appearance_settings: Union[Unset, "AppearanceSettings"] = UNSET
    locale_settings: Union[Unset, "LocaleSettings"] = UNSET
    license_: Union[Unset, "License"] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        system_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.system_settings, Unset):
            system_settings = self.system_settings.to_dict()

        notification_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notification_settings, Unset):
            notification_settings = self.notification_settings.to_dict()

        rest_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rest_settings, Unset):
            rest_settings = self.rest_settings.to_dict()

        appearance_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.appearance_settings, Unset):
            appearance_settings = self.appearance_settings.to_dict()

        locale_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.locale_settings, Unset):
            locale_settings = self.locale_settings.to_dict()

        license_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.license_, Unset):
            license_ = self.license_.to_dict()

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if system_settings is not UNSET:
            field_dict["systemSettings"] = system_settings
        if notification_settings is not UNSET:
            field_dict["notificationSettings"] = notification_settings
        if rest_settings is not UNSET:
            field_dict["restSettings"] = rest_settings
        if appearance_settings is not UNSET:
            field_dict["appearanceSettings"] = appearance_settings
        if locale_settings is not UNSET:
            field_dict["localeSettings"] = locale_settings
        if license_ is not UNSET:
            field_dict["license"] = license_
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.appearance_settings import AppearanceSettings
        from ..models.license_ import License
        from ..models.locale_settings import LocaleSettings
        from ..models.notification_settings import NotificationSettings
        from ..models.rest_cors_settings import RestCorsSettings
        from ..models.system_settings import SystemSettings

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _system_settings = d.pop("systemSettings", UNSET)
        system_settings: Union[Unset, SystemSettings]
        if isinstance(_system_settings, Unset):
            system_settings = UNSET
        else:
            system_settings = SystemSettings.from_dict(_system_settings)

        _notification_settings = d.pop("notificationSettings", UNSET)
        notification_settings: Union[Unset, NotificationSettings]
        if isinstance(_notification_settings, Unset):
            notification_settings = UNSET
        else:
            notification_settings = NotificationSettings.from_dict(_notification_settings)

        _rest_settings = d.pop("restSettings", UNSET)
        rest_settings: Union[Unset, RestCorsSettings]
        if isinstance(_rest_settings, Unset):
            rest_settings = UNSET
        else:
            rest_settings = RestCorsSettings.from_dict(_rest_settings)

        _appearance_settings = d.pop("appearanceSettings", UNSET)
        appearance_settings: Union[Unset, AppearanceSettings]
        if isinstance(_appearance_settings, Unset):
            appearance_settings = UNSET
        else:
            appearance_settings = AppearanceSettings.from_dict(_appearance_settings)

        _locale_settings = d.pop("localeSettings", UNSET)
        locale_settings: Union[Unset, LocaleSettings]
        if isinstance(_locale_settings, Unset):
            locale_settings = UNSET
        else:
            locale_settings = LocaleSettings.from_dict(_locale_settings)

        _license_ = d.pop("license", UNSET)
        license_: Union[Unset, License]
        if isinstance(_license_, Unset):
            license_ = UNSET
        else:
            license_ = License.from_dict(_license_)

        type = d.pop("$type", UNSET)

        global_settings = cls(
            id=id,
            system_settings=system_settings,
            notification_settings=notification_settings,
            rest_settings=rest_settings,
            appearance_settings=appearance_settings,
            locale_settings=locale_settings,
            license_=license_,
            type=type,
        )

        global_settings.additional_properties = d
        return global_settings

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
