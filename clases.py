from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Base = declarative_base()


class Pais(Base):
    __tablename__ = 'pais'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)
    continente = Column(String(100), nullable=False)

    plataformas = relationship("Plataforma", back_populates="pais")
    series = relationship("Serie", back_populates="pais")
    actores = relationship("Actor", back_populates="pais")

    def __repr__(self):
        return "%s - %s" % (self.nombre, self.continente)


class Plataforma(Base):
    __tablename__ = 'plataforma'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)
    suscriptores_millones = Column(Float, nullable=False)

    pais_id = Column(Integer, ForeignKey('pais.id'), nullable=False)

    pais = relationship("Pais", back_populates="plataformas")
    series = relationship("Serie", back_populates="plataforma")

    def __repr__(self):
        return "%s - %.2f millones de suscriptores" % (
            self.nombre,
            self.suscriptores_millones
        )


class Serie(Base):
    __tablename__ = 'serie'

    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)
    genero = Column(String(100), nullable=False)
    anio_estreno = Column(Integer, nullable=False)
    temporadas = Column(Integer, nullable=False)

    plataforma_id = Column(
        Integer, ForeignKey('plataforma.id'), nullable=False
    )

    pais_id = Column(
        Integer, ForeignKey('pais.id'), nullable=False
    )

    plataforma = relationship("Plataforma", back_populates="series")
    pais = relationship("Pais", back_populates="series")
    actores = relationship("Actor", back_populates="serie")
    premios = relationship("Premio", back_populates="serie")

    def __repr__(self):
        return "%s - %s - %d" % (
            self.titulo,
            self.genero,
            self.anio_estreno
        )


class Actor(Base):
    __tablename__ = 'actor'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    edad = Column(Integer, nullable=False)
    rol = Column(String(100), nullable=False)

    pais_id = Column(Integer, ForeignKey('pais.id'), nullable=False)
    serie_id = Column(Integer, ForeignKey('serie.id'), nullable=False)

    pais = relationship("Pais", back_populates="actores")
    serie = relationship("Serie", back_populates="actores")

    def __repr__(self):
        return "%s - %d años - %s" % (
            self.nombre,
            self.edad,
            self.rol
        )


class Premio(Base):
    __tablename__ = 'premio'

    id = Column(Integer, primary_key=True)
    nombre_premio = Column(String(150), nullable=False)
    categoria = Column(String(100), nullable=False)
    anio = Column(Integer, nullable=False)

    serie_id = Column(Integer, ForeignKey('serie.id'), nullable=False)

    serie = relationship("Serie", back_populates="premios")

    def __repr__(self):
        return "%s - %s - %d" % (
            self.nombre_premio,
            self.categoria,
            self.anio
        )


Base.metadata.create_all(engine)
