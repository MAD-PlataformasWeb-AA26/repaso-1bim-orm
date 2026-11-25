from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from clases import Pais, Plataforma

from configuracion import cadena_base_datos


engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

print("EJEMPLOS DE CONSULTAS")

print("Ejemplo 19")
print("Presentar cada país con sus respectivas plataformas")

paises = session.query(Pais).all()

print("--------------------------------")
for p in paises:
    print("%s" % (p))
    for plataforma in p.plataformas:
        print("\t%s" % (plataforma))
    print("---------")
print("--------------------------------")

session.close()
