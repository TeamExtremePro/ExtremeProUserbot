from sqlalchemy import Column, String
from sql_helper import SESSION, BASE


class PMPermit(BASE):
    __tablename__ = "pmpermit"
    username = Column(String(14), primary_key=True)
    reason = Column(String(127))

    def __init__(self, username, reason=""):
        self.username = username
        self.reason = reason


PMPermit.__table__.create(checkfirst=True)


def is_approved(username):
    try:
        return SESSION.query(PMPermit).filter(PMPermit.username == str(username)).one()
    except:
        return None
    finally:
        SESSION.close()


def approve(username, reason):
    adder = PMPermit(str(username), str(reason))
    SESSION.add(adder)
    SESSION.commit()


def disapprove(username):
    rem = SESSION.query(PMPermit).get(str(username))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()


def get_all_approved():
    rem = SESSION.query(PMPermit).all()
    SESSION.close()
    return rem
