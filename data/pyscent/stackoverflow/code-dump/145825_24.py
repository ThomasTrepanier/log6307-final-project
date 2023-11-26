@api.route('/company')
class Company(Resource):

    def post(self, *args, **kwargs):
        """ Creating a new Company """
        data = request.get_json(force=True)
        schema = CompanySchema()
        if data:
            logger.info("Data got by /api/test/testId method %s" % data)

            # Validation with schema.load() OPTION_2
            company, errors = schema.load(data)
            print(company)

            if errors:
                return {"errors": errors}, 422

            company.save_to_db()
            return {"message": COMPANY_CREATED_SUCCESSFULLY}, 201
