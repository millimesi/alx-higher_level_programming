#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from model_state import Base, State
from model_city import City
from relationship_city import Base, City
from relationship_state import State

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

    state_city = session.query(State).order_by(State.id).all()
    for state in state_city:
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('\t{}: {}'.format(city.id, city.name))
    session.close()
