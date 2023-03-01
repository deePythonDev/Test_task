from sqlalchemy.orm import Session
from model import Test
import csv
import model
import os
import logging # Logging Added
from database import create_database_model

from config import SessionLocal, engine

db = SessionLocal()
try:

    model.Base.metadata.create_all(bind = engine)
except Exception as e:
    create_database_model()
    model.Base.metadata.create_all(bind = engine)

database_data=[]
csv_data=[]

with open(f'{os.path.dirname(__file__)}/test.csv', encoding ='unicode_escape') as csvfile:
    reader = csv.DictReader(csvfile)
    logging.critical("Updating database started....")
    for row in reader:
        try:
            PKobj = db.query(Test).filter_by(primKey=row['Field1']+row['Field2']).first()
            try:
                allobj = db.query(Test.primKey).all()
                if len(database_data)<=0:
                    database_data.extend(i[0] for i in allobj)
                csv_data.append(row["Field1"]+row["Field2"])

                if str(row['Field3']) != str(PKobj.field3) or str(row['Field4']) != str(PKobj.field4) or str(row['Field5']) != str(PKobj.field5):
                    logging.critical(f"{row['Field1']+row['Field2']} Value Updated....")
                    PKobj.field3 = row['Field3']
                    PKobj.field4 = row['Field4']
                    PKobj.field5 = row['Field5']
                    PKobj.iud = 'U'

            except Exception as e:
                if (isinstance(e,AttributeError)):
                    logging.critical(f"{row['Field1']+row['Field2']} Value Inserted....")
                _test = Test(primKey = row['Field1']+row['Field2'], field1 = row['Field1'], field2= row['Field2'],field3= row['Field3'],
                                field4= row['Field4'],field5= row['Field5'], iud= 'I')
                db.add(_test)
            finally:
                db.commit()
                db.close()
        except Exception as e:
            logging.error(str(e))
            db.close()

    for i in database_data:
        if (i not in csv_data):
            update = db.query(Test).filter_by(primKey=i).first()
            update.iud = "D"
    db.commit()
    db.close()


