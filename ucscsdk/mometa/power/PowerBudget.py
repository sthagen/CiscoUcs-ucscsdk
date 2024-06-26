"""This module contains the general information for PowerBudget ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class PowerBudgetConsts():
    ADMIN_COMMITTED_UNBOUNDED = "unbounded"
    ADMIN_FPLOCK_STATE_LOCKED = "locked"
    ADMIN_FPLOCK_STATE_UNKNOWN = "unknown"
    ADMIN_FPLOCK_STATE_UNLOCKED = "unlocked"
    ADMIN_PEAK_UNBOUNDED = "unbounded"
    ADMIN_PEAK_NEW_UNBOUNDED = "unbounded"
    BOOT_POWER_UNBOUNDED = "unbounded"
    CAP_ACTION_CLOCK_DOWN = "clock-down"
    CAP_ACTION_NOTHING = "nothing"
    CAP_ACTION_THROTTLED = "throttled"
    CATALOG_POWER_UNBOUNDED = "unbounded"
    CH_RSRVD_POWER_UNBOUNDED = "unbounded"
    CURRENT_POWER_UNBOUNDED = "unbounded"
    DYN_REALLOC_CHASSIS = "chassis"
    DYN_REALLOC_NONE = "none"
    IDLE_POWER_UNBOUNDED = "unbounded"
    MAX_POWER_UNBOUNDED = "unbounded"
    MIN_POWER_UNBOUNDED = "unbounded"
    OPER_COMMITTED_UNBOUNDED = "unbounded"
    OPER_FPLOCK_STATE_LOCKED = "locked"
    OPER_FPLOCK_STATE_UNKNOWN = "unknown"
    OPER_FPLOCK_STATE_UNLOCKED = "unlocked"
    OPER_MIN_UNBOUNDED = "unbounded"
    OPER_PEAK_UNBOUNDED = "unbounded"
    OPER_PROF_METHOD_DEFAULT = "default"
    OPER_PROF_METHOD_NODEMGR = "nodemgr"
    OPER_PROF_METHOD_PNUOS = "pnuos"
    OPER_PROF_METHOD_STATIC = "static"
    OPER_PROF_METHOD_UNKNOWN = "unknown"
    OPER_STATE_BUDGETED = "budgeted"
    OPER_STATE_BUDGETING = "budgeting"
    OPER_STATE_DEPLOYED = "deployed"
    OPER_STATE_DEPLOYING = "deploying"
    OPER_STATE_DISCOVERY_BUDGETED = "discovery-budgeted"
    OPER_STATE_DISCOVERY_RETRY = "discovery-retry"
    OPER_STATE_FIRMWARE_MISMATCH = "firmware-mismatch"
    OPER_STATE_NON_COMPLIANT = "non-compliant"
    OPER_STATE_NOT_CAPPED = "not-capped"
    OPER_STATE_UNBUDGETED = "unbudgeted"
    POWER_AVAIL_STATE_AVAILABLE = "available"
    POWER_AVAIL_STATE_UNAVAILABLE = "unavailable"
    POWER_AVAIL_STATE_UNKNOWN = "unknown"
    POWER_ON_DEPLOY_FALSE = "false"
    POWER_ON_DEPLOY_NO = "no"
    POWER_ON_DEPLOY_TRUE = "true"
    POWER_ON_DEPLOY_YES = "yes"
    PRIO_NO_CAP = "no-cap"
    PRIO_UTILITY = "utility"
    PROF_METHOD_DEFAULT = "default"
    PROF_METHOD_NODEMGR = "nodemgr"
    PROF_METHOD_PNUOS = "pnuos"
    PROF_METHOD_STATIC = "static"
    PROF_METHOD_UNKNOWN = "unknown"
    PROFILING_FALSE = "false"
    PROFILING_NO = "no"
    PROFILING_TRUE = "true"
    PROFILING_YES = "yes"
    PSU_LINE_MODE_HIGH_LINE = "high-line"
    PSU_LINE_MODE_LOW_LINE = "low-line"
    PSU_LINE_MODE_MIXED_LINE = "mixed-line"
    PSU_LINE_MODE_UNDETERMINED = "undetermined"
    PSU_LINE_MODE_UNKNOWN = "unknown"
    PSU_STATE_INSUFFICIENT = "insufficient"
    PSU_STATE_OK = "ok"
    STYLE_INTELLIGENT_POLICY_DRIVEN = "intelligent-policy-driven"
    STYLE_MANUAL_PER_BLADE = "manual-per-blade"


class PowerBudget(ManagedObject):
    """This is PowerBudget class."""

    consts = PowerBudgetConsts()
    naming_props = set([])

    mo_meta = MoMeta("PowerBudget", "powerBudget", "budget", VersionMeta.Version131a, "InputOutput", 0x3f, [], ["admin", "power-mgmt"], ['computeExtBoard', 'storageBlade'], ['powerProfiledPower'], ["Get", "Set"])

    prop_meta = {
        "admin_committed": MoPropertyMeta("admin_committed", "adminCommitted", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]), 
        "admin_fp_lock_state": MoPropertyMeta("admin_fp_lock_state", "adminFPLockState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["locked", "unknown", "unlocked"], []), 
        "admin_peak": MoPropertyMeta("admin_peak", "adminPeak", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]), 
        "admin_peak_new": MoPropertyMeta("admin_peak_new", "adminPeakNew", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]), 
        "boot_power": MoPropertyMeta("boot_power", "bootPower", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]), 
        "cap_action": MoPropertyMeta("cap_action", "capAction", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["clock-down", "nothing", "throttled"], []), 
        "catalog_power": MoPropertyMeta("catalog_power", "catalogPower", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]), 
        "ch_rsrvd_power": MoPropertyMeta("ch_rsrvd_power", "chRsrvdPower", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "current_power": MoPropertyMeta("current_power", "currentPower", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "dyn_realloc": MoPropertyMeta("dyn_realloc", "dynRealloc", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["chassis", "none"], []), 
        "group_name": MoPropertyMeta("group_name", "groupName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "idle_power": MoPropertyMeta("idle_power", "idlePower", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]), 
        "max_power": MoPropertyMeta("max_power", "maxPower", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]), 
        "min_power": MoPropertyMeta("min_power", "minPower", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]), 
        "oper_committed": MoPropertyMeta("oper_committed", "operCommitted", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]), 
        "oper_fp_lock_state": MoPropertyMeta("oper_fp_lock_state", "operFPLockState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["locked", "unknown", "unlocked"], []), 
        "oper_min": MoPropertyMeta("oper_min", "operMin", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]), 
        "oper_peak": MoPropertyMeta("oper_peak", "operPeak", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]), 
        "oper_prof_method": MoPropertyMeta("oper_prof_method", "operProfMethod", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["default", "nodemgr", "pnuos", "static", "unknown"], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["budgeted", "budgeting", "deployed", "deploying", "discovery-budgeted", "discovery-retry", "firmware-mismatch", "non-compliant", "not-capped", "unbudgeted"], []), 
        "power_avail_state": MoPropertyMeta("power_avail_state", "powerAvailState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["available", "unavailable", "unknown"], []), 
        "power_on_deploy": MoPropertyMeta("power_on_deploy", "powerOnDeploy", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "prio": MoPropertyMeta("prio", "prio", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no-cap", "utility"], ["1-10"]), 
        "prof_method": MoPropertyMeta("prof_method", "profMethod", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["default", "nodemgr", "pnuos", "static", "unknown"], []), 
        "profiling": MoPropertyMeta("profiling", "profiling", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "psu_capacity": MoPropertyMeta("psu_capacity", "psuCapacity", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-20000"]), 
        "psu_line_mode": MoPropertyMeta("psu_line_mode", "psuLineMode", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["high-line", "low-line", "mixed-line", "undetermined", "unknown"], []), 
        "psu_state": MoPropertyMeta("psu_state", "psuState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["insufficient", "ok"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "scaled_wt": MoPropertyMeta("scaled_wt", "scaledWt", "byte", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-200"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "style": MoPropertyMeta("style", "style", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["intelligent-policy-driven", "manual-per-blade"], []), 
        "update_time": MoPropertyMeta("update_time", "updateTime", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "weight": MoPropertyMeta("weight", "weight", "byte", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-200"]), 
    }

    prop_map = {
        "adminCommitted": "admin_committed", 
        "adminFPLockState": "admin_fp_lock_state", 
        "adminPeak": "admin_peak", 
        "adminPeakNew": "admin_peak_new", 
        "bootPower": "boot_power", 
        "capAction": "cap_action", 
        "catalogPower": "catalog_power", 
        "chRsrvdPower": "ch_rsrvd_power", 
        "childAction": "child_action", 
        "currentPower": "current_power", 
        "dn": "dn", 
        "dynRealloc": "dyn_realloc", 
        "groupName": "group_name", 
        "idlePower": "idle_power", 
        "maxPower": "max_power", 
        "minPower": "min_power", 
        "operCommitted": "oper_committed", 
        "operFPLockState": "oper_fp_lock_state", 
        "operMin": "oper_min", 
        "operPeak": "oper_peak", 
        "operProfMethod": "oper_prof_method", 
        "operState": "oper_state", 
        "powerAvailState": "power_avail_state", 
        "powerOnDeploy": "power_on_deploy", 
        "prio": "prio", 
        "profMethod": "prof_method", 
        "profiling": "profiling", 
        "psuCapacity": "psu_capacity", 
        "psuLineMode": "psu_line_mode", 
        "psuState": "psu_state", 
        "rn": "rn", 
        "scaledWt": "scaled_wt", 
        "status": "status", 
        "style": "style", 
        "updateTime": "update_time", 
        "weight": "weight", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_committed = None
        self.admin_fp_lock_state = None
        self.admin_peak = None
        self.admin_peak_new = None
        self.boot_power = None
        self.cap_action = None
        self.catalog_power = None
        self.ch_rsrvd_power = None
        self.child_action = None
        self.current_power = None
        self.dyn_realloc = None
        self.group_name = None
        self.idle_power = None
        self.max_power = None
        self.min_power = None
        self.oper_committed = None
        self.oper_fp_lock_state = None
        self.oper_min = None
        self.oper_peak = None
        self.oper_prof_method = None
        self.oper_state = None
        self.power_avail_state = None
        self.power_on_deploy = None
        self.prio = None
        self.prof_method = None
        self.profiling = None
        self.psu_capacity = None
        self.psu_line_mode = None
        self.psu_state = None
        self.scaled_wt = None
        self.status = None
        self.style = None
        self.update_time = None
        self.weight = None

        ManagedObject.__init__(self, "PowerBudget", parent_mo_or_dn, **kwargs)

