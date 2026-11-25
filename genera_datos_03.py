import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from clases import Pais, Plataforma, Serie

from configuracion import cadena_base_datos


engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

with open("data/series.csv", encoding="utf-8") as f:

    datos = csv.DictReader(f)

    for fila in datos:

        pais = session.query(Pais).filter_by(
            nombre=fila["pais"]
        ).one()

        plataforma = session.query(Plataforma).filter_by(
            nombre=fila["plataforma"]
        ).one()

        serie = Serie(
            id=int(fila["id"]),
            titulo=fila["titulo"],
            genero=fila["genero"],
            anio_estreno=int(fila["anio_estreno"]),
            temporadas=int(fila["temporadas"]),
            pais=pais,
            plataforma=plataforma
        )

        session.add(serie)

session.commit()
session.close()
