Agenda Pyramid
==============

Agenda criada com Pyramid + sqlalchemy + Jinja2

Começando
---------------
```
cd < directory containing this file >
$venv/bin/python setup.py develop #instala as dependencias do projeto
$venv/bin/initialize_agenda_db development.ini #inicia o banco de dados (vulgo syncdb do Django)
$venv/bin/pserve development.ini --reload
```

###Tecnologias Usadas

1 - Pyramid - http://docs.pylonsproject.org/projects/pyramid/en/latest/

2 - SqlAlchemy - http://sqlalchemy.org

3 - Jinja2 - http://jinja.pocoo.org

4 - WTForms (WTForms-Alchemy - http://wtforms-alchemy.readthedocs.org ) - http://wtforms.readthedocs.org/en/latest/index.html


O WTForms lembra muito os forms do Django, então vai ficar simples para a galera que conhece o Django trabalhar com ele. E o WTForms-Alchemy é uma alternativa mais simples de trabalhar em conjunto com o SqlAlchemy, não falo mais sobre os dois por que eu conheci recentemente :)
