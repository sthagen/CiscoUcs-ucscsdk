"""This module contains the general information for DomainStorageParam ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class DomainStorageParamConsts():
    pass


class DomainStorageParam(ManagedObject):
    """This is DomainStorageParam class."""

    consts = DomainStorageParamConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("DomainStorageParam", "domainStorageParam", "storage-param-[name]", VersionMeta.Version112a, "InputOutput", 0x3f, [], ["admin"], ['domainChassisFeature', 'domainEnvironmentFeature', 'domainFeatureCatalog', 'domainNetworkFeature', 'domainServerFeature', 'domainStorageFeature', 'featureChassisDef', 'featureEnvDef', 'featureNetworkDef', 'featureServerDef', 'featureStorageDef'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version112a, MoPropertyMeta.NAMING, 0x4, 1, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "value": MoPropertyMeta("value", "value", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "name": "name", 
        "rn": "rn", 
        "status": "status", 
        "value": "value", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.flt_aggr = None
        self.status = None
        self.value = None

        ManagedObject.__init__(self, "DomainStorageParam", parent_mo_or_dn, **kwargs)

