from temp.test1 import session, Address

a = Address(value="jakis adresww", user_id=1)
session.add(a)
session.commit()
