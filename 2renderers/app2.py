from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config


@view_config(
    route_name='home', renderer='json')
def home(request):
    return{'a': 1, 'b': 2}


if __name__ == "__main__":
    with Configurator() as config:
        config.add_route('home', '/')
        config.scan()
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
