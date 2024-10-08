"""This module contains the general information for HcCatalogList ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class HcCatalogListConsts():
    REFRESH_FALSE = "false"
    REFRESH_NO = "no"
    REFRESH_TRUE = "true"
    REFRESH_YES = "yes"


class HcCatalogList(ManagedObject):
    """This is HcCatalogList class."""

    consts = HcCatalogListConsts()
    naming_props = set([])

    mo_meta = MoMeta("HcCatalogList", "hcCatalogList", "catalog-list", VersionMeta.Version151a, "InputOutput", 0x1f, [], ["admin"], ['hcHolder'], ['hcCatalogSource'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "refresh": MoPropertyMeta("refresh", "refresh", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "refresh": "refresh", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.flt_aggr = None
        self.refresh = None
        self.status = None

        ManagedObject.__init__(self, "HcCatalogList", parent_mo_or_dn, **kwargs)

