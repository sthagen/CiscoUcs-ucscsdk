"""This module contains the general information for ConfigImpact ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ConfigImpactConsts():
    CHASSIS_CONFIG_STATE_APPLIED = "applied"
    CHASSIS_CONFIG_STATE_APPLYING = "applying"
    CHASSIS_CONFIG_STATE_FAILED_TO_APPLY = "failed-to-apply"
    CHASSIS_CONFIG_STATE_NOT_APPLIED = "not-applied"
    CONFIG_STATE_APPLIED = "applied"
    CONFIG_STATE_APPLYING = "applying"
    CONFIG_STATE_FAILED_TO_APPLY = "failed-to-apply"
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    DEPLOYMENT_MODE_IMMEDIATE = "immediate"
    DEPLOYMENT_MODE_TIMER_AUTOMATIC = "timer-automatic"
    DEPLOYMENT_MODE_USER_ACK = "user-ack"
    REBOOT_REQUIRED_FALSE = "false"
    REBOOT_REQUIRED_NO = "no"
    REBOOT_REQUIRED_TRUE = "true"
    REBOOT_REQUIRED_YES = "yes"


class ConfigImpact(ManagedObject):
    """This is ConfigImpact class."""

    consts = ConfigImpactConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("ConfigImpact", "configImpact", "impact-[name]", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["read-only"], ['configManagedEpImpactResponse'], [], [None])

    prop_meta = {
        "affected_chassis": MoPropertyMeta("affected_chassis", "affectedChassis", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "affected_obj": MoPropertyMeta("affected_obj", "affectedObj", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "affected_server": MoPropertyMeta("affected_server", "affectedServer", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "changes": MoPropertyMeta("changes", "changes", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|storage|boot-order|chassis-assignment|server-assignment|operational-policies|chassis-identity|local-storage|server-identity|networking|vnic-vhba-placement),){0,10}(defaultValue|storage|boot-order|chassis-assignment|server-assignment|operational-policies|chassis-identity|local-storage|server-identity|networking|vnic-vhba-placement){0,1}""", [], []), 
        "chassis_config_issues": MoPropertyMeta("chassis_config_issues", "chassisConfigIssues", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|chassis-profile-not-supported|migration|firmware-version-mismatch|non-interrupt-fsm-running|insufficient-resources|compute-conn-invalid-hw-config|physical-requirement|chassis-undiscovered|chassis-feature-capability-mismatch|resource-ownership-conflict|compute-conn-unsupported-cmc-version|chassis-unavailable|invalid-chassis-pack|missing-firmware-image|chassis-feature-capability-mismatch-non-fatal|compute-second-controller-unsupported-cmc-version|insufficient-power-budget),){0,18}(defaultValue|not-applicable|chassis-profile-not-supported|migration|firmware-version-mismatch|non-interrupt-fsm-running|insufficient-resources|compute-conn-invalid-hw-config|physical-requirement|chassis-undiscovered|chassis-feature-capability-mismatch|resource-ownership-conflict|compute-conn-unsupported-cmc-version|chassis-unavailable|invalid-chassis-pack|missing-firmware-image|chassis-feature-capability-mismatch-non-fatal|compute-second-controller-unsupported-cmc-version|insufficient-power-budget){0,1}""", [], []), 
        "chassis_config_qualifier": MoPropertyMeta("chassis_config_qualifier", "chassisConfigQualifier", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|chassis-profile-not-supported|migration|firmware-version-mismatch|non-interrupt-fsm-running|insufficient-resources|compute-conn-invalid-hw-config|physical-requirement|chassis-undiscovered|chassis-feature-capability-mismatch|resource-ownership-conflict|compute-conn-unsupported-cmc-version|chassis-unavailable|invalid-chassis-pack|missing-firmware-image|chassis-feature-capability-mismatch-non-fatal|compute-second-controller-unsupported-cmc-version|insufficient-power-budget),){0,18}(defaultValue|not-applicable|chassis-profile-not-supported|migration|firmware-version-mismatch|non-interrupt-fsm-running|insufficient-resources|compute-conn-invalid-hw-config|physical-requirement|chassis-undiscovered|chassis-feature-capability-mismatch|resource-ownership-conflict|compute-conn-unsupported-cmc-version|chassis-unavailable|invalid-chassis-pack|missing-firmware-image|chassis-feature-capability-mismatch-non-fatal|compute-second-controller-unsupported-cmc-version|insufficient-power-budget){0,1}""", [], []), 
        "chassis_config_state": MoPropertyMeta("chassis_config_state", "chassisConfigState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["applied", "applying", "failed-to-apply", "not-applied"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_issues": MoPropertyMeta("config_issues", "configIssues", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|boot-order-pxe|wwnn-derivation-from-vhba|migration|incompat-bios-for-sriov-vnics|iscsi-initiator-ip-address|remote-policy|wwnn-assignment|processor-requirement|physical-requirement|hostimg-policy-invalid|vif-resources-overprovisioned|pinning-invalid|incompatible-number-of-local-disks|mac-derivation-virtualized-port|switch-virtual-if-capacity|invalid-wwn|missing-raid-key|board-controller-update-unsupported|insufficient-resources|compute-undiscovered|boot-configuration-invalid|incompatible-bios-image|iscsi-config|storage-path-configuration-error|resource-ownership-conflict|system-uuid-assignment|server-position-requirement|destructive-local-disk-config|imgsec-policy-invalid|pinning-vlan-mismatch|non-interrupt-fsm-running|vnic-capacity|adaptor-requirement|mac-address-assignment|qos-policy-invalid|insufficient-power-budget|boot-order-iscsi|vnic-vcon-provisioning-change|adaptor-protected-eth-capability|connection-placement|incompatible-disk-types|vnic-not-ha-ready|zone-capacity|adaptor-out-of-vifs|duplicate-address-conflict|vhba-capacity|boot-order-san-image-path|compute-unavailable|power-group-requirement|provsrv-policy-invalid|vnic-vlan-assignment-error|missing-firmware-image|wwpn-assignment|memory-requirement|vlan-port-capacity|bootip-policy-invalid|vfc-vnic-pvlan-conflict|named-vlan-inaccessible|adaptor-fcoe-capability|wwpn-derivation-virtualized-port|incompatible-raid-level|missing-primary-vlan|fcoe-capacity|dynamic-vf-vnic),){0,65}(defaultValue|not-applicable|boot-order-pxe|wwnn-derivation-from-vhba|migration|incompat-bios-for-sriov-vnics|iscsi-initiator-ip-address|remote-policy|wwnn-assignment|processor-requirement|physical-requirement|hostimg-policy-invalid|vif-resources-overprovisioned|pinning-invalid|incompatible-number-of-local-disks|mac-derivation-virtualized-port|switch-virtual-if-capacity|invalid-wwn|missing-raid-key|board-controller-update-unsupported|insufficient-resources|compute-undiscovered|boot-configuration-invalid|incompatible-bios-image|iscsi-config|storage-path-configuration-error|resource-ownership-conflict|system-uuid-assignment|server-position-requirement|destructive-local-disk-config|imgsec-policy-invalid|pinning-vlan-mismatch|non-interrupt-fsm-running|vnic-capacity|adaptor-requirement|mac-address-assignment|qos-policy-invalid|insufficient-power-budget|boot-order-iscsi|vnic-vcon-provisioning-change|adaptor-protected-eth-capability|connection-placement|incompatible-disk-types|vnic-not-ha-ready|zone-capacity|adaptor-out-of-vifs|duplicate-address-conflict|vhba-capacity|boot-order-san-image-path|compute-unavailable|power-group-requirement|provsrv-policy-invalid|vnic-vlan-assignment-error|missing-firmware-image|wwpn-assignment|memory-requirement|vlan-port-capacity|bootip-policy-invalid|vfc-vnic-pvlan-conflict|named-vlan-inaccessible|adaptor-fcoe-capability|wwpn-derivation-virtualized-port|incompatible-raid-level|missing-primary-vlan|fcoe-capacity|dynamic-vf-vnic){0,1}""", [], []), 
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|boot-order-pxe|wwnn-derivation-from-vhba|migration|incompat-bios-for-sriov-vnics|iscsi-initiator-ip-address|remote-policy|wwnn-assignment|processor-requirement|physical-requirement|hostimg-policy-invalid|vif-resources-overprovisioned|pinning-invalid|incompatible-number-of-local-disks|mac-derivation-virtualized-port|switch-virtual-if-capacity|invalid-wwn|missing-raid-key|board-controller-update-unsupported|insufficient-resources|compute-undiscovered|boot-configuration-invalid|incompatible-bios-image|iscsi-config|storage-path-configuration-error|resource-ownership-conflict|system-uuid-assignment|server-position-requirement|destructive-local-disk-config|imgsec-policy-invalid|pinning-vlan-mismatch|non-interrupt-fsm-running|vnic-capacity|adaptor-requirement|mac-address-assignment|qos-policy-invalid|insufficient-power-budget|boot-order-iscsi|vnic-vcon-provisioning-change|adaptor-protected-eth-capability|connection-placement|incompatible-disk-types|vnic-not-ha-ready|zone-capacity|adaptor-out-of-vifs|duplicate-address-conflict|vhba-capacity|boot-order-san-image-path|compute-unavailable|power-group-requirement|provsrv-policy-invalid|vnic-vlan-assignment-error|missing-firmware-image|wwpn-assignment|memory-requirement|vlan-port-capacity|bootip-policy-invalid|vfc-vnic-pvlan-conflict|named-vlan-inaccessible|adaptor-fcoe-capability|wwpn-derivation-virtualized-port|incompatible-raid-level|missing-primary-vlan|fcoe-capacity|dynamic-vf-vnic),){0,65}(defaultValue|not-applicable|boot-order-pxe|wwnn-derivation-from-vhba|migration|incompat-bios-for-sriov-vnics|iscsi-initiator-ip-address|remote-policy|wwnn-assignment|processor-requirement|physical-requirement|hostimg-policy-invalid|vif-resources-overprovisioned|pinning-invalid|incompatible-number-of-local-disks|mac-derivation-virtualized-port|switch-virtual-if-capacity|invalid-wwn|missing-raid-key|board-controller-update-unsupported|insufficient-resources|compute-undiscovered|boot-configuration-invalid|incompatible-bios-image|iscsi-config|storage-path-configuration-error|resource-ownership-conflict|system-uuid-assignment|server-position-requirement|destructive-local-disk-config|imgsec-policy-invalid|pinning-vlan-mismatch|non-interrupt-fsm-running|vnic-capacity|adaptor-requirement|mac-address-assignment|qos-policy-invalid|insufficient-power-budget|boot-order-iscsi|vnic-vcon-provisioning-change|adaptor-protected-eth-capability|connection-placement|incompatible-disk-types|vnic-not-ha-ready|zone-capacity|adaptor-out-of-vifs|duplicate-address-conflict|vhba-capacity|boot-order-san-image-path|compute-unavailable|power-group-requirement|provsrv-policy-invalid|vnic-vlan-assignment-error|missing-firmware-image|wwpn-assignment|memory-requirement|vlan-port-capacity|bootip-policy-invalid|vfc-vnic-pvlan-conflict|named-vlan-inaccessible|adaptor-fcoe-capability|wwpn-derivation-virtualized-port|incompatible-raid-level|missing-primary-vlan|fcoe-capacity|dynamic-vf-vnic){0,1}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["applied", "applying", "failed-to-apply", "not-applied"], []), 
        "deployment_mode": MoPropertyMeta("deployment_mode", "deploymentMode", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["immediate", "timer-automatic", "user-ack"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x4, 1, 510, None, [], []), 
        "reboot_required": MoPropertyMeta("reboot_required", "rebootRequired", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "affectedChassis": "affected_chassis", 
        "affectedObj": "affected_obj", 
        "affectedServer": "affected_server", 
        "changes": "changes", 
        "chassisConfigIssues": "chassis_config_issues", 
        "chassisConfigQualifier": "chassis_config_qualifier", 
        "chassisConfigState": "chassis_config_state", 
        "childAction": "child_action", 
        "configIssues": "config_issues", 
        "configQualifier": "config_qualifier", 
        "configState": "config_state", 
        "deploymentMode": "deployment_mode", 
        "dn": "dn", 
        "name": "name", 
        "rebootRequired": "reboot_required", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.affected_chassis = None
        self.affected_obj = None
        self.affected_server = None
        self.changes = None
        self.chassis_config_issues = None
        self.chassis_config_qualifier = None
        self.chassis_config_state = None
        self.child_action = None
        self.config_issues = None
        self.config_qualifier = None
        self.config_state = None
        self.deployment_mode = None
        self.reboot_required = None
        self.status = None

        ManagedObject.__init__(self, "ConfigImpact", parent_mo_or_dn, **kwargs)

