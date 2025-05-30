"""This module contains the general information for VnicEther ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class VnicEtherConsts():
    ADDR_DERIVED = "derived"
    ADMIN_HOST_PORT_1 = "1"
    ADMIN_HOST_PORT_2 = "2"
    ADMIN_HOST_PORT_ANY = "ANY"
    ADMIN_HOST_PORT_NONE = "NONE"
    ADMIN_VCON_1 = "1"
    ADMIN_VCON_2 = "2"
    ADMIN_VCON_3 = "3"
    ADMIN_VCON_4 = "4"
    ADMIN_VCON_ANY = "any"
    CDN_SOURCE_USER_DEFINED = "user-defined"
    CDN_SOURCE_VNIC_NAME = "vnic-name"
    CONFIG_STATE_APPLIED = "applied"
    CONFIG_STATE_APPLYING = "applying"
    CONFIG_STATE_FAILED_TO_APPLY = "failed-to-apply"
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    INST_TYPE_DEFAULT = "default"
    INST_TYPE_DYNAMIC = "dynamic"
    INST_TYPE_DYNAMIC_VF = "dynamic-vf"
    INST_TYPE_MANUAL = "manual"
    OPER_HOST_PORT_1 = "1"
    OPER_HOST_PORT_2 = "2"
    OPER_HOST_PORT_ANY = "ANY"
    OPER_HOST_PORT_NONE = "NONE"
    OPER_ORDER_UNSPECIFIED = "unspecified"
    OPER_SPEED_LINE_RATE = "line-rate"
    OPER_VCON_1 = "1"
    OPER_VCON_2 = "2"
    OPER_VCON_3 = "3"
    OPER_VCON_4 = "4"
    OPER_VCON_ANY = "any"
    ORDER_UNSPECIFIED = "unspecified"
    OWNER_CONN_POLICY = "conn_policy"
    OWNER_INITIATOR_POLICY = "initiator_policy"
    OWNER_LOGICAL = "logical"
    OWNER_PHYSICAL = "physical"
    OWNER_POLICY = "policy"
    OWNER_UNKNOWN = "unknown"
    PURPOSE_CROSSLINK = "crosslink"
    PURPOSE_GENERAL = "general"
    PURPOSE_MANAGEMENT = "management"
    PURPOSE_OVERLAY = "overlay"
    PURPOSE_UNUSED = "unused"
    PURPOSE_UTILITY = "utility"
    REDUNDANCY_PAIR_TYPE_NONE = "none"
    REDUNDANCY_PAIR_TYPE_PRIMARY = "primary"
    REDUNDANCY_PAIR_TYPE_SECONDARY = "secondary"
    SRIOV_HPN_PREFERENCE_DISABLED = "disabled"
    SRIOV_HPN_PREFERENCE_ENABLED = "enabled"
    SWITCH_ID_A = "A"
    SWITCH_ID_A_B = "A-B"
    SWITCH_ID_B = "B"
    SWITCH_ID_B_A = "B-A"
    SWITCH_ID_NONE = "NONE"
    SWITCH_ID_MGMT = "mgmt"
    TYPE_ETHER = "ether"
    TYPE_FC = "fc"
    TYPE_IPC = "ipc"
    TYPE_SCSI = "scsi"
    TYPE_UNKNOWN = "unknown"
    VIRTUALIZATION_PREFERENCE_NONE = "NONE"
    VIRTUALIZATION_PREFERENCE_SRIOV = "SRIOV"
    VIRTUALIZATION_PREFERENCE_SRIOV_HPN = "SRIOV-HPN"
    VIRTUALIZATION_PREFERENCE_SRIOV_USNIC = "SRIOV-USNIC"
    VIRTUALIZATION_PREFERENCE_SRIOV_VMFEX = "SRIOV-VMFEX"
    VIRTUALIZATION_PREFERENCE_VMMQ = "VMMQ"
    VIRTUALIZATION_PREFERENCE_VMQ = "VMQ"


class VnicEther(ManagedObject):
    """This is VnicEther class."""

    consts = VnicEtherConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("VnicEther", "vnicEther", "ether-[name]", VersionMeta.Version111a, "InputOutput", 0xfffff, [], ["admin", "ls-config", "ls-network", "ls-server"], ['computeInstance', 'computeLocalTemplDef', 'fabricDceSwSrvPcOperation', 'fabricEthEstcEpOperation', 'fabricEthEstcPcOperation', 'fabricEthLanEpOperation', 'fabricEthLanPcOperation', 'fabricEthMonOperation', 'lsServer', 'vnicLanConnPolicy', 'vnicNetGroup', 'vnicNetGroupRef'], ['fabricEthMonSrcEp', 'fabricEthMonSrcEpOperation', 'fabricFcMonSrcEp', 'fabricNetGroupRef', 'faultInst', 'vnicDynamicConPolicyRef', 'vnicEtherIf', 'vnicFcOEIf', 'vnicLifVlan', 'vnicSriovHpnConPolicyRef', 'vnicUsnicConPolicyRef', 'vnicVmqConPolicyRef'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "adaptor_profile_name": MoPropertyMeta("adaptor_profile_name", "adaptorProfileName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", ["derived"], []), 
        "admin_cdn_name": MoPropertyMeta("admin_cdn_name", "adminCdnName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "admin_host_port": MoPropertyMeta("admin_host_port", "adminHostPort", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["1", "2", "ANY", "NONE"], []), 
        "admin_vcon": MoPropertyMeta("admin_vcon", "adminVcon", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["1", "2", "3", "4", "any"], []), 
        "boot_dev": MoPropertyMeta("boot_dev", "bootDev", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "cdn_source": MoPropertyMeta("cdn_source", "cdnSource", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["user-defined", "vnic-name"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|unsupported-azurestackqos-geneve|adaptor-protected-eth-capability|vif-resources-overprovisioned|ungrouped-domain|unsupported-nvgre|unsupported-adaptor-for-vnic-cdn|misconfigured-net-san-group|unresolved-remote-vlan-name|invalid-wwn|service-profile-virtualization-conflict|unsupported-roce-netflow|unsupported-vxlan-netflow|redundancy-vnicpair-not-in-sync|fcoe-capacity|wwpn-derivation-virtualized-port|unresolved-vlan-name|vnic-virtualization-netflow-conflict|unsupported-vxlan-usnic|unsupported-roce-properties|pinning-vlan-mismatch|adaptor-requirement|vnic-not-ha-ready|missing-ipv4-inband-mgmt-addr|unsupported-nvgre-dynamic-vnic|duplicate-vnic-cdn-name|overlapping-vlans|unresolved-remote-vsan-name|mac-derivation-virtualized-port|vnic-virtualization-conflict|unsupported-roce|unsupported-nvgre-netflow|unsupported-adaptor-for-vnic-oracle-rac|vnic-vlan-assignment-error|insufficient-vhba-capacity|inaccessible-vlan|unable-to-update-ucsm|soft-pinning-vlan-mismatch|unsupported-roce-sriov|unsupported-geneve-usnic-vmq|unsupported-nvgre-vmq|connection-placement|vnic-vcon-provisioning-change|missing-ipv6-inband-mgmt-addr|unsupported-nvgre-usnic|insufficient-roce-resources|unsupported-azurestackqos-vmmq-geneve-advfilters|missing-primary-vlan|adaptor-fcoe-capability|vfc-vnic-pvlan-conflict|virtualization-not-supported|unsupported-vxlan|unsupported-roce-nvgre|unresolved-net-san-group|unresolved-vsan-name|insufficient-vnic-capacity|unassociated-vlan|unsupported-roce-vmq|unsupported-roce-vxlan|unsupported-vxlan-vmq|redundancy-vnic-not-in-pair|dynamic-vf-vnic|wwpn-assignment|missing-ipv4-addr|unsupported-vxlan-dynamic-vnic|pinned-target-misconfig|unsupported-vmq-resources),){0,67}(defaultValue|not-applicable|unsupported-azurestackqos-geneve|adaptor-protected-eth-capability|vif-resources-overprovisioned|ungrouped-domain|unsupported-nvgre|unsupported-adaptor-for-vnic-cdn|misconfigured-net-san-group|unresolved-remote-vlan-name|invalid-wwn|service-profile-virtualization-conflict|unsupported-roce-netflow|unsupported-vxlan-netflow|redundancy-vnicpair-not-in-sync|fcoe-capacity|wwpn-derivation-virtualized-port|unresolved-vlan-name|vnic-virtualization-netflow-conflict|unsupported-vxlan-usnic|unsupported-roce-properties|pinning-vlan-mismatch|adaptor-requirement|vnic-not-ha-ready|missing-ipv4-inband-mgmt-addr|unsupported-nvgre-dynamic-vnic|duplicate-vnic-cdn-name|overlapping-vlans|unresolved-remote-vsan-name|mac-derivation-virtualized-port|vnic-virtualization-conflict|unsupported-roce|unsupported-nvgre-netflow|unsupported-adaptor-for-vnic-oracle-rac|vnic-vlan-assignment-error|insufficient-vhba-capacity|inaccessible-vlan|unable-to-update-ucsm|soft-pinning-vlan-mismatch|unsupported-roce-sriov|unsupported-geneve-usnic-vmq|unsupported-nvgre-vmq|connection-placement|vnic-vcon-provisioning-change|missing-ipv6-inband-mgmt-addr|unsupported-nvgre-usnic|insufficient-roce-resources|unsupported-azurestackqos-vmmq-geneve-advfilters|missing-primary-vlan|adaptor-fcoe-capability|vfc-vnic-pvlan-conflict|virtualization-not-supported|unsupported-vxlan|unsupported-roce-nvgre|unresolved-net-san-group|unresolved-vsan-name|insufficient-vnic-capacity|unassociated-vlan|unsupported-roce-vmq|unsupported-roce-vxlan|unsupported-vxlan-vmq|redundancy-vnic-not-in-pair|dynamic-vf-vnic|wwpn-assignment|missing-ipv4-addr|unsupported-vxlan-dynamic-vnic|pinned-target-misconfig|unsupported-vmq-resources){0,1}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["applied", "applying", "failed-to-apply", "not-applied"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []), 
        "dynamic_id": MoPropertyMeta("dynamic_id", "dynamicId", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "equipment_dn": MoPropertyMeta("equipment_dn", "equipmentDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "ident_pool_name": MoPropertyMeta("ident_pool_name", "identPoolName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], []), 
        "inst_type": MoPropertyMeta("inst_type", "instType", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["default", "dynamic", "dynamic-vf", "manual"], []), 
        "mtu": MoPropertyMeta("mtu", "mtu", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, [], ["1500-9000"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x400, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "nw_ctrl_policy_name": MoPropertyMeta("nw_ctrl_policy_name", "nwCtrlPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "nw_templ_name": MoPropertyMeta("nw_templ_name", "nwTemplName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "oper_adaptor_profile_name": MoPropertyMeta("oper_adaptor_profile_name", "operAdaptorProfileName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_cdn_name": MoPropertyMeta("oper_cdn_name", "operCdnName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_host_port": MoPropertyMeta("oper_host_port", "operHostPort", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["1", "2", "ANY", "NONE"], []), 
        "oper_ident_pool_name": MoPropertyMeta("oper_ident_pool_name", "operIdentPoolName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_nw_ctrl_policy_name": MoPropertyMeta("oper_nw_ctrl_policy_name", "operNwCtrlPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_nw_templ_name": MoPropertyMeta("oper_nw_templ_name", "operNwTemplName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_order": MoPropertyMeta("oper_order", "operOrder", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "oper_qos_policy_name": MoPropertyMeta("oper_qos_policy_name", "operQosPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_speed": MoPropertyMeta("oper_speed", "operSpeed", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["line-rate"], ["8-40000000"]), 
        "oper_stats_policy_name": MoPropertyMeta("oper_stats_policy_name", "operStatsPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_vcon": MoPropertyMeta("oper_vcon", "operVcon", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["1", "2", "3", "4", "any"], []), 
        "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["unspecified"], ["0-256"]), 
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["conn_policy", "initiator_policy", "logical", "physical", "policy", "unknown"], []), 
        "pf_dn": MoPropertyMeta("pf_dn", "pfDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "pin_to_group_name": MoPropertyMeta("pin_to_group_name", "pinToGroupName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x4000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "purpose": MoPropertyMeta("purpose", "purpose", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["crosslink", "general", "management", "overlay", "unused", "utility"], []), 
        "qos_policy_name": MoPropertyMeta("qos_policy_name", "qosPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "redundancy_pair_type": MoPropertyMeta("redundancy_pair_type", "redundancyPairType", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["none", "primary", "secondary"], []), 
        "redundancy_peer": MoPropertyMeta("redundancy_peer", "redundancyPeer", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x10000, 0, 256, None, [], []), 
        "sriov_hpn_preference": MoPropertyMeta("sriov_hpn_preference", "sriovHpnPreference", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []), 
        "stats_policy_name": MoPropertyMeta("stats_policy_name", "statsPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x40000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x80000, None, None, None, ["A", "A-B", "B", "B-A", "NONE", "mgmt"], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ether", "fc", "ipc", "scsi", "unknown"], []), 
        "virtualization_preference": MoPropertyMeta("virtualization_preference", "virtualizationPreference", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NONE", "SRIOV", "SRIOV-HPN", "SRIOV-USNIC", "SRIOV-VMFEX", "VMMQ", "VMQ"], []), 
    }

    prop_map = {
        "adaptorProfileName": "adaptor_profile_name", 
        "addr": "addr", 
        "adminCdnName": "admin_cdn_name", 
        "adminHostPort": "admin_host_port", 
        "adminVcon": "admin_vcon", 
        "bootDev": "boot_dev", 
        "cdnSource": "cdn_source", 
        "childAction": "child_action", 
        "configQualifier": "config_qualifier", 
        "configState": "config_state", 
        "dn": "dn", 
        "dynamicId": "dynamic_id", 
        "equipmentDn": "equipment_dn", 
        "fltAggr": "flt_aggr", 
        "identPoolName": "ident_pool_name", 
        "instType": "inst_type", 
        "mtu": "mtu", 
        "name": "name", 
        "nwCtrlPolicyName": "nw_ctrl_policy_name", 
        "nwTemplName": "nw_templ_name", 
        "operAdaptorProfileName": "oper_adaptor_profile_name", 
        "operCdnName": "oper_cdn_name", 
        "operHostPort": "oper_host_port", 
        "operIdentPoolName": "oper_ident_pool_name", 
        "operNwCtrlPolicyName": "oper_nw_ctrl_policy_name", 
        "operNwTemplName": "oper_nw_templ_name", 
        "operOrder": "oper_order", 
        "operQosPolicyName": "oper_qos_policy_name", 
        "operSpeed": "oper_speed", 
        "operStatsPolicyName": "oper_stats_policy_name", 
        "operVcon": "oper_vcon", 
        "order": "order", 
        "owner": "owner", 
        "pfDn": "pf_dn", 
        "pinToGroupName": "pin_to_group_name", 
        "purpose": "purpose", 
        "qosPolicyName": "qos_policy_name", 
        "redundancyPairType": "redundancy_pair_type", 
        "redundancyPeer": "redundancy_peer", 
        "rn": "rn", 
        "sriovHpnPreference": "sriov_hpn_preference", 
        "statsPolicyName": "stats_policy_name", 
        "status": "status", 
        "switchId": "switch_id", 
        "type": "type", 
        "virtualizationPreference": "virtualization_preference", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.adaptor_profile_name = None
        self.addr = None
        self.admin_cdn_name = None
        self.admin_host_port = None
        self.admin_vcon = None
        self.boot_dev = None
        self.cdn_source = None
        self.child_action = None
        self.config_qualifier = None
        self.config_state = None
        self.dynamic_id = None
        self.equipment_dn = None
        self.flt_aggr = None
        self.ident_pool_name = None
        self.inst_type = None
        self.mtu = None
        self.nw_ctrl_policy_name = None
        self.nw_templ_name = None
        self.oper_adaptor_profile_name = None
        self.oper_cdn_name = None
        self.oper_host_port = None
        self.oper_ident_pool_name = None
        self.oper_nw_ctrl_policy_name = None
        self.oper_nw_templ_name = None
        self.oper_order = None
        self.oper_qos_policy_name = None
        self.oper_speed = None
        self.oper_stats_policy_name = None
        self.oper_vcon = None
        self.order = None
        self.owner = None
        self.pf_dn = None
        self.pin_to_group_name = None
        self.purpose = None
        self.qos_policy_name = None
        self.redundancy_pair_type = None
        self.redundancy_peer = None
        self.sriov_hpn_preference = None
        self.stats_policy_name = None
        self.status = None
        self.switch_id = None
        self.type = None
        self.virtualization_preference = None

        ManagedObject.__init__(self, "VnicEther", parent_mo_or_dn, **kwargs)

