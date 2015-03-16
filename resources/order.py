import falcon
from hooks.inputValidation import validate_required
from models.base import Orders


class OrderResource:

    def __init__(self):
        pass

    def on_get(self, req, resp, order_id=-1):
        order = Orders().getByID(order_id)

        resp.status = falcon.HTTP_200
        resp.body = order

    @falcon.before(validate_required(['quantity', 'model', 'name', 'address', 'city', 'state', 'zip']))
    def on_put(self, req, resp):
        inputs = req.context['doc']

        # todo abstract creation logic to the model
        order = Orders(status='new', quantity=inputs['quantity'], model=inputs['model'], name=inputs['name'],
                       address=inputs['address'], city=inputs['city'], state=inputs['state'],
                       zip=inputs['zip'])
        order.save()

        resp.body = order