"""This module contains the general information for AdaptorMenloEthErrorStats ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AdaptorMenloEthErrorStatsConsts():
    MENLO_ETH_INDEX_0 = "0"
    MENLO_ETH_INDEX_0_A = "0_A"
    MENLO_ETH_INDEX_0_B = "0_B"
    MENLO_ETH_INDEX_1 = "1"
    MENLO_ETH_INDEX_1_A = "1_A"
    MENLO_ETH_INDEX_1_B = "1_B"
    MENLO_ETH_INDEX_UNKNOWN = "unknown"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class AdaptorMenloEthErrorStats(ManagedObject):
    """This is AdaptorMenloEthErrorStats class."""

    consts = AdaptorMenloEthErrorStatsConsts()
    naming_props = set(['menloEthIndex'])

    mo_meta = MoMeta("AdaptorMenloEthErrorStats", "adaptorMenloEthErrorStats", "menlo-eth-error-stats-[menlo_eth_index]", VersionMeta.Version111a, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['adaptorUnit'], ['adaptorMenloEthErrorStatsHist'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "correctable_errors": MoPropertyMeta("correctable_errors", "correctableErrors", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "correctable_errors_delta": MoPropertyMeta("correctable_errors_delta", "correctableErrorsDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "correctable_errors_delta_avg": MoPropertyMeta("correctable_errors_delta_avg", "correctableErrorsDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "correctable_errors_delta_max": MoPropertyMeta("correctable_errors_delta_max", "correctableErrorsDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "correctable_errors_delta_min": MoPropertyMeta("correctable_errors_delta_min", "correctableErrorsDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "drop_acl": MoPropertyMeta("drop_acl", "dropAcl", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "drop_acl_delta": MoPropertyMeta("drop_acl_delta", "dropAclDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "drop_acl_delta_avg": MoPropertyMeta("drop_acl_delta_avg", "dropAclDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "drop_acl_delta_max": MoPropertyMeta("drop_acl_delta_max", "dropAclDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "drop_acl_delta_min": MoPropertyMeta("drop_acl_delta_min", "dropAclDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "menlo_eth_index": MoPropertyMeta("menlo_eth_index", "menloEthIndex", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, None, None, None, None, ["0", "0_A", "0_B", "1", "1_A", "1_B", "unknown"], []), 
        "normalized_time_col": MoPropertyMeta("normalized_time_col", "normalizedTimeCol", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "pop_errors": MoPropertyMeta("pop_errors", "popErrors", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "pop_errors_delta": MoPropertyMeta("pop_errors_delta", "popErrorsDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "pop_errors_delta_avg": MoPropertyMeta("pop_errors_delta_avg", "popErrorsDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "pop_errors_delta_max": MoPropertyMeta("pop_errors_delta_max", "popErrorsDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "pop_errors_delta_min": MoPropertyMeta("pop_errors_delta_min", "popErrorsDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "push_errors": MoPropertyMeta("push_errors", "pushErrors", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "push_errors_delta": MoPropertyMeta("push_errors_delta", "pushErrorsDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "push_errors_delta_avg": MoPropertyMeta("push_errors_delta_avg", "pushErrorsDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "push_errors_delta_max": MoPropertyMeta("push_errors_delta_max", "pushErrorsDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "push_errors_delta_min": MoPropertyMeta("push_errors_delta_min", "pushErrorsDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "stats_reported": MoPropertyMeta("stats_reported", "statsReported", "int", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "uncorrectable_errors": MoPropertyMeta("uncorrectable_errors", "uncorrectableErrors", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "uncorrectable_errors_delta": MoPropertyMeta("uncorrectable_errors_delta", "uncorrectableErrorsDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "uncorrectable_errors_delta_avg": MoPropertyMeta("uncorrectable_errors_delta_avg", "uncorrectableErrorsDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "uncorrectable_errors_delta_max": MoPropertyMeta("uncorrectable_errors_delta_max", "uncorrectableErrorsDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "uncorrectable_errors_delta_min": MoPropertyMeta("uncorrectable_errors_delta_min", "uncorrectableErrorsDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "correctableErrors": "correctable_errors", 
        "correctableErrorsDelta": "correctable_errors_delta", 
        "correctableErrorsDeltaAvg": "correctable_errors_delta_avg", 
        "correctableErrorsDeltaMax": "correctable_errors_delta_max", 
        "correctableErrorsDeltaMin": "correctable_errors_delta_min", 
        "dn": "dn", 
        "dropAcl": "drop_acl", 
        "dropAclDelta": "drop_acl_delta", 
        "dropAclDeltaAvg": "drop_acl_delta_avg", 
        "dropAclDeltaMax": "drop_acl_delta_max", 
        "dropAclDeltaMin": "drop_acl_delta_min", 
        "intervals": "intervals", 
        "menloEthIndex": "menlo_eth_index", 
        "normalizedTimeCol": "normalized_time_col", 
        "popErrors": "pop_errors", 
        "popErrorsDelta": "pop_errors_delta", 
        "popErrorsDeltaAvg": "pop_errors_delta_avg", 
        "popErrorsDeltaMax": "pop_errors_delta_max", 
        "popErrorsDeltaMin": "pop_errors_delta_min", 
        "pushErrors": "push_errors", 
        "pushErrorsDelta": "push_errors_delta", 
        "pushErrorsDeltaAvg": "push_errors_delta_avg", 
        "pushErrorsDeltaMax": "push_errors_delta_max", 
        "pushErrorsDeltaMin": "push_errors_delta_min", 
        "rn": "rn", 
        "statsReported": "stats_reported", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "uncorrectableErrors": "uncorrectable_errors", 
        "uncorrectableErrorsDelta": "uncorrectable_errors_delta", 
        "uncorrectableErrorsDeltaAvg": "uncorrectable_errors_delta_avg", 
        "uncorrectableErrorsDeltaMax": "uncorrectable_errors_delta_max", 
        "uncorrectableErrorsDeltaMin": "uncorrectable_errors_delta_min", 
        "update": "update", 
    }

    def __init__(self, parent_mo_or_dn, menlo_eth_index, **kwargs):
        self._dirty_mask = 0
        self.menlo_eth_index = menlo_eth_index
        self.child_action = None
        self.correctable_errors = None
        self.correctable_errors_delta = None
        self.correctable_errors_delta_avg = None
        self.correctable_errors_delta_max = None
        self.correctable_errors_delta_min = None
        self.drop_acl = None
        self.drop_acl_delta = None
        self.drop_acl_delta_avg = None
        self.drop_acl_delta_max = None
        self.drop_acl_delta_min = None
        self.intervals = None
        self.normalized_time_col = None
        self.pop_errors = None
        self.pop_errors_delta = None
        self.pop_errors_delta_avg = None
        self.pop_errors_delta_max = None
        self.pop_errors_delta_min = None
        self.push_errors = None
        self.push_errors_delta = None
        self.push_errors_delta_avg = None
        self.push_errors_delta_max = None
        self.push_errors_delta_min = None
        self.stats_reported = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.uncorrectable_errors = None
        self.uncorrectable_errors_delta = None
        self.uncorrectable_errors_delta_avg = None
        self.uncorrectable_errors_delta_max = None
        self.uncorrectable_errors_delta_min = None
        self.update = None

        ManagedObject.__init__(self, "AdaptorMenloEthErrorStats", parent_mo_or_dn, **kwargs)

