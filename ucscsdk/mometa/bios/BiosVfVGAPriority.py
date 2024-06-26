"""This module contains the general information for BiosVfVGAPriority ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosVfVGAPriorityConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_VGAPRIORITY_OFFBOARD = "offboard"
    VP_VGAPRIORITY_ONBOARD = "onboard"
    VP_VGAPRIORITY_ONBOARD_VGA_DISABLED = "onboard-vga-disabled"
    VP_VGAPRIORITY_PLATFORM_DEFAULT = "platform-default"
    VP_VGAPRIORITY_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfVGAPriority(ManagedObject):
    """This is BiosVfVGAPriority class."""

    consts = BiosVfVGAPriorityConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfVGAPriority", "biosVfVGAPriority", "VGA-Priority", VersionMeta.Version121a, "InputOutput", 0x1f, [], ["read-only"], ['biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version121a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_vga_priority": MoPropertyMeta("vp_vga_priority", "vpVGAPriority", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["offboard", "onboard", "onboard-vga-disabled", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpVGAPriority": "vp_vga_priority", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_vga_priority = None

        ManagedObject.__init__(self, "BiosVfVGAPriority", parent_mo_or_dn, **kwargs)

