from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/home')
    config.add_route('index', '/')
    config.add_route('authenticate', '/auth')
    config.add_route('boards', '/boards')
    config.add_route('lists', '/board/{board_id}/lists')
    config.add_route('cards', '/board/{board_id}/cards')
    config.scan()
    return config.make_wsgi_app()