from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from practice_session import db


class AvocadoDb(db.Model):
    __tablename__ = 'avocado'
    avocado_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(1000))
    avgprice = db.Column(db.Float)
    totalvol = db.Column(db.Integer)
    avo_a = db.Column(db.Integer)
    avo_b = db.Column(db.Float)
    avo_c = db.Column(db.Float)
    type = db.Column(db.Integer, ForeignKey('avotype.typeid'))
    regionid = db.Column(db.Integer, ForeignKey('avoregion.regionid'))
    avo_region = relationship("Avoregion")
    avo_type = relationship("Avotype")


class Avoregion(db.Model):
    __tablename__ = 'avoregion'
    regionid = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(60))
    avocado = relationship("AvocadoDb")


class Avotype(db.Model):
    __tablename__ = 'avotype'
    typeid = db.Column(db.Integer, primary_key=True)
    type= db.Column(db.String(60))
    avocado = relationship("AvocadoDb")
