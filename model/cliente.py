from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base


class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column("pk_cliente",Integer, primary_key=True, autoincrement=True)
    nome = Column(String(140), unique=True)
    email = Column(String(140), unique=True)
    tel = Column(Integer)
    data_insercao = Column(DateTime, default=datetime.now())


    def __init__(self, id:int, nome:str, email:str, tel:int,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Cliente

        Arguments:
            nome: nome do Cliente.
            email: email do Cliente
            tel: tel do Cliente
            data_insercao: data de quando o Cliente foi inserido à base
        """
        self.id = id
        self.nome = nome
        self.email = email
        self.tel = tel

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

