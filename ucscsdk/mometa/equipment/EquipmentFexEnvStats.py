"""This module contains the general information for EquipmentFexEnvStats ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EquipmentFexEnvStatsConsts():
    DIE1_N_A = "N/A"
    DIE1_AVG_N_A = "N/A"
    DIE1_MAX_N_A = "N/A"
    DIE1_MIN_N_A = "N/A"
    INLET_N_A = "N/A"
    INLET1_N_A = "N/A"
    INLET1_AVG_N_A = "N/A"
    INLET1_MAX_N_A = "N/A"
    INLET1_MIN_N_A = "N/A"
    INLET_AVG_N_A = "N/A"
    INLET_MAX_N_A = "N/A"
    INLET_MIN_N_A = "N/A"
    OUTLET1_N_A = "N/A"
    OUTLET1_AVG_N_A = "N/A"
    OUTLET1_MAX_N_A = "N/A"
    OUTLET1_MIN_N_A = "N/A"
    OUTLET2_N_A = "N/A"
    OUTLET2_AVG_N_A = "N/A"
    OUTLET2_MAX_N_A = "N/A"
    OUTLET2_MIN_N_A = "N/A"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class EquipmentFexEnvStats(ManagedObject):
    """This is EquipmentFexEnvStats class."""

    consts = EquipmentFexEnvStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentFexEnvStats", "equipmentFexEnvStats", "env-stats", VersionMeta.Version111a, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['equipmentFex'], ['equipmentFexEnvStatsHist'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "die1": MoPropertyMeta("die1", "die1", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-4294967295"]), 
        "die1_avg": MoPropertyMeta("die1_avg", "die1Avg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-4294967295"]), 
        "die1_max": MoPropertyMeta("die1_max", "die1Max", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-4294967295"]), 
        "die1_min": MoPropertyMeta("die1_min", "die1Min", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-4294967295"]), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "inlet": MoPropertyMeta("inlet", "inlet", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-4294967295"]), 
        "inlet1": MoPropertyMeta("inlet1", "inlet1", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-4294967295"]), 
        "inlet1_avg": MoPropertyMeta("inlet1_avg", "inlet1Avg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-4294967295"]), 
        "inlet1_max": MoPropertyMeta("inlet1_max", "inlet1Max", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-4294967295"]), 
        "inlet1_min": MoPropertyMeta("inlet1_min", "inlet1Min", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-4294967295"]), 
        "inlet_avg": MoPropertyMeta("inlet_avg", "inletAvg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-4294967295"]), 
        "inlet_max": MoPropertyMeta("inlet_max", "inletMax", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-4294967295"]), 
        "inlet_min": MoPropertyMeta("inlet_min", "inletMin", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-4294967295"]), 
        "input_status": MoPropertyMeta("input_status", "inputStatus", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "normalized_time_col": MoPropertyMeta("normalized_time_col", "normalizedTimeCol", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "outlet1": MoPropertyMeta("outlet1", "outlet1", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-4294967295"]), 
        "outlet1_avg": MoPropertyMeta("outlet1_avg", "outlet1Avg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-4294967295"]), 
        "outlet1_max": MoPropertyMeta("outlet1_max", "outlet1Max", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-4294967295"]), 
        "outlet1_min": MoPropertyMeta("outlet1_min", "outlet1Min", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-4294967295"]), 
        "outlet2": MoPropertyMeta("outlet2", "outlet2", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-4294967295"]), 
        "outlet2_avg": MoPropertyMeta("outlet2_avg", "outlet2Avg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-4294967295"]), 
        "outlet2_max": MoPropertyMeta("outlet2_max", "outlet2Max", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-4294967295"]), 
        "outlet2_min": MoPropertyMeta("outlet2_min", "outlet2Min", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-4294967295"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "stats_reported": MoPropertyMeta("stats_reported", "statsReported", "int", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "die1": "die1", 
        "die1Avg": "die1_avg", 
        "die1Max": "die1_max", 
        "die1Min": "die1_min", 
        "dn": "dn", 
        "inlet": "inlet", 
        "inlet1": "inlet1", 
        "inlet1Avg": "inlet1_avg", 
        "inlet1Max": "inlet1_max", 
        "inlet1Min": "inlet1_min", 
        "inletAvg": "inlet_avg", 
        "inletMax": "inlet_max", 
        "inletMin": "inlet_min", 
        "inputStatus": "input_status", 
        "intervals": "intervals", 
        "normalizedTimeCol": "normalized_time_col", 
        "outlet1": "outlet1", 
        "outlet1Avg": "outlet1_avg", 
        "outlet1Max": "outlet1_max", 
        "outlet1Min": "outlet1_min", 
        "outlet2": "outlet2", 
        "outlet2Avg": "outlet2_avg", 
        "outlet2Max": "outlet2_max", 
        "outlet2Min": "outlet2_min", 
        "rn": "rn", 
        "statsReported": "stats_reported", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "update": "update", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.die1 = None
        self.die1_avg = None
        self.die1_max = None
        self.die1_min = None
        self.inlet = None
        self.inlet1 = None
        self.inlet1_avg = None
        self.inlet1_max = None
        self.inlet1_min = None
        self.inlet_avg = None
        self.inlet_max = None
        self.inlet_min = None
        self.input_status = None
        self.intervals = None
        self.normalized_time_col = None
        self.outlet1 = None
        self.outlet1_avg = None
        self.outlet1_max = None
        self.outlet1_min = None
        self.outlet2 = None
        self.outlet2_avg = None
        self.outlet2_max = None
        self.outlet2_min = None
        self.stats_reported = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "EquipmentFexEnvStats", parent_mo_or_dn, **kwargs)

