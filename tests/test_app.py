from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_pagina_inicial_retorna_200_e_mensagem():
    # Arrange: cria o cliente de testes
    client = TestClient(app)

    # Act: faz a requisição GET na raiz
    response = client.get('/')

    # Assert: verifica o status e o conteúdo da resposta
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá, mundo! Bem-vindo à minha API.'}
