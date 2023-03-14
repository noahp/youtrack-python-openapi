from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgileStatus")


@attr.s(auto_attribs=True)
class AgileStatus:
    """Shows if the board has any configuration problems.

    Attributes:
        id (Union[Unset, str]):
        valid (Union[Unset, bool]):
        has_jobs (Union[Unset, bool]):
        errors (Union[Unset, List[str]]):
        warnings (Union[Unset, List[str]]):
        type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    valid: Union[Unset, bool] = UNSET
    has_jobs: Union[Unset, bool] = UNSET
    errors: Union[Unset, List[str]] = UNSET
    warnings: Union[Unset, List[str]] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        valid = self.valid
        has_jobs = self.has_jobs
        errors: Union[Unset, List[str]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        warnings: Union[Unset, List[str]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if valid is not UNSET:
            field_dict["valid"] = valid
        if has_jobs is not UNSET:
            field_dict["hasJobs"] = has_jobs
        if errors is not UNSET:
            field_dict["errors"] = errors
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        valid = d.pop("valid", UNSET)

        has_jobs = d.pop("hasJobs", UNSET)

        errors = cast(List[str], d.pop("errors", UNSET))

        warnings = cast(List[str], d.pop("warnings", UNSET))

        type = d.pop("$type", UNSET)

        agile_status = cls(
            id=id,
            valid=valid,
            has_jobs=has_jobs,
            errors=errors,
            warnings=warnings,
            type=type,
        )

        agile_status.additional_properties = d
        return agile_status

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
