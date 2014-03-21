from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config

from .models import Agenda, ItemAgenda
from .forms import AgendaForm, ItemAgendaForm


@view_config(route_name='home', renderer='templates/index.html')
def home(request):
    agendas = Agenda.all()
    return {'agendas': agendas}


@view_config(route_name='items', renderer='templates/items.html')
def items(request):
    items = ItemAgenda.filter_by(agenda_id=request.matchdict['agenda_id'])
    return {'items': items}


@view_config(route_name='new_agenda', renderer='templates/new_agenda.html')
@view_config(route_name='edit_agenda', renderer='templates/new_agenda.html')
def new_agenda(request):
    agenda = Agenda.by_id(request.matchdict.get('agenda_id')) or Agenda()
    form = AgendaForm(request.POST, agenda)

    if request.POST and form.validate():
        form.populate_obj(agenda)
        request.db.merge(agenda)
        return HTTPFound(request.route_url('home'))

    return {'form': form}


@view_config(route_name='new_item', renderer='templates/new_edit.html')
@view_config(route_name='edit_item', renderer='templates/new_edit.html')
def new_item(request):
    item = ItemAgenda.by_id(request.matchdict.get('item_id')) or ItemAgenda()
    form = ItemAgendaForm(request.POST, item)

    if request.POST and form.validate():
        form.populate_obj(item)
        item.agenda_id = request.matchdict['agenda_id']
        request.db.add(item)
        return HTTPFound(request.route_url('items',
            agenda_id=request.matchdict['agenda_id'])
        )

    return {'form': form}

@view_config(route_name='delete_item', renderer='json')
def delete_item(request):
    item = ItemAgenda.by_id(request.matchdict['item_id'])
    request.db.delete(item)
    return HTTPFound(request.route_url('items',
        agenda_id=request.matchdict['agenda_id'])
    )
