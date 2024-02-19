#!/usr/bin/python3
"""
Start link class to table in database
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1],
                                  sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    new_state_name = 'Louisiana'
    new_state = State(name=new_state_name)
    session.add(new_state)
    session.commit()
    state = session.query(State).filter(State.name == new_state_name).all()
    if state:
        for result in state:
            print("{}".format(result.id))
    else:
        print("Not found")

    session.close()
