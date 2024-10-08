"""This module contains the general information for PowerGroup ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class PowerGroupConsts():
    ADMIN_COMMITTED_UNBOUNDED = "unbounded"
    ADMIN_PEAK_UNBOUNDED = "unbounded"
    CUR_REQ_POWER_UNBOUNDED = "unbounded"
    CURRENT_POWER_UNBOUNDED = "unbounded"
    INT_ID_NONE = "none"
    MIN_REQ_POWER_UNBOUNDED = "unbounded"
    OPER_COMMITTED_UNBOUNDED = "unbounded"
    OPER_PEAK_UNBOUNDED = "unbounded"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    REALLOC_CHASSIS = "chassis"
    REALLOC_NONE = "none"


class PowerGroup(ManagedObject):
    """This is PowerGroup class."""

    consts = PowerGroupConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("PowerGroup", "powerGroup", "group-[name]", VersionMeta.Version111a, "InputOutput", 0x3ff, [], ["admin", "ls-config", "ls-config-policy", "read-only"], ['powerEp'], ['powerChassisMember'], ["Get"])

    prop_meta = {
        "admin_committed": MoPropertyMeta("admin_committed", "adminCommitted", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]), 
        "admin_peak": MoPropertyMeta("admin_peak", "adminPeak", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "cur_req_power": MoPropertyMeta("cur_req_power", "curReqPower", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]), 
        "current_power": MoPropertyMeta("current_power", "currentPower", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "min_req_power": MoPropertyMeta("min_req_power", "minReqPower", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "oper_committed": MoPropertyMeta("oper_committed", "operCommitted", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]), 
        "oper_peak": MoPropertyMeta("oper_peak", "operPeak", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((cap-ok|defaultValue|cap-insufficient|cap-mismatch),){0,3}(cap-ok|defaultValue|cap-insufficient|cap-mismatch){0,1}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "qualifier": MoPropertyMeta("qualifier", "qualifier", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "realloc": MoPropertyMeta("realloc", "realloc", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["chassis", "none"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "adminCommitted": "admin_committed", 
        "adminPeak": "admin_peak", 
        "childAction": "child_action", 
        "curReqPower": "cur_req_power", 
        "currentPower": "current_power", 
        "descr": "descr", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "intId": "int_id", 
        "minReqPower": "min_req_power", 
        "name": "name", 
        "operCommitted": "oper_committed", 
        "operPeak": "oper_peak", 
        "operState": "oper_state", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "qualifier": "qualifier", 
        "realloc": "realloc", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.admin_committed = None
        self.admin_peak = None
        self.child_action = None
        self.cur_req_power = None
        self.current_power = None
        self.descr = None
        self.flt_aggr = None
        self.int_id = None
        self.min_req_power = None
        self.oper_committed = None
        self.oper_peak = None
        self.oper_state = None
        self.policy_level = None
        self.policy_owner = None
        self.qualifier = None
        self.realloc = None
        self.status = None

        ManagedObject.__init__(self, "PowerGroup", parent_mo_or_dn, **kwargs)

