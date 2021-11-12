from practice_session import api
from flask_restx import fields

avocado_body_model = api.model(
    'Avocado Body',
    {
        'date': fields.String("2017-01-04"),
        'avgprice': fields.Float(3.22),
        'totalvol': fields.Integer(32200),
        'avo_a': fields.Integer(6464),
        'avo_b': fields.Float(53634.7),
        'avo_c': fields.Float(121234.3),
        'type': fields.Integer(1),
        'regionid': fields.Integer(5)
    }
)

avocado_update_model = api.model(
    'Avocado Update/Delete',
    {
        'date': fields.String("2017-01-04"),
        'avgprice': fields.Float(3.22),
        'totalvol': fields.Integer(32200),
        'avo_a': fields.Integer(6464),
        'avo_b': fields.Float(53634.7),
        'avo_c': fields.Float(121234.3),
        'type': fields.Integer(1),
        'regionid': fields.Integer(5)
    }
)


avocado_response_model = api.model(
    'Avocado Response',
    {
        'avocado_id' : fields.Integer(),
        'date': fields.String(),
        'avgprice': fields.Float(),
        'totalvol': fields.Integer(),
        'avo_a': fields.Integer(),
        'avo_b': fields.Float(),
        'avo_c': fields.Float(),
        'region_name': fields.String(attribute="avo_region.region"),
        'type_name': fields.String(attribute="avo_type.type"),
    }
)



