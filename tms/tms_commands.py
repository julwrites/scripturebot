
# Local modules
from common import debug
from common import database
from common import telegram
from common import telegram_utils
from common import text_utils
from bgw import bgw_utils
from tms import tms_utils

CMD_TMS = "/tms"
CMD_TMS_PROMPT = "Give me a Verse reference, or Pack and Verse number\n(P.S. you can even try giving me a topic)"
CMD_TMS_BADQUERY = "I can't find anything related to this, try another one?"

STATE_WAIT_TMS = "Waiting for TMS query"

def cmds(user, cmd, msg):
    if user is None:
        return False
    
    debug.log("Running TMS commands")

    try:
        result = (\
        cmd_tms(user, cmd, msg) \
        )
    except:
        debug.log("Exception in TMS Commands")
        return False
    return result

def states(user, msg):
    if user is None:
        return False

    debug.log("Running TMS states")
    
    try:
        result = ( \
        state_tms(user, msg)       \
        )
    except:
        debug.log("Exception in TMS States")
        return False
    return result

def resolve_tms_query(user, query):
    if user is not None:
        verse = None

        if text_utils.is_valid(query): 
            debug.log("Resolving TMS Query")

            verse_reference = bgw_utils.get_reference(query)
            if text_utils.is_valid(query):
                verse = tms_utils.query_verse_by_reference(verse_reference)
            
            if verse is None:
                verse = tms_utils.query_verse_by_pack_pos(query)

            if verse is None:
                verse = tms_utils.query_verse_by_topic(query)

            if verse is not None:
                passage = bgw_utils.get_passage_raw(verse.reference, user.get_version())
                verse_msg = tms_utils.format_verse(verse, passage)

                telegram.send_msg(verse_msg, user.get_uid())
                user.set_state(None)
            else:
                telegram.send_msg(CMD_TMS_BADQUERY, user.get_uid())
        else:
            telegram.send_msg_keyboard(CMD_TMS_PROMPT, user.get_uid())
            user.set_state(STATE_WAIT_TMS)

        return True

    return False

def cmd_tms(user, cmd, msg):
    if cmd == CMD_TMS:
        debug.log_cmd(cmd)

        query = msg.get("text").strip()
        query = query.replace(cmd, "")

        return resolve_tms_query(user, query)
    return False

def state_tms(user, msg):
    if user is not None and user.get_state() == STATE_WAIT_TMS:
        query = msg.get("text").strip()

        return resolve_tms_query(user, query)
    return False