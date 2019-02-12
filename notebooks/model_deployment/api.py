#!/usr/bin/python
from flask import Flask
from flask_restplus import Api, Resource, fields
from sklearn.externals import joblib
from m09_model_deployment import predict_proba

app = Flask(__name__)

api = Api(
    app, 
    version='1.0', 
    title='Phishing Prediction API',
    description='Phishing Prediction API')

ns = api.namespace('predict', 
     description='Phishing Classifier')
   
parser = api.parser()

parser.add_argument(
    'URL', 
    type=str, 
    required=True, 
    help='URL to be analyzed', 
    location='args')

resource_fields = api.model('Resource', {
    'result': fields.String,
})

@ns.route('/')
class PhishingApi(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        
        return {
         "result": predict_proba(args['URL'])
        }, 200
    
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=8888)
