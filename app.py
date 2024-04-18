from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Cliente
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
cliente_tag = Tag(name="Cliente", description="Adição, visualização e remoção de clientes à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/cliente', tags=[cliente_tag],
          responses={"200": ClienteViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_cliente(form: ClienteSchema):
    """Adiciona um novo Cliente à base de dados

    Retorna uma representação dos clientes e comentários associados.
    """
    cliente = Cliente(
        id=None,
        nome=form.nome,
        email=form.email,
        tel=form.tel)
    logger.debug(f"Adicionando cliente de nome: '{cliente.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando cliente
        session.add(cliente)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado cliente de nome: '{cliente.nome}'")
        return apresenta_cliente(cliente), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Cliente de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar cliente '{cliente.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar cliente '{cliente.nome}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.put('/cliente', tags=[cliente_tag],
          responses={"200": ClienteViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def update_cliente(form: ClienteSchema):
    """Atualiza um Cliente na base de dados

    Retorna uma representação dos clientes.
    """
    cliente = Cliente(
        id=form.id,
        nome=form.nome,
        email=form.email,
        tel=form.tel)
    logger.debug(f"Adicionando cliente de nome: '{cliente.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando cliente
        #session.update(cliente).Cliente.id == cliente_id
        #session.query(Cliente).filter(Cliente.id == cliente.id).update(cliente)
        cliente_upd = session.query(Cliente).filter(Cliente.id == cliente.id).first()

        cliente_upd.nome = cliente.nome
        cliente_upd.email = cliente.email
        cliente_upd.tel = cliente.tel

        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Atualizado cliente de nome: '{cliente.nome}'")
        return apresenta_cliente(cliente), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Cliente de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar cliente '{cliente.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = e
        logger.warning(f"Erro ao adicionar cliente '{cliente.nome}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/clientes', tags=[cliente_tag],
         responses={"200": ListagemClientesSchema, "404": ErrorSchema})
def get_clientes():
    """Faz a busca por todos os Cliente cadastrados

    Retorna uma representação da listagem de clientes.
    """
    logger.debug(f"Coletando clientes ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    clientes = session.query(Cliente).all()

    if not clientes:
        # se não há clientes cadastrados
        return {"clientes": []}, 200
    else:
        logger.debug(f"%d rodutos econtrados" % len(clientes))
        # retorna a representação de cliente
        print(clientes)
        return apresenta_clientes(clientes), 200


@app.get('/cliente', tags=[cliente_tag],
         responses={"200": ClienteViewSchema, "404": ErrorSchema})
def get_cliente(query: ClienteBuscaSchema):
    """Faz a busca por um Cliente a partir do id do cliente

    Retorna uma representação dos clientes e comentários associados.
    """
    cliente_id = query.id
    logger.debug(f"Coletando dados sobre cliente #{cliente_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not cliente:
        # se o cliente não foi encontrado
        error_msg = "Cliente não encontrado na base :/"
        logger.warning(f"Erro ao buscar cliente '{cliente_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Cliente econtrado: '{cliente.nome}'")
        # retorna a representação de cliente
        return apresenta_cliente(cliente), 200


@app.delete('/cliente', tags=[cliente_tag],
            responses={"200": ClienteDelSchema, "404": ErrorSchema})
def del_cliente(query: ClienteBuscaSchema):
    """Deleta um Cliente a partir do nome de cliente informado

    Retorna uma mensagem de confirmação da remoção.
    """
    cliente_id = query.id
    print(cliente_id)
    logger.debug(f"Deletando dados sobre cliente #{cliente_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Cliente).filter(Cliente.id == cliente_id).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado cliente #{cliente_id}")
        return {"mesage": "Cliente removido", "id": cliente_id}
    else:
        # se o cliente não foi encontrado
        error_msg = "Cliente não encontrado na base :/"
        logger.warning(f"Erro ao deletar cliente #'{cliente_id}', {error_msg}")
        return {"mesage": error_msg}, 404
