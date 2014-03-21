from wtforms_alchemy import ModelForm
from wtforms_components import DateField
from agenda.models import Agenda, ItemAgenda

class AgendaForm(ModelForm):
    class Meta:
        model = Agenda

class ItemAgendaForm(ModelForm):
    class Meta:
        model = ItemAgenda
    data = DateField('Data', format='%d/%m/%Y')
