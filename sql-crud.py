from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the "Programmer" table - this is done after the sessions and declaritive db below
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)



# create a new varibale called session instead of connecting to the database directly

Session = sessionmaker(db)

# open an actual session by calling the Session() above

session = Session()

# create the database using declaritive_base sub class
base.metadata.create_all(db)

# create records on ur Programmer Table - This is done after the class programmer is created
ada_lovelace = Programmer(
    first_name = "Ada",
    last_name = "Lovelace",
    gender = "Female",
    nationality = "British",
    famous_for ="First Programmer"
)

alan_turning = Programmer(
    first_name = "Alan",
    last_name = "Turing",
    gender = "Male",
    nationality = "British",
    famous_for ="Modern Computing"
)

grace_hopper = Programmer(
    first_name = "Grace",
    last_name = "Hopper",
    gender = "Female",
    nationality = "American",
    famous_for ="COBOL Language"
)

margaret_hamilton = Programmer(
    first_name = "Margaret",
    last_name = "Hamilton",
    gender = "Female",
    nationality = "American",
    famous_for ="Apollo 11"
)

bill_gates = Programmer(
    first_name = "Bill",
    last_name = "Gates",
    gender = "Male",
    nationality = "American",
    famous_for ="Microsoft"
)

tim_berners_lee = Programmer(
    first_name = "Tim",
    last_name = "Berners-Lee",
    gender = "Male",
    nationality = "British",
    famous_for ="World Wide Web"
)

ben_williams = Programmer(
    first_name = "Ben",
    last_name = "Williams",
    gender = "Male",
    nationality = "British",
    famous_for ="Being Welsh"
)

# add each instance of our programmer to our session
#session.add(ada_lovelace) - this gets commented out after adding her to the db as to not duplicate our work
session.add(alan_turning)
session.add(grace_hopper)
session.add(margaret_hamilton)
session.add(bill_gates)
session.add(tim_berners_lee)
session.add(ben_williams)

# commit our session to the database
#session.commit()


# updating a single record
#programmer = session.query(programmer).filter_by(id=7).first()
#programmer.famous_for = "World President"

# commit our session to the database
session.commit()
# then run the file python3 sql-crud.py

#update multiple records - Commented out single record to avoid duplications
people = session.query(Programmer)
for person in people:
    if person.gender == "Female":
        person.gender = "F"
    elif person.gender == "Male":
        person.gender = "M"
    else:
        print("Gender not defined")
    session.commit()

# run this in the server with python3 sql-crud.py 

# query the database to find all programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep= " | "
    )

# once the programmers are added simply run the file python3 sql-crud.py