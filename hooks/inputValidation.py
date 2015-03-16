import falcon


def validate_required(inputs):

    def hook(req, resp, resource, params):
        doc = req.context['doc']

        if type(inputs) is list:
            for input_name in inputs:
                check_exists(input_name, doc)
        else:
            check_exists(inputs, doc)

    def check_exists(input_name, doc):
        if input_name not in doc:
            raise falcon.HTTPError(falcon.HTTP_400, 'Missing Field',
                                   input_name + " field missing")

    return hook
