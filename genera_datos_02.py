import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from clases import Pais, Plataforma

from configuracion import cadena_base_datos


engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

with open("data/plataformas.csv", encoding="utf-8") as f:

    datos = csv.DictReader(f)

    for fila in datos:

        pais = session.query(Pais).filter_by(
            nombre=fila["pais"]
        ).one()

        plataforma = Plataforma(
            id=int(fila["id"]),
            nombre=fila["nombre"],
            suscriptores_millones=float(fila["suscriptores_millones"]),
            pais=pais
        )

        session.add(plataforma)

session.commit()
session.close()
