# create entries into db
from models import db, Puppy, Owner, Toy

# creating two puppies
rufus = Puppy('rufus')
fido = Puppy('fido')

# add puppies to db
db.session.add_all([rufus,fido])
db.session.commit()

# check
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='rufus').first()

# create owner object
jose = Owner('jose', rufus.id)

# give rufus toys
toy1 = Toy('chew toy', rufus.id)
toy2 = Toy('ball', rufus.id)

db.session.add_all([jose, toy1, toy2])
db.session.commit()

# grab rufus after those additions
rufus = Puppy.query.filter_by(name='rufus').first()
print(rufus.owner)
print(rufus)

print(rufus.report_toys())
print(rufus.owner)
