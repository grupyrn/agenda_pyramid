from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from pyramid_jinja2 import renderer_factory

from .models import (
    DBSession,
    Base,
)

def db_session(request):
    """
    Essa funcao faz com que o session do sqlalchemy seja acessado
    no request:

    config.add_request_method(db_session, 'qualquer_nome', reify=True)

    db = request.qualquer_nome
    """
    session = DBSession()
    
    def cleanup(request):
        session.close()

    request.add_finished_callback(cleanup)
    return session

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.add_renderer('.html', renderer_factory)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_request_method(db_session, 'db', reify=True)

    # incluindo as rotas na config
    config.include('agenda.routes')
    return config.make_wsgi_app()
