from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from clases import Actor, Serie, Plataforma, Pais

from configuracion import cadena_base_datos


engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

print("EJEMPLOS DE CONSULTAS")

print("""Obtener todos los actores que participan en series
transmitidas por plataformas de Estados Unidos""")

actores = session.query(Actor).\
    join(Serie).\
    join(Pais).\
    filter(Pais.nombre == "Estados Unidos").all()

print("--------------------------------")
for a in actores:
    print("%s" % (a))
    print("Serie: %s" % (a.serie.titulo))
    print("Plataforma: %s" % (a.serie.plataforma.nombre))
    print("País: %s" % (a.serie.pais.nombre))
    print("---------")
print("--------------------------------")

session.close()
