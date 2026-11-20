from http import HTTPStatus

from fastapi import FastAPI

app = FastAPI(title='Minha API com FastAPI')


@app.get('/', status_code=HTTPStatus.OK)
def pagina_inicial():
    return {'message': 'Olá, mundo! Bem-vindo à minha API.'}
