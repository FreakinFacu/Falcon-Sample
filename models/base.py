from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/orders', echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class Orders(Base):
     __tablename__ = 'orders'

     id       = Column(Integer, primary_key=True)
     status   = Column(String(255))
     quantity = Column(Integer)
     model    = Column(String(255))
     name     = Column(String(255))
     address  = Column(String(255))
     city     = Column(String(255))
     state    = Column(String(2))
     zip      = Column(String(10))

     def __repr__(self):
        return '{"id":%s, state:"%s"}' % (self.id, self.state)

     def getByID(self, id):
         return session.query(Orders).filter(Orders.id == id).first()

     def save(self):
         session.add(self)
         session.commit()

     # todo look into using OrderedDict instead so that order is preserved
     def apiResponse(self):
        return {
            "id": self.id,
            "status": self.status,
            "quantity": self.quantity,
            "model": self.model,
            "name": self.name,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "zip": self.zip
        }
