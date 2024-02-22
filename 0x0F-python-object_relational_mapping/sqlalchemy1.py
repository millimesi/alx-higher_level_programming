#!/usr/bin/python3
import sqlalchemy
#connecting with the database
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
#declare Mapping
from sqlalchemy.orm import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    def __repr__(self):
       return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                            self.name, self.fullname, self.nickname)
print(repr(User.__table__))

#create database tables defined by the models (classes) 
#mapped to SQLAlchemy's declarative base Base, 
#and it creates them in the specified database engine engine.
print(Base.metadata.create_all(engine))

#creating end user
ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')

#Creating a session 
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

#above Session is associated with our SQLite-enabled Engine, but it hasn’t opened any connections yet. 
session = Session()

#adding object session.add() to our Session
#At this point, we say that the instance is pending;
#no SQL has yet been issued and the object is not yet represented by a row in the database. 
session.add(ed_user)

#query
our_user = session.query(User).filter_by(name='ed').first()
print(our_user)

#We can add more User objects at once using add_all()
session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Flintstone', nickname='freddy')])

#can change the object attribute
ed_user.nickname = 'eddie'

#to see modifiyed object
session.dirty

#to see new objects pending
session.new 

# issue all remaining changes to the database and commit the transaction
#Session.commit() flushes the remaining changes to the database, and commits the transaction. 
session.commit()

#undoes all the changes made within the current transaction,
#reverting the database to its state before the transaction began
session.rollback()

#check if an object is in session
fake_user in session

### Quering ###
for instance in session.query(User).order_by(User.id):
    print(instance.name, instance.fullname)

for name, fullname in session.query(User.name, User.fullname):
    print(name, fullname)

for row in session.query(User, User.name).all():
    print(row.User, row.name)

#deleting a object/row
session.delete(ed_user)

session.close()