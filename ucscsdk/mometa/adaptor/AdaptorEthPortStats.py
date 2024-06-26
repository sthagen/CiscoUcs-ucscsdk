"""This module contains the general information for AdaptorEthPortStats ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AdaptorEthPortStatsConsts():
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"
    TRAFFIC_DIRECTION_RX = "rx"
    TRAFFIC_DIRECTION_TX = "tx"
    TRAFFIC_DIRECTION_UNKNOWN = "unknown"


class AdaptorEthPortStats(ManagedObject):
    """This is AdaptorEthPortStats class."""

    consts = AdaptorEthPortStatsConsts()
    naming_props = set(['trafficDirection'])

    mo_meta = MoMeta("AdaptorEthPortStats", "adaptorEthPortStats", "eth-port-stats-[traffic_direction]", VersionMeta.Version111a, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['adaptorHostEthIf', 'vmNic'], ['adaptorEthPortStatsHist'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "good_packets": MoPropertyMeta("good_packets", "goodPackets", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "good_packets_delta": MoPropertyMeta("good_packets_delta", "goodPacketsDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "good_packets_delta_avg": MoPropertyMeta("good_packets_delta_avg", "goodPacketsDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "good_packets_delta_max": MoPropertyMeta("good_packets_delta_max", "goodPacketsDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "good_packets_delta_min": MoPropertyMeta("good_packets_delta_min", "goodPacketsDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "normalized_time_col": MoPropertyMeta("normalized_time_col", "normalizedTimeCol", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "pause_packets": MoPropertyMeta("pause_packets", "pausePackets", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "pause_packets_delta": MoPropertyMeta("pause_packets_delta", "pausePacketsDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "pause_packets_delta_avg": MoPropertyMeta("pause_packets_delta_avg", "pausePacketsDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "pause_packets_delta_max": MoPropertyMeta("pause_packets_delta_max", "pausePacketsDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "pause_packets_delta_min": MoPropertyMeta("pause_packets_delta_min", "pausePacketsDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "per_priority_pause_packets": MoPropertyMeta("per_priority_pause_packets", "perPriorityPausePackets", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "per_priority_pause_packets_delta": MoPropertyMeta("per_priority_pause_packets_delta", "perPriorityPausePacketsDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "per_priority_pause_packets_delta_avg": MoPropertyMeta("per_priority_pause_packets_delta_avg", "perPriorityPausePacketsDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "per_priority_pause_packets_delta_max": MoPropertyMeta("per_priority_pause_packets_delta_max", "perPriorityPausePacketsDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "per_priority_pause_packets_delta_min": MoPropertyMeta("per_priority_pause_packets_delta_min", "perPriorityPausePacketsDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "ppp_packets": MoPropertyMeta("ppp_packets", "pppPackets", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "ppp_packets_delta": MoPropertyMeta("ppp_packets_delta", "pppPacketsDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "ppp_packets_delta_avg": MoPropertyMeta("ppp_packets_delta_avg", "pppPacketsDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "ppp_packets_delta_max": MoPropertyMeta("ppp_packets_delta_max", "pppPacketsDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "ppp_packets_delta_min": MoPropertyMeta("ppp_packets_delta_min", "pppPacketsDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "stats_reported": MoPropertyMeta("stats_reported", "statsReported", "int", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "total_packets": MoPropertyMeta("total_packets", "totalPackets", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "total_packets_delta": MoPropertyMeta("total_packets_delta", "totalPacketsDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "total_packets_delta_avg": MoPropertyMeta("total_packets_delta_avg", "totalPacketsDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "total_packets_delta_max": MoPropertyMeta("total_packets_delta_max", "totalPacketsDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "total_packets_delta_min": MoPropertyMeta("total_packets_delta_min", "totalPacketsDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "traffic_direction": MoPropertyMeta("traffic_direction", "trafficDirection", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, None, None, None, None, ["rx", "tx", "unknown"], []), 
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "vlan_packets": MoPropertyMeta("vlan_packets", "vlanPackets", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "vlan_packets_delta": MoPropertyMeta("vlan_packets_delta", "vlanPacketsDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "vlan_packets_delta_avg": MoPropertyMeta("vlan_packets_delta_avg", "vlanPacketsDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "vlan_packets_delta_max": MoPropertyMeta("vlan_packets_delta_max", "vlanPacketsDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "vlan_packets_delta_min": MoPropertyMeta("vlan_packets_delta_min", "vlanPacketsDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "goodPackets": "good_packets", 
        "goodPacketsDelta": "good_packets_delta", 
        "goodPacketsDeltaAvg": "good_packets_delta_avg", 
        "goodPacketsDeltaMax": "good_packets_delta_max", 
        "goodPacketsDeltaMin": "good_packets_delta_min", 
        "intervals": "intervals", 
        "normalizedTimeCol": "normalized_time_col", 
        "pausePackets": "pause_packets", 
        "pausePacketsDelta": "pause_packets_delta", 
        "pausePacketsDeltaAvg": "pause_packets_delta_avg", 
        "pausePacketsDeltaMax": "pause_packets_delta_max", 
        "pausePacketsDeltaMin": "pause_packets_delta_min", 
        "perPriorityPausePackets": "per_priority_pause_packets", 
        "perPriorityPausePacketsDelta": "per_priority_pause_packets_delta", 
        "perPriorityPausePacketsDeltaAvg": "per_priority_pause_packets_delta_avg", 
        "perPriorityPausePacketsDeltaMax": "per_priority_pause_packets_delta_max", 
        "perPriorityPausePacketsDeltaMin": "per_priority_pause_packets_delta_min", 
        "pppPackets": "ppp_packets", 
        "pppPacketsDelta": "ppp_packets_delta", 
        "pppPacketsDeltaAvg": "ppp_packets_delta_avg", 
        "pppPacketsDeltaMax": "ppp_packets_delta_max", 
        "pppPacketsDeltaMin": "ppp_packets_delta_min", 
        "rn": "rn", 
        "statsReported": "stats_reported", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "totalPackets": "total_packets", 
        "totalPacketsDelta": "total_packets_delta", 
        "totalPacketsDeltaAvg": "total_packets_delta_avg", 
        "totalPacketsDeltaMax": "total_packets_delta_max", 
        "totalPacketsDeltaMin": "total_packets_delta_min", 
        "trafficDirection": "traffic_direction", 
        "update": "update", 
        "vlanPackets": "vlan_packets", 
        "vlanPacketsDelta": "vlan_packets_delta", 
        "vlanPacketsDeltaAvg": "vlan_packets_delta_avg", 
        "vlanPacketsDeltaMax": "vlan_packets_delta_max", 
        "vlanPacketsDeltaMin": "vlan_packets_delta_min", 
    }

    def __init__(self, parent_mo_or_dn, traffic_direction, **kwargs):
        self._dirty_mask = 0
        self.traffic_direction = traffic_direction
        self.child_action = None
        self.good_packets = None
        self.good_packets_delta = None
        self.good_packets_delta_avg = None
        self.good_packets_delta_max = None
        self.good_packets_delta_min = None
        self.intervals = None
        self.normalized_time_col = None
        self.pause_packets = None
        self.pause_packets_delta = None
        self.pause_packets_delta_avg = None
        self.pause_packets_delta_max = None
        self.pause_packets_delta_min = None
        self.per_priority_pause_packets = None
        self.per_priority_pause_packets_delta = None
        self.per_priority_pause_packets_delta_avg = None
        self.per_priority_pause_packets_delta_max = None
        self.per_priority_pause_packets_delta_min = None
        self.ppp_packets = None
        self.ppp_packets_delta = None
        self.ppp_packets_delta_avg = None
        self.ppp_packets_delta_max = None
        self.ppp_packets_delta_min = None
        self.stats_reported = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.total_packets = None
        self.total_packets_delta = None
        self.total_packets_delta_avg = None
        self.total_packets_delta_max = None
        self.total_packets_delta_min = None
        self.update = None
        self.vlan_packets = None
        self.vlan_packets_delta = None
        self.vlan_packets_delta_avg = None
        self.vlan_packets_delta_max = None
        self.vlan_packets_delta_min = None

        ManagedObject.__init__(self, "AdaptorEthPortStats", parent_mo_or_dn, **kwargs)

