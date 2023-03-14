from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue_folder import IssueFolder


T = TypeVar("T", bound="IssueCountResponse")


@attr.s(auto_attribs=True)
class IssueCountResponse:
    """Represents the number of issues in a search result.

    Attributes:
        id (Union[Unset, str]):
        count (Union[Unset, int]):
        unresolved_only (Union[Unset, bool]):
        query (Union[Unset, str]):
        folder (Union[Unset, IssueFolder]): Represents an issue folder, such as a project, a saved search, or a tag.
        type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    unresolved_only: Union[Unset, bool] = UNSET
    query: Union[Unset, str] = UNSET
    folder: Union[Unset, "IssueFolder"] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        count = self.count
        unresolved_only = self.unresolved_only
        query = self.query
        folder: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.folder, Unset):
            folder = self.folder.to_dict()

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if count is not UNSET:
            field_dict["count"] = count
        if unresolved_only is not UNSET:
            field_dict["unresolvedOnly"] = unresolved_only
        if query is not UNSET:
            field_dict["query"] = query
        if folder is not UNSET:
            field_dict["folder"] = folder
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.issue_folder import IssueFolder

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        count = d.pop("count", UNSET)

        unresolved_only = d.pop("unresolvedOnly", UNSET)

        query = d.pop("query", UNSET)

        _folder = d.pop("folder", UNSET)
        folder: Union[Unset, IssueFolder]
        if isinstance(_folder, Unset):
            folder = UNSET
        else:
            folder = IssueFolder.from_dict(_folder)

        type = d.pop("$type", UNSET)

        issue_count_response = cls(
            id=id,
            count=count,
            unresolved_only=unresolved_only,
            query=query,
            folder=folder,
            type=type,
        )

        issue_count_response.additional_properties = d
        return issue_count_response

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
