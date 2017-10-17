from shekels.t1 import session, User

u1 = User(name='osma', fullname='dupa')
session.add(u1)
session.commit()

