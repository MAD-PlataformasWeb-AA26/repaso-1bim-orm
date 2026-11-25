import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from clases import Serie, Premio

from configuracion import cadena_base_datos


engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

with open("data/premios.csv", encoding="utf-8") as f:

    datos = csv.DictReader(f)

    for fila in datos:

        serie = session.query(Serie).filter_by(
            titulo=fila["serie"]
        ).one()

        premio = Premio(
            nombre_premio=fila["nombre_premio"],
            categoria=fila["categoria"],
            anio=int(fila["anio"]),
            serie=serie
        )

        session.add(premio)

session.commit()
session.close()
