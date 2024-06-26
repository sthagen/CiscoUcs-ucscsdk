"""This module contains the general information for TrigRecurrWindow ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class TrigRecurrWindowConsts():
    CONCUR_CAP_UNLIMITED = "unlimited"
    DAY_FRIDAY = "Friday"
    DAY_MONDAY = "Monday"
    DAY_SATURDAY = "Saturday"
    DAY_SUNDAY = "Sunday"
    DAY_THURSDAY = "Thursday"
    DAY_TUESDAY = "Tuesday"
    DAY_WEDNESDAY = "Wednesday"
    DAY_EVEN_DAY = "even-day"
    DAY_EVERY_DAY = "every-day"
    DAY_ODD_DAY = "odd-day"
    PROC_BREAK_NONE = "none"
    PROC_CAP_UNLIMITED = "unlimited"
    TIME_CAP_NONE = "none"


class TrigRecurrWindow(ManagedObject):
    """This is TrigRecurrWindow class."""

    consts = TrigRecurrWindowConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("TrigRecurrWindow", "trigRecurrWindow", "recurr-[name]", VersionMeta.Version101a, "InputOutput", 0x1fff, [], ["admin", "ls-compute", "ls-config", "ls-server"], ['trigSched'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "concur_cap": MoPropertyMeta("concur_cap", "concurCap", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["unlimited"], ["0-65535"]), 
        "day": MoPropertyMeta("day", "day", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["Friday", "Monday", "Saturday", "Sunday", "Thursday", "Tuesday", "Wednesday", "even-day", "every-day", "odd-day"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "hour": MoPropertyMeta("hour", "hour", "ushort", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["0-23"]), 
        "job_count": MoPropertyMeta("job_count", "jobCount", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "minute": MoPropertyMeta("minute", "minute", "ushort", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["0-59"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "proc_break": MoPropertyMeta("proc_break", "procBreak", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[0-9]+:([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]{1,3})?""", ["none"], ["0-4294967295"]), 
        "proc_cap": MoPropertyMeta("proc_cap", "procCap", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["unlimited"], ["0-65535"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []), 
        "start_date": MoPropertyMeta("start_date", "startDate", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "time_cap": MoPropertyMeta("time_cap", "timeCap", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""[0-9]+:([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]{1,3})?""", ["none"], ["0-4294967295"]), 
    }

    prop_map = {
        "childAction": "child_action", 
        "concurCap": "concur_cap", 
        "day": "day", 
        "dn": "dn", 
        "hour": "hour", 
        "jobCount": "job_count", 
        "minute": "minute", 
        "name": "name", 
        "procBreak": "proc_break", 
        "procCap": "proc_cap", 
        "rn": "rn", 
        "startDate": "start_date", 
        "status": "status", 
        "timeCap": "time_cap", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.concur_cap = None
        self.day = None
        self.hour = None
        self.job_count = None
        self.minute = None
        self.proc_break = None
        self.proc_cap = None
        self.start_date = None
        self.status = None
        self.time_cap = None

        ManagedObject.__init__(self, "TrigRecurrWindow", parent_mo_or_dn, **kwargs)

