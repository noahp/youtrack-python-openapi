from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.general_user_profile import GeneralUserProfile
    from ..models.notifications_user_profile import NotificationsUserProfile
    from ..models.time_tracking_user_profile import TimeTrackingUserProfile


T = TypeVar("T", bound="UserProfiles")


@attr.s(auto_attribs=True)
class UserProfiles:
    """Represents a group of settings of a user profile in YouTrack.

    Attributes:
        id (Union[Unset, str]):
        general (Union[Unset, GeneralUserProfile]): Represents the user profile in YouTrack.
        notifications (Union[Unset, NotificationsUserProfile]): Represents the notification settings in the profile of
            the specific user.
        timetracking (Union[Unset, TimeTrackingUserProfile]): Represents time tracking settings in the user's profile.
        type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    general: Union[Unset, "GeneralUserProfile"] = UNSET
    notifications: Union[Unset, "NotificationsUserProfile"] = UNSET
    timetracking: Union[Unset, "TimeTrackingUserProfile"] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        general: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.general, Unset):
            general = self.general.to_dict()

        notifications: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notifications, Unset):
            notifications = self.notifications.to_dict()

        timetracking: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.timetracking, Unset):
            timetracking = self.timetracking.to_dict()

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if general is not UNSET:
            field_dict["general"] = general
        if notifications is not UNSET:
            field_dict["notifications"] = notifications
        if timetracking is not UNSET:
            field_dict["timetracking"] = timetracking
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.general_user_profile import GeneralUserProfile
        from ..models.notifications_user_profile import NotificationsUserProfile
        from ..models.time_tracking_user_profile import TimeTrackingUserProfile

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _general = d.pop("general", UNSET)
        general: Union[Unset, GeneralUserProfile]
        if isinstance(_general, Unset):
            general = UNSET
        else:
            general = GeneralUserProfile.from_dict(_general)

        _notifications = d.pop("notifications", UNSET)
        notifications: Union[Unset, NotificationsUserProfile]
        if isinstance(_notifications, Unset):
            notifications = UNSET
        else:
            notifications = NotificationsUserProfile.from_dict(_notifications)

        _timetracking = d.pop("timetracking", UNSET)
        timetracking: Union[Unset, TimeTrackingUserProfile]
        if isinstance(_timetracking, Unset):
            timetracking = UNSET
        else:
            timetracking = TimeTrackingUserProfile.from_dict(_timetracking)

        type = d.pop("$type", UNSET)

        user_profiles = cls(
            id=id,
            general=general,
            notifications=notifications,
            timetracking=timetracking,
            type=type,
        )

        user_profiles.additional_properties = d
        return user_profiles

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
