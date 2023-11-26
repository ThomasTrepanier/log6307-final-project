upload_parser = api.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)

hostauth_create_fields = api.model(
    'HostAuthCreate', {
        'name': fields.String(description="The name of the instance", required=True),
        'username': fields.String(description="Username to connect", required=True),
        'password': fields.String(description="Password to connect", required=False)
    }
)

@api.route('/api/hostauth')
class HostAuthView(Resource):
    @api.expect(upload_parser, hostauth_create_fields)
    def post(self):
        args = upload_parser.parse_args()
        args.get('file')
        api.payload.get('name') # This line will cause a error
        return {'name': args.get('name')}, 201
