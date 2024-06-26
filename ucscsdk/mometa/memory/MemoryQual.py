"""This module contains the general information for MemoryQual ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class MemoryQualConsts():
    CLOCK_UNSPECIFIED = "unspecified"
    LATENCY_UNSPECIFIED = "unspecified"
    MAX_CAP_UNSPECIFIED = "unspecified"
    MIN_CAP_UNSPECIFIED = "unspecified"
    SPEED_UNSPECIFIED = "unspecified"
    UNITS_UNSPECIFIED = "unspecified"
    WIDTH_UNSPECIFIED = "unspecified"


class MemoryQual(ManagedObject):
    """This is MemoryQual class."""

    consts = MemoryQualConsts()
    naming_props = set([])

    mo_meta = MoMeta("MemoryQual", "memoryQual", "memory", VersionMeta.Version111a, "InputOutput", 0x7ff, [], ["admin", "pn-policy", "read-only"], ['computeQual'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "clock": MoPropertyMeta("clock", "clock", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "latency": MoPropertyMeta("latency", "latency", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "max_cap": MoPropertyMeta("max_cap", "maxCap", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "min_cap": MoPropertyMeta("min_cap", "minCap", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "speed": MoPropertyMeta("speed", "speed", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "units": MoPropertyMeta("units", "units", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "width": MoPropertyMeta("width", "width", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["unspecified"], ["0-4294967295"]), 
    }

    prop_map = {
        "childAction": "child_action", 
        "clock": "clock", 
        "dn": "dn", 
        "latency": "latency", 
        "maxCap": "max_cap", 
        "minCap": "min_cap", 
        "rn": "rn", 
        "speed": "speed", 
        "status": "status", 
        "units": "units", 
        "width": "width", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.clock = None
        self.latency = None
        self.max_cap = None
        self.min_cap = None
        self.speed = None
        self.status = None
        self.units = None
        self.width = None

        ManagedObject.__init__(self, "MemoryQual", parent_mo_or_dn, **kwargs)

