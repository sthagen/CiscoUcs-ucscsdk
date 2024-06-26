"""This module contains the general information for FabricVCon ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricVConConsts():
    FABRIC_A = "A"
    FABRIC_B = "B"
    FABRIC_NONE = "NONE"
    FABRIC_ANY = "any"
    FABRIC_MGMT = "mgmt"
    ID_1 = "1"
    ID_2 = "2"
    ID_3 = "3"
    ID_4 = "4"
    INST_TYPE_AUTO = "auto"
    INST_TYPE_MANUAL = "manual"
    INST_TYPE_POLICY = "policy"
    PLACEMENT_AUTO = "auto"
    PLACEMENT_PHYSICAL = "physical"
    SELECT_ALL = "all"
    SELECT_ASSIGNED_ONLY = "assigned-only"
    SELECT_DYNAMIC_ONLY = "dynamic-only"
    SELECT_EXCLUDE_DYNAMIC = "exclude-dynamic"
    SELECT_EXCLUDE_UNASSIGNED = "exclude-unassigned"
    SELECT_EXCLUDE_USNIC = "exclude-usnic"
    SELECT_UNASSIGNED_ONLY = "unassigned-only"
    SELECT_USNIC_ONLY = "usnic-only"
    SHARE_DIFFERENT_TRANSPORT = "different-transport"
    SHARE_EXCLUSIVE_ONLY = "exclusive-only"
    SHARE_EXCLUSIVE_PREFERRED = "exclusive-preferred"
    SHARE_SAME_TRANSPORT = "same-transport"
    SHARE_SHARED = "shared"


class FabricVCon(ManagedObject):
    """This is FabricVCon class."""

    consts = FabricVConConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("FabricVCon", "fabricVCon", "vcon-[id]", VersionMeta.Version111a, "InputOutput", 0x7ff, [], ["admin", "ext-lan-policy", "ls-network", "ls-network-policy", "ls-server-policy", "ls-storage-policy"], ['fabricVConProfile', 'lsServer'], [], ["Add", "Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "equipment_dn": MoPropertyMeta("equipment_dn", "equipmentDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "fabric": MoPropertyMeta("fabric", "fabric", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["A", "B", "NONE", "any", "mgmt"], []), 
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x8, None, None, None, ["1", "2", "3", "4"], []), 
        "inst_type": MoPropertyMeta("inst_type", "instType", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["auto", "manual", "policy"], []), 
        "placement": MoPropertyMeta("placement", "placement", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["auto", "physical"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "select": MoPropertyMeta("select", "select", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["all", "assigned-only", "dynamic-only", "exclude-dynamic", "exclude-unassigned", "exclude-usnic", "unassigned-only", "usnic-only"], []), 
        "share": MoPropertyMeta("share", "share", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["different-transport", "exclusive-only", "exclusive-preferred", "same-transport", "shared"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((fc|ethernet|defaultValue),){0,2}(fc|ethernet|defaultValue){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "equipmentDn": "equipment_dn", 
        "fabric": "fabric", 
        "id": "id", 
        "instType": "inst_type", 
        "placement": "placement", 
        "rn": "rn", 
        "select": "select", 
        "share": "share", 
        "status": "status", 
        "transport": "transport", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.equipment_dn = None
        self.fabric = None
        self.inst_type = None
        self.placement = None
        self.select = None
        self.share = None
        self.status = None
        self.transport = None

        ManagedObject.__init__(self, "FabricVCon", parent_mo_or_dn, **kwargs)

