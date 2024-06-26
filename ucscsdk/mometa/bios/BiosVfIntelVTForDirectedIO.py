"""This module contains the general information for BiosVfIntelVTForDirectedIO ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosVfIntelVTForDirectedIOConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_INTEL_VTDATSSUPPORT_DISABLED = "disabled"
    VP_INTEL_VTDATSSUPPORT_ENABLED = "enabled"
    VP_INTEL_VTDATSSUPPORT_PLATFORM_DEFAULT = "platform-default"
    VP_INTEL_VTDATSSUPPORT_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_INTEL_VTDCOHERENCY_SUPPORT_DISABLED = "disabled"
    VP_INTEL_VTDCOHERENCY_SUPPORT_ENABLED = "enabled"
    VP_INTEL_VTDCOHERENCY_SUPPORT_PLATFORM_DEFAULT = "platform-default"
    VP_INTEL_VTDCOHERENCY_SUPPORT_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_INTEL_VTDINTERRUPT_REMAPPING_DISABLED = "disabled"
    VP_INTEL_VTDINTERRUPT_REMAPPING_ENABLED = "enabled"
    VP_INTEL_VTDINTERRUPT_REMAPPING_PLATFORM_DEFAULT = "platform-default"
    VP_INTEL_VTDINTERRUPT_REMAPPING_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_INTEL_VTDPASS_THROUGH_DMASUPPORT_DISABLED = "disabled"
    VP_INTEL_VTDPASS_THROUGH_DMASUPPORT_ENABLED = "enabled"
    VP_INTEL_VTDPASS_THROUGH_DMASUPPORT_PLATFORM_DEFAULT = "platform-default"
    VP_INTEL_VTDPASS_THROUGH_DMASUPPORT_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_INTEL_VTFOR_DIRECTED_IO_DISABLED = "disabled"
    VP_INTEL_VTFOR_DIRECTED_IO_ENABLED = "enabled"
    VP_INTEL_VTFOR_DIRECTED_IO_PLATFORM_DEFAULT = "platform-default"
    VP_INTEL_VTFOR_DIRECTED_IO_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfIntelVTForDirectedIO(ManagedObject):
    """This is BiosVfIntelVTForDirectedIO class."""

    consts = BiosVfIntelVTForDirectedIOConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfIntelVTForDirectedIO", "biosVfIntelVTForDirectedIO", "Intel-VT-for-directed-IO", VersionMeta.Version111a, "InputOutput", 0x1ff, [], ["read-only"], ['biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_intel_vtdats_support": MoPropertyMeta("vp_intel_vtdats_support", "vpIntelVTDATSSupport", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []), 
        "vp_intel_vtd_coherency_support": MoPropertyMeta("vp_intel_vtd_coherency_support", "vpIntelVTDCoherencySupport", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []), 
        "vp_intel_vtd_interrupt_remapping": MoPropertyMeta("vp_intel_vtd_interrupt_remapping", "vpIntelVTDInterruptRemapping", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []), 
        "vp_intel_vtd_pass_through_dma_support": MoPropertyMeta("vp_intel_vtd_pass_through_dma_support", "vpIntelVTDPassThroughDMASupport", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []), 
        "vp_intel_vt_for_directed_io": MoPropertyMeta("vp_intel_vt_for_directed_io", "vpIntelVTForDirectedIO", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpIntelVTDATSSupport": "vp_intel_vtdats_support", 
        "vpIntelVTDCoherencySupport": "vp_intel_vtd_coherency_support", 
        "vpIntelVTDInterruptRemapping": "vp_intel_vtd_interrupt_remapping", 
        "vpIntelVTDPassThroughDMASupport": "vp_intel_vtd_pass_through_dma_support", 
        "vpIntelVTForDirectedIO": "vp_intel_vt_for_directed_io", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_intel_vtdats_support = None
        self.vp_intel_vtd_coherency_support = None
        self.vp_intel_vtd_interrupt_remapping = None
        self.vp_intel_vtd_pass_through_dma_support = None
        self.vp_intel_vt_for_directed_io = None

        ManagedObject.__init__(self, "BiosVfIntelVTForDirectedIO", parent_mo_or_dn, **kwargs)

