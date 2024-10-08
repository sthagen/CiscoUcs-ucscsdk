"""This module contains the general information for EquipmentChassisAssocCtx ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EquipmentChassisAssocCtxConsts():
    pass


class EquipmentChassisAssocCtx(ManagedObject):
    """This is EquipmentChassisAssocCtx class."""

    consts = EquipmentChassisAssocCtxConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentChassisAssocCtx", "equipmentChassisAssocCtx", "cp-assoc-ctx", VersionMeta.Version151a, "InputOutput", 0xf, [], ["read-only"], ['equipmentChassisProfileAssocCtx'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "fru_cap_dn": MoPropertyMeta("fru_cap_dn", "fruCapDn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fruCapDn": "fru_cap_dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.fru_cap_dn = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentChassisAssocCtx", parent_mo_or_dn, **kwargs)

