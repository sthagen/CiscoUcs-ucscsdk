"""This module contains the general information for ComputeRackQual ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputeRackQualConsts():
    pass


class ComputeRackQual(ManagedObject):
    """This is ComputeRackQual class."""

    consts = ComputeRackQualConsts()
    naming_props = set(['minId', 'maxId'])

    mo_meta = MoMeta("ComputeRackQual", "computeRackQual", "rack-from-[min_id]-to-[max_id]", VersionMeta.Version111a, "InputOutput", 0x3f, [], ["admin", "pn-policy", "read-only"], ['computeDomainQual'], [], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "max_id": MoPropertyMeta("max_id", "maxId", "uint", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], ["1-255"]), 
        "min_id": MoPropertyMeta("min_id", "minId", "uint", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["1-255"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "maxId": "max_id", 
        "minId": "min_id", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, min_id, max_id, **kwargs):
        self._dirty_mask = 0
        self.min_id = min_id
        self.max_id = max_id
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "ComputeRackQual", parent_mo_or_dn, **kwargs)

