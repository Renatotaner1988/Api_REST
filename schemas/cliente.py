from pydantic import BaseModel
from typing import Optional, List
from model.cliente import Cliente

class ClienteSchema(BaseModel):
    """ Define como um novo cliente a ser inserido deve ser representado
    """
    id: int = 1
    nome: str = "Renato Lisboa da Silva"
    cep: int= 25010390
    tel: int = 995978514
    endereco: str = "Rua José Lages de Barros"
    numero: int = 50
    bairro: str = "Vila Ideal"
    cidade: str = "Duque de Caxias"
    estado: str = "RJ"




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
            "cep": cliente.cep,
            "tel": cliente.tel,
            "endereco": cliente.endereco,
            "numero": cliente.numero,
            "bairro": cliente.bairro,
            "cidade": cliente.cidade,
            "estado": cliente.estado,
        })

    return {"clientes": result}


class ClienteViewSchema(BaseModel):
    """ Define como um cliente será retornado: cliente
    """
    id: int = 1
    nome: str = "Renato Lisboa"
    cep: int = 25010390
    tel: int = 995849316
    endereco: str = "Rua José Lages de Barros"
    numero: int = 50
    bairro: str = "Vila Ideal"
    cidade: str = "Duque de Caxias"
    estado: str = "RJ"


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
        "cep": cliente.cep,
        "tel": cliente.tel,
        "endereco": cliente.endereco,
        "numero": cliente.numero,
        "bairro": cliente.bairro,
        "cidade": cliente.cidade,
        "estado": cliente.estado,
        
    }
