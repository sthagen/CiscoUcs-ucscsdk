"""This module contains the general information for AdaptorFcIfEventStatsHist ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AdaptorFcIfEventStatsHistConsts():
    INVALID_CRCCOUNT_NA = "NA"
    INVALID_CRCCOUNT_DELTA_NA = "NA"
    INVALID_CRCCOUNT_DELTA_AVG_NA = "NA"
    INVALID_CRCCOUNT_DELTA_MAX_NA = "NA"
    INVALID_CRCCOUNT_DELTA_MIN_NA = "NA"
    LINK_FAILURE_COUNT_NA = "NA"
    LINK_FAILURE_COUNT_DELTA_NA = "NA"
    LINK_FAILURE_COUNT_DELTA_AVG_NA = "NA"
    LINK_FAILURE_COUNT_DELTA_MAX_NA = "NA"
    LINK_FAILURE_COUNT_DELTA_MIN_NA = "NA"
    LIP_COUNT_NA = "NA"
    LIP_COUNT_DELTA_NA = "NA"
    LIP_COUNT_DELTA_AVG_NA = "NA"
    LIP_COUNT_DELTA_MAX_NA = "NA"
    LIP_COUNT_DELTA_MIN_NA = "NA"
    LOSS_OF_SIGNAL_COUNT_NA = "NA"
    LOSS_OF_SIGNAL_COUNT_DELTA_NA = "NA"
    LOSS_OF_SIGNAL_COUNT_DELTA_AVG_NA = "NA"
    LOSS_OF_SIGNAL_COUNT_DELTA_MAX_NA = "NA"
    LOSS_OF_SIGNAL_COUNT_DELTA_MIN_NA = "NA"
    LOSS_OF_SYNC_COUNT_NA = "NA"
    LOSS_OF_SYNC_COUNT_DELTA_NA = "NA"
    LOSS_OF_SYNC_COUNT_DELTA_AVG_NA = "NA"
    LOSS_OF_SYNC_COUNT_DELTA_MAX_NA = "NA"
    LOSS_OF_SYNC_COUNT_DELTA_MIN_NA = "NA"
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    N_OSCOUNT_NA = "NA"
    N_OSCOUNT_DELTA_NA = "NA"
    N_OSCOUNT_DELTA_AVG_NA = "NA"
    N_OSCOUNT_DELTA_MAX_NA = "NA"
    N_OSCOUNT_DELTA_MIN_NA = "NA"
    SECONDS_SINCE_LAST_RESET_NA = "NA"
    SECONDS_SINCE_LAST_RESET_DELTA_NA = "NA"
    SECONDS_SINCE_LAST_RESET_DELTA_AVG_NA = "NA"
    SECONDS_SINCE_LAST_RESET_DELTA_MAX_NA = "NA"
    SECONDS_SINCE_LAST_RESET_DELTA_MIN_NA = "NA"
    SEQ_PROTOCOL_ERR_COUNT_NA = "NA"
    SEQ_PROTOCOL_ERR_COUNT_DELTA_NA = "NA"
    SEQ_PROTOCOL_ERR_COUNT_DELTA_AVG_NA = "NA"
    SEQ_PROTOCOL_ERR_COUNT_DELTA_MAX_NA = "NA"
    SEQ_PROTOCOL_ERR_COUNT_DELTA_MIN_NA = "NA"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class AdaptorFcIfEventStatsHist(ManagedObject):
    """This is AdaptorFcIfEventStatsHist class."""

    consts = AdaptorFcIfEventStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("AdaptorFcIfEventStatsHist", "adaptorFcIfEventStatsHist", "[id]", VersionMeta.Version111a, "OutputOnly", 0xf, [], ["read-only"], ['adaptorFcIfEventStats'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version111a, MoPropertyMeta.NAMING, None, None, None, None, [], []), 
        "invalid_crc_count": MoPropertyMeta("invalid_crc_count", "invalidCRCCount", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "invalid_crc_count_delta": MoPropertyMeta("invalid_crc_count_delta", "invalidCRCCountDelta", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "invalid_crc_count_delta_avg": MoPropertyMeta("invalid_crc_count_delta_avg", "invalidCRCCountDeltaAvg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "invalid_crc_count_delta_max": MoPropertyMeta("invalid_crc_count_delta_max", "invalidCRCCountDeltaMax", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "invalid_crc_count_delta_min": MoPropertyMeta("invalid_crc_count_delta_min", "invalidCRCCountDeltaMin", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "link_failure_count": MoPropertyMeta("link_failure_count", "linkFailureCount", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "link_failure_count_delta": MoPropertyMeta("link_failure_count_delta", "linkFailureCountDelta", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "link_failure_count_delta_avg": MoPropertyMeta("link_failure_count_delta_avg", "linkFailureCountDeltaAvg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "link_failure_count_delta_max": MoPropertyMeta("link_failure_count_delta_max", "linkFailureCountDeltaMax", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "link_failure_count_delta_min": MoPropertyMeta("link_failure_count_delta_min", "linkFailureCountDeltaMin", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "lip_count": MoPropertyMeta("lip_count", "lipCount", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "lip_count_delta": MoPropertyMeta("lip_count_delta", "lipCountDelta", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "lip_count_delta_avg": MoPropertyMeta("lip_count_delta_avg", "lipCountDeltaAvg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "lip_count_delta_max": MoPropertyMeta("lip_count_delta_max", "lipCountDeltaMax", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "lip_count_delta_min": MoPropertyMeta("lip_count_delta_min", "lipCountDeltaMin", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "loss_of_signal_count": MoPropertyMeta("loss_of_signal_count", "lossOfSignalCount", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "loss_of_signal_count_delta": MoPropertyMeta("loss_of_signal_count_delta", "lossOfSignalCountDelta", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "loss_of_signal_count_delta_avg": MoPropertyMeta("loss_of_signal_count_delta_avg", "lossOfSignalCountDeltaAvg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "loss_of_signal_count_delta_max": MoPropertyMeta("loss_of_signal_count_delta_max", "lossOfSignalCountDeltaMax", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "loss_of_signal_count_delta_min": MoPropertyMeta("loss_of_signal_count_delta_min", "lossOfSignalCountDeltaMin", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "loss_of_sync_count": MoPropertyMeta("loss_of_sync_count", "lossOfSyncCount", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "loss_of_sync_count_delta": MoPropertyMeta("loss_of_sync_count_delta", "lossOfSyncCountDelta", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "loss_of_sync_count_delta_avg": MoPropertyMeta("loss_of_sync_count_delta_avg", "lossOfSyncCountDeltaAvg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "loss_of_sync_count_delta_max": MoPropertyMeta("loss_of_sync_count_delta_max", "lossOfSyncCountDeltaMax", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "loss_of_sync_count_delta_min": MoPropertyMeta("loss_of_sync_count_delta_min", "lossOfSyncCountDeltaMin", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "n_os_count": MoPropertyMeta("n_os_count", "nOSCount", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "n_os_count_delta": MoPropertyMeta("n_os_count_delta", "nOSCountDelta", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "n_os_count_delta_avg": MoPropertyMeta("n_os_count_delta_avg", "nOSCountDeltaAvg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "n_os_count_delta_max": MoPropertyMeta("n_os_count_delta_max", "nOSCountDeltaMax", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "n_os_count_delta_min": MoPropertyMeta("n_os_count_delta_min", "nOSCountDeltaMin", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "seconds_since_last_reset": MoPropertyMeta("seconds_since_last_reset", "secondsSinceLastReset", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "seconds_since_last_reset_delta": MoPropertyMeta("seconds_since_last_reset_delta", "secondsSinceLastResetDelta", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "seconds_since_last_reset_delta_avg": MoPropertyMeta("seconds_since_last_reset_delta_avg", "secondsSinceLastResetDeltaAvg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "seconds_since_last_reset_delta_max": MoPropertyMeta("seconds_since_last_reset_delta_max", "secondsSinceLastResetDeltaMax", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "seconds_since_last_reset_delta_min": MoPropertyMeta("seconds_since_last_reset_delta_min", "secondsSinceLastResetDeltaMin", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "seq_protocol_err_count": MoPropertyMeta("seq_protocol_err_count", "seqProtocolErrCount", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "seq_protocol_err_count_delta": MoPropertyMeta("seq_protocol_err_count_delta", "seqProtocolErrCountDelta", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "seq_protocol_err_count_delta_avg": MoPropertyMeta("seq_protocol_err_count_delta_avg", "seqProtocolErrCountDeltaAvg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "seq_protocol_err_count_delta_max": MoPropertyMeta("seq_protocol_err_count_delta_max", "seqProtocolErrCountDeltaMax", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "seq_protocol_err_count_delta_min": MoPropertyMeta("seq_protocol_err_count_delta_min", "seqProtocolErrCountDeltaMin", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "invalidCRCCount": "invalid_crc_count", 
        "invalidCRCCountDelta": "invalid_crc_count_delta", 
        "invalidCRCCountDeltaAvg": "invalid_crc_count_delta_avg", 
        "invalidCRCCountDeltaMax": "invalid_crc_count_delta_max", 
        "invalidCRCCountDeltaMin": "invalid_crc_count_delta_min", 
        "linkFailureCount": "link_failure_count", 
        "linkFailureCountDelta": "link_failure_count_delta", 
        "linkFailureCountDeltaAvg": "link_failure_count_delta_avg", 
        "linkFailureCountDeltaMax": "link_failure_count_delta_max", 
        "linkFailureCountDeltaMin": "link_failure_count_delta_min", 
        "lipCount": "lip_count", 
        "lipCountDelta": "lip_count_delta", 
        "lipCountDeltaAvg": "lip_count_delta_avg", 
        "lipCountDeltaMax": "lip_count_delta_max", 
        "lipCountDeltaMin": "lip_count_delta_min", 
        "lossOfSignalCount": "loss_of_signal_count", 
        "lossOfSignalCountDelta": "loss_of_signal_count_delta", 
        "lossOfSignalCountDeltaAvg": "loss_of_signal_count_delta_avg", 
        "lossOfSignalCountDeltaMax": "loss_of_signal_count_delta_max", 
        "lossOfSignalCountDeltaMin": "loss_of_signal_count_delta_min", 
        "lossOfSyncCount": "loss_of_sync_count", 
        "lossOfSyncCountDelta": "loss_of_sync_count_delta", 
        "lossOfSyncCountDeltaAvg": "loss_of_sync_count_delta_avg", 
        "lossOfSyncCountDeltaMax": "loss_of_sync_count_delta_max", 
        "lossOfSyncCountDeltaMin": "loss_of_sync_count_delta_min", 
        "mostRecent": "most_recent", 
        "nOSCount": "n_os_count", 
        "nOSCountDelta": "n_os_count_delta", 
        "nOSCountDeltaAvg": "n_os_count_delta_avg", 
        "nOSCountDeltaMax": "n_os_count_delta_max", 
        "nOSCountDeltaMin": "n_os_count_delta_min", 
        "rn": "rn", 
        "secondsSinceLastReset": "seconds_since_last_reset", 
        "secondsSinceLastResetDelta": "seconds_since_last_reset_delta", 
        "secondsSinceLastResetDeltaAvg": "seconds_since_last_reset_delta_avg", 
        "secondsSinceLastResetDeltaMax": "seconds_since_last_reset_delta_max", 
        "secondsSinceLastResetDeltaMin": "seconds_since_last_reset_delta_min", 
        "seqProtocolErrCount": "seq_protocol_err_count", 
        "seqProtocolErrCountDelta": "seq_protocol_err_count_delta", 
        "seqProtocolErrCountDeltaAvg": "seq_protocol_err_count_delta_avg", 
        "seqProtocolErrCountDeltaMax": "seq_protocol_err_count_delta_max", 
        "seqProtocolErrCountDeltaMin": "seq_protocol_err_count_delta_min", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.invalid_crc_count = None
        self.invalid_crc_count_delta = None
        self.invalid_crc_count_delta_avg = None
        self.invalid_crc_count_delta_max = None
        self.invalid_crc_count_delta_min = None
        self.link_failure_count = None
        self.link_failure_count_delta = None
        self.link_failure_count_delta_avg = None
        self.link_failure_count_delta_max = None
        self.link_failure_count_delta_min = None
        self.lip_count = None
        self.lip_count_delta = None
        self.lip_count_delta_avg = None
        self.lip_count_delta_max = None
        self.lip_count_delta_min = None
        self.loss_of_signal_count = None
        self.loss_of_signal_count_delta = None
        self.loss_of_signal_count_delta_avg = None
        self.loss_of_signal_count_delta_max = None
        self.loss_of_signal_count_delta_min = None
        self.loss_of_sync_count = None
        self.loss_of_sync_count_delta = None
        self.loss_of_sync_count_delta_avg = None
        self.loss_of_sync_count_delta_max = None
        self.loss_of_sync_count_delta_min = None
        self.most_recent = None
        self.n_os_count = None
        self.n_os_count_delta = None
        self.n_os_count_delta_avg = None
        self.n_os_count_delta_max = None
        self.n_os_count_delta_min = None
        self.seconds_since_last_reset = None
        self.seconds_since_last_reset_delta = None
        self.seconds_since_last_reset_delta_avg = None
        self.seconds_since_last_reset_delta_max = None
        self.seconds_since_last_reset_delta_min = None
        self.seq_protocol_err_count = None
        self.seq_protocol_err_count_delta = None
        self.seq_protocol_err_count_delta_avg = None
        self.seq_protocol_err_count_delta_max = None
        self.seq_protocol_err_count_delta_min = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None

        ManagedObject.__init__(self, "AdaptorFcIfEventStatsHist", parent_mo_or_dn, **kwargs)

