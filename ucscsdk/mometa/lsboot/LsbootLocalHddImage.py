"""This module contains the general information for LsbootLocalHddImage ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LsbootLocalHddImageConsts():
    TYPE_EMBEDDED_LOCAL_JBOD = "embedded-local-jbod"
    TYPE_EMBEDDED_LOCAL_LUN = "embedded-local-lun"
    TYPE_LOCAL_ANY = "local-any"
    TYPE_LOCAL_JBOD = "local-jbod"
    TYPE_LOCAL_LUN = "local-lun"
    TYPE_NVME = "nvme"
    TYPE_SD_CARD = "sd-card"
    TYPE_USB_EXTERN = "usb-extern"
    TYPE_USB_INTERN = "usb-intern"


class LsbootLocalHddImage(ManagedObject):
    """This is LsbootLocalHddImage class."""

    consts = LsbootLocalHddImageConsts()
    naming_props = set([])

    mo_meta = MoMeta("LsbootLocalHddImage", "lsbootLocalHddImage", "local-hdd", VersionMeta.Version112a, "InputOutput", 0x1f, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-server-policy", "ls-storage", "ls-storage-policy"], ['lsbootLocalStorage'], ['lsbootLocalLunImagePath', 'lsbootUEFIBootParam'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "order": MoPropertyMeta("order", "order", "ushort", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["1-16"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["embedded-local-jbod", "embedded-local-lun", "local-any", "local-jbod", "local-lun", "nvme", "sd-card", "usb-extern", "usb-intern"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "order": "order", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.order = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "LsbootLocalHddImage", parent_mo_or_dn, **kwargs)

