"""This module contains the general information for ComputePCIeFatalCompletionStatsHist ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputePCIeFatalCompletionStatsHistConsts():
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class ComputePCIeFatalCompletionStatsHist(ManagedObject):
    """This is ComputePCIeFatalCompletionStatsHist class."""

    consts = ComputePCIeFatalCompletionStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("ComputePCIeFatalCompletionStatsHist", "computePCIeFatalCompletionStatsHist", "[id]", VersionMeta.Version111a, "OutputOnly", 0xf, [], ["read-only"], ['computePCIeFatalCompletionStats'], [], [None])

    prop_meta = {
        "abort_errors": MoPropertyMeta("abort_errors", "AbortErrors", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "abort_errors_avg": MoPropertyMeta("abort_errors_avg", "AbortErrorsAvg", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "abort_errors_max": MoPropertyMeta("abort_errors_max", "AbortErrorsMax", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "abort_errors_min": MoPropertyMeta("abort_errors_min", "AbortErrorsMin", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "abort_errors_running": MoPropertyMeta("abort_errors_running", "AbortErrorsRunning", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "timeout_errors": MoPropertyMeta("timeout_errors", "TimeoutErrors", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "timeout_errors_avg": MoPropertyMeta("timeout_errors_avg", "TimeoutErrorsAvg", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "timeout_errors_max": MoPropertyMeta("timeout_errors_max", "TimeoutErrorsMax", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "timeout_errors_min": MoPropertyMeta("timeout_errors_min", "TimeoutErrorsMin", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "timeout_errors_running": MoPropertyMeta("timeout_errors_running", "TimeoutErrorsRunning", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version111a, MoPropertyMeta.NAMING, None, None, None, None, [], []), 
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "unexpected_errors": MoPropertyMeta("unexpected_errors", "unexpectedErrors", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "unexpected_errors_avg": MoPropertyMeta("unexpected_errors_avg", "unexpectedErrorsAvg", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "unexpected_errors_max": MoPropertyMeta("unexpected_errors_max", "unexpectedErrorsMax", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "unexpected_errors_min": MoPropertyMeta("unexpected_errors_min", "unexpectedErrorsMin", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "unexpected_errors_running": MoPropertyMeta("unexpected_errors_running", "unexpectedErrorsRunning", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "AbortErrors": "abort_errors", 
        "AbortErrorsAvg": "abort_errors_avg", 
        "AbortErrorsMax": "abort_errors_max", 
        "AbortErrorsMin": "abort_errors_min", 
        "AbortErrorsRunning": "abort_errors_running", 
        "TimeoutErrors": "timeout_errors", 
        "TimeoutErrorsAvg": "timeout_errors_avg", 
        "TimeoutErrorsMax": "timeout_errors_max", 
        "TimeoutErrorsMin": "timeout_errors_min", 
        "TimeoutErrorsRunning": "timeout_errors_running", 
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "mostRecent": "most_recent", 
        "rn": "rn", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "unexpectedErrors": "unexpected_errors", 
        "unexpectedErrorsAvg": "unexpected_errors_avg", 
        "unexpectedErrorsMax": "unexpected_errors_max", 
        "unexpectedErrorsMin": "unexpected_errors_min", 
        "unexpectedErrorsRunning": "unexpected_errors_running", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.abort_errors = None
        self.abort_errors_avg = None
        self.abort_errors_max = None
        self.abort_errors_min = None
        self.abort_errors_running = None
        self.timeout_errors = None
        self.timeout_errors_avg = None
        self.timeout_errors_max = None
        self.timeout_errors_min = None
        self.timeout_errors_running = None
        self.child_action = None
        self.most_recent = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.unexpected_errors = None
        self.unexpected_errors_avg = None
        self.unexpected_errors_max = None
        self.unexpected_errors_min = None
        self.unexpected_errors_running = None

        ManagedObject.__init__(self, "ComputePCIeFatalCompletionStatsHist", parent_mo_or_dn, **kwargs)

