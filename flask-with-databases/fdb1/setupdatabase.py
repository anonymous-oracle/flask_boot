from base4 import db, Puppy

# creates all the tables model--> db table

db.create_all()

sam = Puppy('sammy', 3)
frank = Puppy('frankie',4)

# # both will print a value of None since they are not added to the db yet
# print(sam.id)
# print(frank.id)


############################ADDING ROWS TO DATABASE###############################
db.session.add_all([sam, frank])

# OR

# db.session.add(sam)
# db.session.add(frank)
##################################################################################

db.session.commit() # save the changes
# print(sam.id)
# print(frank.id)
