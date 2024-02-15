import threading

from sqlalchemy import Column, String

from RadiuxManager.modules.sql import BASE, SESSION


class RadiuxChats(BASE):
    __tablename__ = "Radiux_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


RadiuxChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_Radiux(chat_id):
    try:
        chat = SESSION.query(RadiuxChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def set_Radiux(chat_id):
    with INSERTION_LOCK:
        Radiuxchat = SESSION.query(RadiuxChats).get(str(chat_id))
        if not Radiuxchat:
            Radiuxchat = RadiuxChats(str(chat_id))
        SESSION.add(Radiuxchat)
        SESSION.commit()


def rem_Radiux(chat_id):
    with INSERTION_LOCK:
        Radiuxchat = SESSION.query(RadiuxChats).get(str(chat_id))
        if Radiuxchat:
            SESSION.delete(Radiuxchat)
        SESSION.commit()
