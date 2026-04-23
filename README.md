# RACK+

Sistema web em Django para gerenciamento de salas, racks e devices.

## Funcionalidades

- Login com autenticacao
- Dashboard com resumo do sistema
- Cadastro e listagem de salas
- Cadastro e listagem de racks por sala
- Cadastro e listagem de devices por rack
- Pagina de detalhe do device com bateria, armazenamento e auditoria
- Tela de movimentacoes
- Interface responsiva para desktop e mobile
- API REST para devices

## Tecnologias

- Python
- Django
- Django REST Framework
- WhiteNoise
- SQLite

## Como instalar e rodar

1. Clone o repositorio.
2. Crie e ative um ambiente virtual.
3. Instale as dependencias:

```bash
pip install -r requirements.txt
```

4. Rode as migrations:

```bash
python manage.py migrate
```

5. Colete os arquivos estaticos:

```bash
python manage.py collectstatic --noinput
```

6. Inicie o servidor:

```bash
python manage.py runserver
```

7. Acesse no navegador:

```text
http://127.0.0.1:8000/
```

## Usuario administrador

Se ainda nao existir um usuario, crie com:

```bash
python manage.py createsuperuser
```

Depois use esse login para acessar o sistema.

## Rotas principais

- `/` - login
- `/app/` - dashboard
- `/app/homepage/` - salas
- `/app/sala/<id>/` - racks da sala
- `/app/rack/<id>/` - devices do rack
- `/app/device/<id>/` - detalhe do device
- `/app/movimentacoes/` - auditoria e movimentacoes
- `/api/devices/` - API REST de devices

## Observacoes

- O projeto usa `base.html` nas paginas principais.
- As rotas internas exigem autenticacao.
- Para refletir mudancas no CSS com `DEBUG = False`, rode novamente:

```bash
python manage.py collectstatic --noinput
```

## Estrutura do projeto

- `core/models.py` - modelos
- `core/views.py` - views web
- `core/api_views.py` - API REST
- `core/templates/` - templates HTML
- `core/static/core/` - arquivos CSS e imagens
- `core/urls.py` - rotas da aplicacao
- `rackplus/settings.py` - configuracoes do Django

