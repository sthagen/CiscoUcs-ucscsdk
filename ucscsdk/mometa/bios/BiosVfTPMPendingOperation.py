"""This module contains the general information for BiosVfTPMPendingOperation ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosVfTPMPendingOperationConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_TPMPENDING_OPERATION_NONE = "none"
    VP_TPMPENDING_OPERATION_PLATFORM_DEFAULT = "platform-default"
    VP_TPMPENDING_OPERATION_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_TPMPENDING_OPERATION_TPMCLEAR = "tpmclear"
    VP_TPMPENDING_OPERATION_TPMPPIOOWNEROFF = "tpmppioowneroff"
    VP_TPMPENDING_OPERATION_TPMPPIOOWNERON = "tpmppioowneron"


class BiosVfTPMPendingOperation(ManagedObject):
    """This is BiosVfTPMPendingOperation class."""

    consts = BiosVfTPMPendingOperationConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfTPMPendingOperation", "biosVfTPMPendingOperation", "TPM-Pending-Operation", VersionMeta.Version141a, "InputOutput", 0x1f, [], ["read-only"], ['biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_tpm_pending_operation": MoPropertyMeta("vp_tpm_pending_operation", "vpTPMPendingOperation", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["none", "platform-default", "platform-recommended", "tpmclear", "tpmppioowneroff", "tpmppioowneron"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpTPMPendingOperation": "vp_tpm_pending_operation", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_tpm_pending_operation = None

        ManagedObject.__init__(self, "BiosVfTPMPendingOperation", parent_mo_or_dn, **kwargs)

