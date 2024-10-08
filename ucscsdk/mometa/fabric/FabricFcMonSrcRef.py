"""This module contains the general information for FabricFcMonSrcRef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricFcMonSrcRefConsts():
    SOURCE_TYPE_PORT_CHANNEL = "port-channel"
    SOURCE_TYPE_STORAGE = "storage"
    SOURCE_TYPE_UPLINK_PORT = "uplink-port"
    SOURCE_TYPE_VHBA = "vhba"
    SOURCE_TYPE_VSAN = "vsan"


class FabricFcMonSrcRef(ManagedObject):
    """This is FabricFcMonSrcRef class."""

    consts = FabricFcMonSrcRefConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("FabricFcMonSrcRef", "fabricFcMonSrcRef", "src-ref-[id]", VersionMeta.Version151a, "InputOutput", 0x1f, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricFcMon'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "source_dn": MoPropertyMeta("source_dn", "sourceDn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "source_type": MoPropertyMeta("source_type", "sourceType", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["port-channel", "storage", "uplink-port", "vhba", "vsan"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "rn": "rn", 
        "sourceDn": "source_dn", 
        "sourceType": "source_type", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.source_dn = None
        self.source_type = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "FabricFcMonSrcRef", parent_mo_or_dn, **kwargs)

