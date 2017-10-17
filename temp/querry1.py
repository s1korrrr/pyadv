from temp.test1 import session, User

u1 = User(name='trzecia', fullname='dupa')
session.add(u1)
session.commit()

