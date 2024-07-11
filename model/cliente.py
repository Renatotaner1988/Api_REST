from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base


class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column("pk_cliente",Integer, primary_key=True, autoincrement=True)
    nome = Column(String(140))
    cep = Column(Integer)
    tel = Column(Integer)
    endereco = Column(String(500))
    numero = Column(Integer)
    bairro = Column(String(500))
    cidade = Column(String(500))
    estado = Column(String(500))
    data_insercao = Column(DateTime, default=datetime.now())


    def __init__(self, id:int, nome:str, cep:int, tel:int, endereco:str, numero:int, bairro:str, cidade:str, estado:str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Cliente

        Arguments:
            nome: nome do Cliente.
            cep: cep do Cliente
            tel: tel do Cliente
            data_insercao: data de quando o Cliente foi inserido à base
        """
        self.id = id
        self.nome = nome
        self.cep = cep
        self.tel = tel
        self.endereco = endereco
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado


        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

