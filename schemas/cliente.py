from pydantic import BaseModel
from typing import Optional, List
from model.cliente import Cliente

class ClienteSchema(BaseModel):
    """ Define como um novo cliente a ser inserido deve ser representado
    """
    id: int = 1
    nome: str = "Renato Lisboa da Silva"
    email: str = "renato@email.com.br"
    tel: str = 995978514


class ClienteBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do cliente.
    """
    #nome: str = "Teste"
    id: int = 1


class ListagemClientesSchema(BaseModel):
    """ Define como uma listagem de clientes será retornada.
    """
    cliente:List[ClienteSchema]


def apresenta_clientes(clientes: List[Cliente]):
    """ Retorna uma representação do cliente seguindo o schema definido em
        ClienteViewSchema.
    """
    result = []
    for cliente in clientes:
        result.append({
            "id": cliente.id,
            "nome": cliente.nome,
            "email": cliente.email,
            "tel": cliente.tel,
        })

    return {"clientes": result}


class ClienteViewSchema(BaseModel):
    """ Define como um cliente será retornado: cliente + comentários.
    """
    id: int = 1
    nome: str = "Renato Lisboa"
    email: str = "renato@mail.com"
    tel: str = "12345678"


class ClienteDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_cliente(cliente: Cliente):
    """ Retorna uma representação do cliente seguindo o schema definido em
        ClienteViewSchema.
    """
    return {
        "id": cliente.id,
        "nome": cliente.nome,
        "email": cliente.email,
        "tel": cliente.tel
    }
