"""This module contains the general information for ProcessorQual ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ProcessorQualConsts():
    ARCH_DUAL_CORE_OPTERON = "Dual-Core_Opteron"
    ARCH_INTEL_P4_C = "Intel_P4_C"
    ARCH_OPTERON = "Opteron"
    ARCH_PENTIUM_4 = "Pentium_4"
    ARCH_TURION_64 = "Turion_64"
    ARCH_XEON = "Xeon"
    ARCH_XEON_MP = "Xeon_MP"
    ARCH_ZEN = "Zen"
    ARCH_ANY = "any"
    MAX_CORES_UNSPECIFIED = "unspecified"
    MAX_PROCS_UNSPECIFIED = "unspecified"
    MAX_THREADS_UNSPECIFIED = "unspecified"
    MIN_CORES_UNSPECIFIED = "unspecified"
    MIN_PROCS_UNSPECIFIED = "unspecified"
    MIN_THREADS_UNSPECIFIED = "unspecified"
    SPEED_UNSPECIFIED = "unspecified"
    STEPPING_UNSPECIFIED = "unspecified"


class ProcessorQual(ManagedObject):
    """This is ProcessorQual class."""

    consts = ProcessorQualConsts()
    naming_props = set([])

    mo_meta = MoMeta("ProcessorQual", "processorQual", "cpu", VersionMeta.Version111a, "InputOutput", 0x3fff, [], ["admin", "pn-policy", "read-only"], ['computeQual'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "arch": MoPropertyMeta("arch", "arch", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Dual-Core_Opteron", "Intel_P4_C", "Opteron", "Pentium_4", "Turion_64", "Xeon", "Xeon_MP", "Zen", "any"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "max_cores": MoPropertyMeta("max_cores", "maxCores", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["unspecified"], ["0-65535"]), 
        "max_procs": MoPropertyMeta("max_procs", "maxProcs", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["unspecified"], ["0-65535"]), 
        "max_threads": MoPropertyMeta("max_threads", "maxThreads", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["unspecified"], ["0-65535"]), 
        "min_cores": MoPropertyMeta("min_cores", "minCores", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["unspecified"], ["0-65535"]), 
        "min_procs": MoPropertyMeta("min_procs", "minProcs", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["unspecified"], ["0-65535"]), 
        "min_threads": MoPropertyMeta("min_threads", "minThreads", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["unspecified"], ["0-65535"]), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""[ !#$%\(\)\*\+,\-\./:;\?@\[\\\]\^_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []), 
        "speed": MoPropertyMeta("speed", "speed", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "stepping": MoPropertyMeta("stepping", "stepping", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["unspecified"], ["0-4294967295"]), 
    }

    prop_map = {
        "arch": "arch", 
        "childAction": "child_action", 
        "dn": "dn", 
        "maxCores": "max_cores", 
        "maxProcs": "max_procs", 
        "maxThreads": "max_threads", 
        "minCores": "min_cores", 
        "minProcs": "min_procs", 
        "minThreads": "min_threads", 
        "model": "model", 
        "rn": "rn", 
        "speed": "speed", 
        "status": "status", 
        "stepping": "stepping", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.arch = None
        self.child_action = None
        self.max_cores = None
        self.max_procs = None
        self.max_threads = None
        self.min_cores = None
        self.min_procs = None
        self.min_threads = None
        self.model = None
        self.speed = None
        self.status = None
        self.stepping = None

        ManagedObject.__init__(self, "ProcessorQual", parent_mo_or_dn, **kwargs)

