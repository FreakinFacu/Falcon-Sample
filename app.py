import falcon

from wsgiref import simple_server
from resources import order

# Import required middleware
from middleware.Auth import AuthMiddleware
from middleware.RequireJSON import RequireJSON
from middleware.JSONTranslator import JSONTranslator


# Set up falcon api with middleware
app = falcon.API(middleware=[
    AuthMiddleware(),
    RequireJSON(),
    JSONTranslator(),
])

# Set up OrderResource to listen /order/ endpoint
orderResource = order.OrderResource()

app.add_route('/order/{order_id}', orderResource)
app.add_route('/order', orderResource)

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()