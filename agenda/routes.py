
def includeme(config):
    """
    Quando entender como funciona, voce pode terminar a app.
    O que falta?
    Deletar uma agenda
    

    add_route(nome_da_rota, url)
    config.scan(view_file)
    Depois de definidas as rotas, o scan verifica se os route_name das Views
    que existem na package definida, batem com as do arquivo route em questao 
    """
    config.add_route('home', '/')
    config.add_route('items', '/items/{agenda_id}')
    config.add_route('new_agenda', '/new_agenda')
    config.add_route('edit_agenda', '/edit_agenda/{agenda_id}')
    config.add_route('new_item', '/items/{agenda_id}/new_item')
    config.add_route('edit_item', '/items/{agenda_id}/edit_item/{item_id}')
    config.add_route('delete_item', '/items/{agenda_id}/delete_item/{item_id}')

    config.scan('agenda.views')
