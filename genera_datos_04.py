import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from clases import Pais, Serie, Actor

from configuracion import cadena_base_datos


engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

archivos = [
    "data/actores.csv",
    "data/actors.csv"
]

for archivo in archivos:

    with open(archivo, encoding="utf-8") as f:

        datos = csv.DictReader(f)

        for fila in datos:

            pais = session.query(Pais).filter_by(
                nombre=fila["pais"]
            ).one()

            serie = session.query(Serie).filter_by(
                titulo=fila["serie"]
            ).one()

            actor = Actor(
                id=int(fila["id"]),
                nombre=fila["nombre"],
                edad=int(fila["edad"]),
                rol=fila["rol"],
                pais=pais,
                serie=serie
            )

            session.add(actor)

session.commit()
session.close()
