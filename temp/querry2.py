from temp.test1 import session, User

q = session.query(User).join(
    Address
)
print(q)

for x in q:
    print("USER!!")
    print(x.id)
    print(x.name)
    print(x.fullname)