from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationsUserProfile")


@attr.s(auto_attribs=True)
class NotificationsUserProfile:
    """Represents the notification settings in the profile of the specific user.

    Attributes:
        id (Union[Unset, str]):
        notify_on_own_changes (Union[Unset, bool]):
        jabber_notifications_enabled (Union[Unset, bool]):
        email_notifications_enabled (Union[Unset, bool]):
        mention_notifications_enabled (Union[Unset, bool]):
        duplicate_cluster_notifications_enabled (Union[Unset, bool]):
        mailbox_integration_notifications_enabled (Union[Unset, bool]):
        use_plain_text_emails (Union[Unset, bool]):
        auto_watch_on_comment (Union[Unset, bool]):
        auto_watch_on_create (Union[Unset, bool]):
        auto_watch_on_vote (Union[Unset, bool]):
        auto_watch_on_update (Union[Unset, bool]):
        type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    notify_on_own_changes: Union[Unset, bool] = UNSET
    jabber_notifications_enabled: Union[Unset, bool] = UNSET
    email_notifications_enabled: Union[Unset, bool] = UNSET
    mention_notifications_enabled: Union[Unset, bool] = UNSET
    duplicate_cluster_notifications_enabled: Union[Unset, bool] = UNSET
    mailbox_integration_notifications_enabled: Union[Unset, bool] = UNSET
    use_plain_text_emails: Union[Unset, bool] = UNSET
    auto_watch_on_comment: Union[Unset, bool] = UNSET
    auto_watch_on_create: Union[Unset, bool] = UNSET
    auto_watch_on_vote: Union[Unset, bool] = UNSET
    auto_watch_on_update: Union[Unset, bool] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        notify_on_own_changes = self.notify_on_own_changes
        jabber_notifications_enabled = self.jabber_notifications_enabled
        email_notifications_enabled = self.email_notifications_enabled
        mention_notifications_enabled = self.mention_notifications_enabled
        duplicate_cluster_notifications_enabled = self.duplicate_cluster_notifications_enabled
        mailbox_integration_notifications_enabled = self.mailbox_integration_notifications_enabled
        use_plain_text_emails = self.use_plain_text_emails
        auto_watch_on_comment = self.auto_watch_on_comment
        auto_watch_on_create = self.auto_watch_on_create
        auto_watch_on_vote = self.auto_watch_on_vote
        auto_watch_on_update = self.auto_watch_on_update
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if notify_on_own_changes is not UNSET:
            field_dict["notifyOnOwnChanges"] = notify_on_own_changes
        if jabber_notifications_enabled is not UNSET:
            field_dict["jabberNotificationsEnabled"] = jabber_notifications_enabled
        if email_notifications_enabled is not UNSET:
            field_dict["emailNotificationsEnabled"] = email_notifications_enabled
        if mention_notifications_enabled is not UNSET:
            field_dict["mentionNotificationsEnabled"] = mention_notifications_enabled
        if duplicate_cluster_notifications_enabled is not UNSET:
            field_dict["duplicateClusterNotificationsEnabled"] = duplicate_cluster_notifications_enabled
        if mailbox_integration_notifications_enabled is not UNSET:
            field_dict["mailboxIntegrationNotificationsEnabled"] = mailbox_integration_notifications_enabled
        if use_plain_text_emails is not UNSET:
            field_dict["usePlainTextEmails"] = use_plain_text_emails
        if auto_watch_on_comment is not UNSET:
            field_dict["autoWatchOnComment"] = auto_watch_on_comment
        if auto_watch_on_create is not UNSET:
            field_dict["autoWatchOnCreate"] = auto_watch_on_create
        if auto_watch_on_vote is not UNSET:
            field_dict["autoWatchOnVote"] = auto_watch_on_vote
        if auto_watch_on_update is not UNSET:
            field_dict["autoWatchOnUpdate"] = auto_watch_on_update
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        notify_on_own_changes = d.pop("notifyOnOwnChanges", UNSET)

        jabber_notifications_enabled = d.pop("jabberNotificationsEnabled", UNSET)

        email_notifications_enabled = d.pop("emailNotificationsEnabled", UNSET)

        mention_notifications_enabled = d.pop("mentionNotificationsEnabled", UNSET)

        duplicate_cluster_notifications_enabled = d.pop("duplicateClusterNotificationsEnabled", UNSET)

        mailbox_integration_notifications_enabled = d.pop("mailboxIntegrationNotificationsEnabled", UNSET)

        use_plain_text_emails = d.pop("usePlainTextEmails", UNSET)

        auto_watch_on_comment = d.pop("autoWatchOnComment", UNSET)

        auto_watch_on_create = d.pop("autoWatchOnCreate", UNSET)

        auto_watch_on_vote = d.pop("autoWatchOnVote", UNSET)

        auto_watch_on_update = d.pop("autoWatchOnUpdate", UNSET)

        type = d.pop("$type", UNSET)

        notifications_user_profile = cls(
            id=id,
            notify_on_own_changes=notify_on_own_changes,
            jabber_notifications_enabled=jabber_notifications_enabled,
            email_notifications_enabled=email_notifications_enabled,
            mention_notifications_enabled=mention_notifications_enabled,
            duplicate_cluster_notifications_enabled=duplicate_cluster_notifications_enabled,
            mailbox_integration_notifications_enabled=mailbox_integration_notifications_enabled,
            use_plain_text_emails=use_plain_text_emails,
            auto_watch_on_comment=auto_watch_on_comment,
            auto_watch_on_create=auto_watch_on_create,
            auto_watch_on_vote=auto_watch_on_vote,
            auto_watch_on_update=auto_watch_on_update,
            type=type,
        )

        notifications_user_profile.additional_properties = d
        return notifications_user_profile

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
