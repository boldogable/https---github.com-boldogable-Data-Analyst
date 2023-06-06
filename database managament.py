from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Create and connect to the database
engine = create_engine('sqlite:///database.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

Define the data table
class Data(Base):
tablename = 'data'
id = Column(Integer, primary_key=True)
name = Column(String)
age = Column(Integer)

Create the table if it doesn't exist
Base.metadata.create_all(engine)

Add data
data1 = Data(name='John', age=25)
data2 = Data(name='Alice', age=30)
session.add_all([data1, data2])
session.commit()

Query and print data
data = session.query(Data).all()
for d in data:
print(d.name, d.age)
