from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue_folder import IssueFolder
    from ..models.suggestion import Suggestion


T = TypeVar("T", bound="SearchSuggestions")


@attr.s(auto_attribs=True)
class SearchSuggestions:
    """Represents the list of search suggestions for the currently entered search query.

    Attributes:
        id (Union[Unset, str]):
        caret (Union[Unset, int]):
        ignore_unresolved_setting (Union[Unset, bool]):
        query (Union[Unset, str]):
        suggestions (Union[Unset, List['Suggestion']]):
        folders (Union[Unset, List['IssueFolder']]):
        type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    caret: Union[Unset, int] = UNSET
    ignore_unresolved_setting: Union[Unset, bool] = UNSET
    query: Union[Unset, str] = UNSET
    suggestions: Union[Unset, List["Suggestion"]] = UNSET
    folders: Union[Unset, List["IssueFolder"]] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        caret = self.caret
        ignore_unresolved_setting = self.ignore_unresolved_setting
        query = self.query
        suggestions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.suggestions, Unset):
            suggestions = []
            for suggestions_item_data in self.suggestions:
                suggestions_item = suggestions_item_data.to_dict()

                suggestions.append(suggestions_item)

        folders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.folders, Unset):
            folders = []
            for folders_item_data in self.folders:
                folders_item = folders_item_data.to_dict()

                folders.append(folders_item)

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if caret is not UNSET:
            field_dict["caret"] = caret
        if ignore_unresolved_setting is not UNSET:
            field_dict["ignoreUnresolvedSetting"] = ignore_unresolved_setting
        if query is not UNSET:
            field_dict["query"] = query
        if suggestions is not UNSET:
            field_dict["suggestions"] = suggestions
        if folders is not UNSET:
            field_dict["folders"] = folders
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.issue_folder import IssueFolder
        from ..models.suggestion import Suggestion

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        caret = d.pop("caret", UNSET)

        ignore_unresolved_setting = d.pop("ignoreUnresolvedSetting", UNSET)

        query = d.pop("query", UNSET)

        suggestions = []
        _suggestions = d.pop("suggestions", UNSET)
        for suggestions_item_data in _suggestions or []:
            suggestions_item = Suggestion.from_dict(suggestions_item_data)

            suggestions.append(suggestions_item)

        folders = []
        _folders = d.pop("folders", UNSET)
        for folders_item_data in _folders or []:
            folders_item = IssueFolder.from_dict(folders_item_data)

            folders.append(folders_item)

        type = d.pop("$type", UNSET)

        search_suggestions = cls(
            id=id,
            caret=caret,
            ignore_unresolved_setting=ignore_unresolved_setting,
            query=query,
            suggestions=suggestions,
            folders=folders,
            type=type,
        )

        search_suggestions.additional_properties = d
        return search_suggestions

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
