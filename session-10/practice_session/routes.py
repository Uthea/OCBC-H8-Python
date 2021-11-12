from flask import jsonify
from flask_pydantic import validate
from flask_restx import Resource, Namespace, abort

from practice_session import db
from practice_session.api_model import avocado_response_model, avocado_body_model, avocado_update_model
from practice_session.model import AvocadoDb
from practice_session.pydantic_model import AvocadoBodyModel

api = Namespace('Avocado', description='CRUD Avocado', path='/')


@api.route('/avocado')
class Avocado(Resource):
    @api.marshal_with(avocado_response_model)
    def get(self):
        avocados = AvocadoDb.query.limit(10).all()
        return avocados

    @api.expect(avocado_body_model)
    @api.response(201, 'created', avocado_response_model)
    @validate()
    def post(self, body: AvocadoBodyModel):
        new_avocado = AvocadoDb(
            date=body.date,
            avgprice=body.avgprice,
            totalvol=body.totalvol,
            avo_a=body.avo_a,
            avo_b=body.avo_b,
            avo_c=body.avo_c,
            type=body.type,
            regionid=body.regionid
        )

        db.session.add(new_avocado)
        db.session.commit()

        return new_avocado


@api.route('/avocado/<int:id>')
class ParamAvocado(Resource):
    @api.marshal_with(avocado_response_model, code=200)
    def get(self, id):
        avocado = AvocadoDb.query.get(id)
        if avocado is None:
            return abort(404, 'Id Not Found')
        return avocado

    @api.expect(avocado_update_model)
    @validate()
    def put(self, id, body: AvocadoBodyModel):
        avocado = AvocadoDb.query.get(id)
        if avocado is None:
            return abort(404, 'Id Not Found')

        avocado.date = body.date
        avocado.avgprice = body.avgprice
        avocado.totalvol = body.totalvol
        avocado.avo_a = body.avo_a
        avocado.avo_b = body.avo_b
        avocado.avo_c = body.avo_c
        avocado.type = body.type
        avocado.regionid = body.regionid

        db.session.commit()

        return jsonify('Update Success !')

    @validate()
    def delete(self, id):
        avocado = AvocadoDb.query.get(id)
        if avocado is None:
            return abort(404, 'Id Not Found')

        db.session.delete(avocado)
        db.session.commit()

        return jsonify('Delete Success !')


