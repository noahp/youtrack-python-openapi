from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.online_users import OnlineUsers


T = TypeVar("T", bound="Telemetry")


@attr.s(auto_attribs=True)
class Telemetry:
    """Telemetry data of the YouTrack installation.

    Attributes:
        id (Union[Unset, str]):
        installation_folder (Union[Unset, str]):
        database_location (Union[Unset, str]):
        logs_location (Union[Unset, str]):
        available_processors (Union[Unset, int]):
        available_memory (Union[Unset, str]):
        allocated_memory (Union[Unset, str]):
        used_memory (Union[Unset, str]):
        uptime (Union[Unset, str]):
        started_time (Union[Unset, int]):
        database_background_threads (Union[Unset, int]):
        pending_async_jobs (Union[Unset, int]):
        cached_results_count_in_db_queries_cache (Union[Unset, int]):
        database_queries_cache_hit_rate (Union[Unset, str]):
        blob_strings_cache_hit_rate (Union[Unset, str]):
        total_transactions (Union[Unset, int]):
        transactions_per_second (Union[Unset, str]):
        requests_per_second (Union[Unset, str]):
        database_size (Union[Unset, str]):
        full_database_size (Union[Unset, str]):
        text_index_size (Union[Unset, str]):
        online_users (Union[Unset, OnlineUsers]): Stores number of online user.
        report_calculator_threads (Union[Unset, int]):
        notification_analyzer_threads (Union[Unset, int]):
        type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    installation_folder: Union[Unset, str] = UNSET
    database_location: Union[Unset, str] = UNSET
    logs_location: Union[Unset, str] = UNSET
    available_processors: Union[Unset, int] = UNSET
    available_memory: Union[Unset, str] = UNSET
    allocated_memory: Union[Unset, str] = UNSET
    used_memory: Union[Unset, str] = UNSET
    uptime: Union[Unset, str] = UNSET
    started_time: Union[Unset, int] = UNSET
    database_background_threads: Union[Unset, int] = UNSET
    pending_async_jobs: Union[Unset, int] = UNSET
    cached_results_count_in_db_queries_cache: Union[Unset, int] = UNSET
    database_queries_cache_hit_rate: Union[Unset, str] = UNSET
    blob_strings_cache_hit_rate: Union[Unset, str] = UNSET
    total_transactions: Union[Unset, int] = UNSET
    transactions_per_second: Union[Unset, str] = UNSET
    requests_per_second: Union[Unset, str] = UNSET
    database_size: Union[Unset, str] = UNSET
    full_database_size: Union[Unset, str] = UNSET
    text_index_size: Union[Unset, str] = UNSET
    online_users: Union[Unset, "OnlineUsers"] = UNSET
    report_calculator_threads: Union[Unset, int] = UNSET
    notification_analyzer_threads: Union[Unset, int] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        installation_folder = self.installation_folder
        database_location = self.database_location
        logs_location = self.logs_location
        available_processors = self.available_processors
        available_memory = self.available_memory
        allocated_memory = self.allocated_memory
        used_memory = self.used_memory
        uptime = self.uptime
        started_time = self.started_time
        database_background_threads = self.database_background_threads
        pending_async_jobs = self.pending_async_jobs
        cached_results_count_in_db_queries_cache = self.cached_results_count_in_db_queries_cache
        database_queries_cache_hit_rate = self.database_queries_cache_hit_rate
        blob_strings_cache_hit_rate = self.blob_strings_cache_hit_rate
        total_transactions = self.total_transactions
        transactions_per_second = self.transactions_per_second
        requests_per_second = self.requests_per_second
        database_size = self.database_size
        full_database_size = self.full_database_size
        text_index_size = self.text_index_size
        online_users: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.online_users, Unset):
            online_users = self.online_users.to_dict()

        report_calculator_threads = self.report_calculator_threads
        notification_analyzer_threads = self.notification_analyzer_threads
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if installation_folder is not UNSET:
            field_dict["installationFolder"] = installation_folder
        if database_location is not UNSET:
            field_dict["databaseLocation"] = database_location
        if logs_location is not UNSET:
            field_dict["logsLocation"] = logs_location
        if available_processors is not UNSET:
            field_dict["availableProcessors"] = available_processors
        if available_memory is not UNSET:
            field_dict["availableMemory"] = available_memory
        if allocated_memory is not UNSET:
            field_dict["allocatedMemory"] = allocated_memory
        if used_memory is not UNSET:
            field_dict["usedMemory"] = used_memory
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if started_time is not UNSET:
            field_dict["startedTime"] = started_time
        if database_background_threads is not UNSET:
            field_dict["databaseBackgroundThreads"] = database_background_threads
        if pending_async_jobs is not UNSET:
            field_dict["pendingAsyncJobs"] = pending_async_jobs
        if cached_results_count_in_db_queries_cache is not UNSET:
            field_dict["cachedResultsCountInDBQueriesCache"] = cached_results_count_in_db_queries_cache
        if database_queries_cache_hit_rate is not UNSET:
            field_dict["databaseQueriesCacheHitRate"] = database_queries_cache_hit_rate
        if blob_strings_cache_hit_rate is not UNSET:
            field_dict["blobStringsCacheHitRate"] = blob_strings_cache_hit_rate
        if total_transactions is not UNSET:
            field_dict["totalTransactions"] = total_transactions
        if transactions_per_second is not UNSET:
            field_dict["transactionsPerSecond"] = transactions_per_second
        if requests_per_second is not UNSET:
            field_dict["requestsPerSecond"] = requests_per_second
        if database_size is not UNSET:
            field_dict["databaseSize"] = database_size
        if full_database_size is not UNSET:
            field_dict["fullDatabaseSize"] = full_database_size
        if text_index_size is not UNSET:
            field_dict["textIndexSize"] = text_index_size
        if online_users is not UNSET:
            field_dict["onlineUsers"] = online_users
        if report_calculator_threads is not UNSET:
            field_dict["reportCalculatorThreads"] = report_calculator_threads
        if notification_analyzer_threads is not UNSET:
            field_dict["notificationAnalyzerThreads"] = notification_analyzer_threads
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.online_users import OnlineUsers

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        installation_folder = d.pop("installationFolder", UNSET)

        database_location = d.pop("databaseLocation", UNSET)

        logs_location = d.pop("logsLocation", UNSET)

        available_processors = d.pop("availableProcessors", UNSET)

        available_memory = d.pop("availableMemory", UNSET)

        allocated_memory = d.pop("allocatedMemory", UNSET)

        used_memory = d.pop("usedMemory", UNSET)

        uptime = d.pop("uptime", UNSET)

        started_time = d.pop("startedTime", UNSET)

        database_background_threads = d.pop("databaseBackgroundThreads", UNSET)

        pending_async_jobs = d.pop("pendingAsyncJobs", UNSET)

        cached_results_count_in_db_queries_cache = d.pop("cachedResultsCountInDBQueriesCache", UNSET)

        database_queries_cache_hit_rate = d.pop("databaseQueriesCacheHitRate", UNSET)

        blob_strings_cache_hit_rate = d.pop("blobStringsCacheHitRate", UNSET)

        total_transactions = d.pop("totalTransactions", UNSET)

        transactions_per_second = d.pop("transactionsPerSecond", UNSET)

        requests_per_second = d.pop("requestsPerSecond", UNSET)

        database_size = d.pop("databaseSize", UNSET)

        full_database_size = d.pop("fullDatabaseSize", UNSET)

        text_index_size = d.pop("textIndexSize", UNSET)

        _online_users = d.pop("onlineUsers", UNSET)
        online_users: Union[Unset, OnlineUsers]
        if isinstance(_online_users, Unset):
            online_users = UNSET
        else:
            online_users = OnlineUsers.from_dict(_online_users)

        report_calculator_threads = d.pop("reportCalculatorThreads", UNSET)

        notification_analyzer_threads = d.pop("notificationAnalyzerThreads", UNSET)

        type = d.pop("$type", UNSET)

        telemetry = cls(
            id=id,
            installation_folder=installation_folder,
            database_location=database_location,
            logs_location=logs_location,
            available_processors=available_processors,
            available_memory=available_memory,
            allocated_memory=allocated_memory,
            used_memory=used_memory,
            uptime=uptime,
            started_time=started_time,
            database_background_threads=database_background_threads,
            pending_async_jobs=pending_async_jobs,
            cached_results_count_in_db_queries_cache=cached_results_count_in_db_queries_cache,
            database_queries_cache_hit_rate=database_queries_cache_hit_rate,
            blob_strings_cache_hit_rate=blob_strings_cache_hit_rate,
            total_transactions=total_transactions,
            transactions_per_second=transactions_per_second,
            requests_per_second=requests_per_second,
            database_size=database_size,
            full_database_size=full_database_size,
            text_index_size=text_index_size,
            online_users=online_users,
            report_calculator_threads=report_calculator_threads,
            notification_analyzer_threads=notification_analyzer_threads,
            type=type,
        )

        telemetry.additional_properties = d
        return telemetry

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
