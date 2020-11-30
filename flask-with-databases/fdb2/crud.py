from base import db, Puppy

######################################################
# NOTE: TO RUN THIS SCRIPT AGAIN, DELETE THE SQLITE DB
######################################################

# create
mypuppy = Puppy('rufus', 5)
db.session.add(mypuppy)
db.session.commit()

# read
allpuppies = Puppy.query.all() # list of puppies objects in the table
# print(allpuppies)

# select by id
puppyone = Puppy.query.get(1)
# print(puppyone)

# filters
pupfrankie = Puppy.query.filter_by(name='frankie')
# print(pupfrankie.all())

# update
firstpup = Puppy.query.get(1)
firstpup.age = 10
db.session.add(firstpup)
db.session.commit()

# delete
secondpup = Puppy.query.get(2)
db.session.delete(secondpup)
db.session.commit()

# allpuppies = Puppy.query.all()
# print(allpuppies)


