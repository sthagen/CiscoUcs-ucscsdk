"""This module contains the general information for BiosVfLvDIMMSupport ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosVfLvDIMMSupportConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_LV_DDRMODE_AUTO = "auto"
    VP_LV_DDRMODE_PERFORMANCE_MODE = "performance-mode"
    VP_LV_DDRMODE_PLATFORM_DEFAULT = "platform-default"
    VP_LV_DDRMODE_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_LV_DDRMODE_POWER_SAVING_MODE = "power-saving-mode"


class BiosVfLvDIMMSupport(ManagedObject):
    """This is BiosVfLvDIMMSupport class."""

    consts = BiosVfLvDIMMSupportConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfLvDIMMSupport", "biosVfLvDIMMSupport", "LvDIMM-Support", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["read-only"], ['biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_lv_ddr_mode": MoPropertyMeta("vp_lv_ddr_mode", "vpLvDDRMode", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["auto", "performance-mode", "platform-default", "platform-recommended", "power-saving-mode"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpLvDDRMode": "vp_lv_ddr_mode", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_lv_ddr_mode = None

        ManagedObject.__init__(self, "BiosVfLvDIMMSupport", parent_mo_or_dn, **kwargs)

