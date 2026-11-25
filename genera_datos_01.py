import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from clases import Pais

from configuracion import cadena_base_datos


engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

archivos = [
    "data/paises.csv",
    "data/countries.csv"
]

for archivo in archivos:

    with open(archivo, encoding="utf-8") as f:

        datos = csv.DictReader(f)

        for fila in datos:

            pais = Pais(
                id=int(fila["id"]),
                nombre=fila["nombre"],
                continente=fila["continente"]
            )

            session.add(pais)

session.commit()
session.close()
