from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="PostIssuesIdAttachmentsMultipartData")


@attr.s(auto_attribs=True)
class PostIssuesIdAttachmentsMultipartData:
    """
    Attributes:
        files0 (Union[Unset, File]):
    """

    files0: Union[Unset, File] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        files0: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.files0, Unset):
            files0 = self.files0.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if files0 is not UNSET:
            field_dict["files[0]"] = files0

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        files0: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.files0, Unset):
            files0 = self.files0.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if files0 is not UNSET:
            field_dict["files[0]"] = files0

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _files0 = d.pop("files[0]", UNSET)
        files0: Union[Unset, File]
        if isinstance(_files0, Unset):
            files0 = UNSET
        else:
            files0 = File(payload=BytesIO(_files0))

        post_issues_id_attachments_multipart_data = cls(
            files0=files0,
        )

        post_issues_id_attachments_multipart_data.additional_properties = d
        return post_issues_id_attachments_multipart_data

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
