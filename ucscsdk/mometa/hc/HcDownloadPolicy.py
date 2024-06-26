"""This module contains the general information for HcDownloadPolicy ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class HcDownloadPolicyConsts():
    DOWNLOAD_INTERVAL_1DAY = "1day"
    DOWNLOAD_INTERVAL_1WEEK = "1week"
    DOWNLOAD_INTERVAL_2WEEK = "2week"
    DOWNLOAD_INTERVAL_ON_DEMAND = "on-demand"
    INT_ID_NONE = "none"
    POLICY_ADMIN_STATE_DISABLE = "disable"
    POLICY_ADMIN_STATE_ENABLE = "enable"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    PROXY_PWD_SET_FALSE = "false"
    PROXY_PWD_SET_NO = "no"
    PROXY_PWD_SET_TRUE = "true"
    PROXY_PWD_SET_YES = "yes"
    PWD_SET_FALSE = "false"
    PWD_SET_NO = "no"
    PWD_SET_TRUE = "true"
    PWD_SET_YES = "yes"
    TYPE_CISCO = "Cisco"
    TYPE_LOCAL = "local"


class HcDownloadPolicy(ManagedObject):
    """This is HcDownloadPolicy class."""

    consts = HcDownloadPolicyConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("HcDownloadPolicy", "hcDownloadPolicy", "hc-dl-policy-[type]", VersionMeta.Version151a, "InputOutput", 0x3ff, [], ["admin"], ['hcCatalogSource', 'orgDomainGroup'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "download_interval": MoPropertyMeta("download_interval", "downloadInterval", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["1day", "1week", "2week", "on-demand"], []), 
        "enc_password": MoPropertyMeta("enc_password", "encPassword", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "enc_proxy_pwd": MoPropertyMeta("enc_proxy_pwd", "encProxyPwd", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "http_proxy": MoPropertyMeta("http_proxy", "httpProxy", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([a-zA-Z0-9][a-zA-Z0-9_.@-]{0,63}(:[0-9]|:[1-9][0-9]|:[1-9][0-9][0-9]|:[1-9][0-9][0-9][0-9]|:[1-5][0-9][0-9][0-9][0-9]|:6[0-4][0-9][0-9][0-9]|:65[0-4][0-9][0-9]|:655[0-2][0-9]|:6553[0-5])?)?$""", [], []), 
        "http_url": MoPropertyMeta("http_url", "httpURL", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10, 0, 510, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 64, None, [], []), 
        "policy_admin_state": MoPropertyMeta("policy_admin_state", "policyAdminState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["disable", "enable"], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "proxy_pwd": MoPropertyMeta("proxy_pwd", "proxyPwd", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 64, None, [], []), 
        "proxy_pwd_set": MoPropertyMeta("proxy_pwd_set", "proxyPwdSet", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "proxy_user": MoPropertyMeta("proxy_user", "proxyUser", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([a-zA-Z0-9_.@-]{0,64})?$""", [], []), 
        "pwd_set": MoPropertyMeta("pwd_set", "pwdSet", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x200, None, None, None, ["Cisco", "local"], []), 
        "username": MoPropertyMeta("username", "username", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([a-zA-Z0-9_.@-]{0,64})?$""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "downloadInterval": "download_interval", 
        "encPassword": "enc_password", 
        "encProxyPwd": "enc_proxy_pwd", 
        "httpProxy": "http_proxy", 
        "httpURL": "http_url", 
        "intId": "int_id", 
        "name": "name", 
        "password": "password", 
        "policyAdminState": "policy_admin_state", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "proxyPwd": "proxy_pwd", 
        "proxyPwdSet": "proxy_pwd_set", 
        "proxyUser": "proxy_user", 
        "pwdSet": "pwd_set", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
        "username": "username", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.descr = None
        self.download_interval = None
        self.enc_password = None
        self.enc_proxy_pwd = None
        self.http_proxy = None
        self.http_url = None
        self.int_id = None
        self.name = None
        self.password = None
        self.policy_admin_state = None
        self.policy_level = None
        self.policy_owner = None
        self.proxy_pwd = None
        self.proxy_pwd_set = None
        self.proxy_user = None
        self.pwd_set = None
        self.status = None
        self.username = None

        ManagedObject.__init__(self, "HcDownloadPolicy", parent_mo_or_dn, **kwargs)

