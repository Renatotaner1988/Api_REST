# Minha API REST

Esse é um pequeno projeto simples que foca no exercício de consumo de uma API externa e aplicando as 5 rotas (POST, PUT, DELETE, GET.)

As principais tecnologias utilizadas foram:

- Flask
- SQLAlchemy
- OpenAPI3
- SQLite
## Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

Este comando instala as bibliotecas, descritas no arquivo `requirements.txt`.

```
pip install -r requirements.txt

```
Para executar a API  basta executar:

```
flask run --host 0.0.0.0 --port 5000

```


Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 


```
flask run --host 0.0.0.0 --port 5000 --reload

```


Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
