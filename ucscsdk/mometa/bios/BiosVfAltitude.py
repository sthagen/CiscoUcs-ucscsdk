"""This module contains the general information for BiosVfAltitude ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosVfAltitudeConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_ALTITUDE_1500_M = "1500-m"
    VP_ALTITUDE_300_M = "300-m"
    VP_ALTITUDE_3000_M = "3000-m"
    VP_ALTITUDE_900_M = "900-m"
    VP_ALTITUDE_AUTO = "auto"
    VP_ALTITUDE_PLATFORM_DEFAULT = "platform-default"
    VP_ALTITUDE_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfAltitude(ManagedObject):
    """This is BiosVfAltitude class."""

    consts = BiosVfAltitudeConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfAltitude", "biosVfAltitude", "Altitude", VersionMeta.Version141a, "InputOutput", 0x1f, [], ["read-only"], ['biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_altitude": MoPropertyMeta("vp_altitude", "vpAltitude", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["1500-m", "300-m", "3000-m", "900-m", "auto", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpAltitude": "vp_altitude", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_altitude = None

        ManagedObject.__init__(self, "BiosVfAltitude", parent_mo_or_dn, **kwargs)

