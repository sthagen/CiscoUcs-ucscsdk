"""This module contains the general information for QosclassEthClassified ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class QosclassEthClassifiedConsts():
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    BW_PERCENT_NOT_APPLICABLE = "not-applicable"
    COS_ANY = "any"
    DROP_DROP = "drop"
    DROP_NO_DROP = "no-drop"
    MTU_FC = "fc"
    MTU_NORMAL = "normal"
    MULTICAST_OPTIMIZE_FALSE = "false"
    MULTICAST_OPTIMIZE_NO = "no"
    MULTICAST_OPTIMIZE_TRUE = "true"
    MULTICAST_OPTIMIZE_YES = "yes"
    PRIORITY_BEST_EFFORT = "best-effort"
    PRIORITY_BRONZE = "bronze"
    PRIORITY_FC = "fc"
    PRIORITY_GOLD = "gold"
    PRIORITY_PLATINUM = "platinum"
    PRIORITY_SILVER = "silver"
    WEIGHT_BEST_EFFORT = "best-effort"
    WEIGHT_NONE = "none"


class QosclassEthClassified(ManagedObject):
    """This is QosclassEthClassified class."""

    consts = QosclassEthClassifiedConsts()
    naming_props = set(['priority'])

    mo_meta = MoMeta("QosclassEthClassified", "qosclassEthClassified", "class-[priority]", VersionMeta.Version141a, "InputOutput", 0xfff, [], ["admin", "ext-lan-qos", "ext-san-qos", "ls-network", "ls-network-policy", "ls-qos-policy"], ['qosclassDefinition', 'qosclassPolicy'], [], ["Get", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []), 
        "bw_percent": MoPropertyMeta("bw_percent", "bwPercent", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-100"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "cos": MoPropertyMeta("cos", "cos", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["any"], ["0-6", "255-255"]), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "drop": MoPropertyMeta("drop", "drop", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["drop", "no-drop"], []), 
        "mtu": MoPropertyMeta("mtu", "mtu", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["fc", "normal"], ["0-4294967295"]), 
        "multicast_optimize": MoPropertyMeta("multicast_optimize", "multicastOptimize", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["false", "no", "true", "yes"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "priority": MoPropertyMeta("priority", "priority", "string", VersionMeta.Version141a, MoPropertyMeta.NAMING, 0x100, None, None, None, ["best-effort", "bronze", "fc", "gold", "platinum", "silver"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "weight": MoPropertyMeta("weight", "weight", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["best-effort", "none"], ["0-10"]), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "bwPercent": "bw_percent", 
        "childAction": "child_action", 
        "cos": "cos", 
        "dn": "dn", 
        "drop": "drop", 
        "mtu": "mtu", 
        "multicastOptimize": "multicast_optimize", 
        "name": "name", 
        "priority": "priority", 
        "rn": "rn", 
        "status": "status", 
        "weight": "weight", 
    }

    def __init__(self, parent_mo_or_dn, priority, **kwargs):
        self._dirty_mask = 0
        self.priority = priority
        self.admin_state = None
        self.bw_percent = None
        self.child_action = None
        self.cos = None
        self.drop = None
        self.mtu = None
        self.multicast_optimize = None
        self.name = None
        self.status = None
        self.weight = None

        ManagedObject.__init__(self, "QosclassEthClassified", parent_mo_or_dn, **kwargs)

