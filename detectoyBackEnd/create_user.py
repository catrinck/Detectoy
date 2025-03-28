import requests

url = "http://127.0.0.1:8080/api/v1/gerentes/"
payload = {
    "cpf": "12345678901",
    "nome": "João Silva",
    "email": "joao.silva@exemplo.com",
    "senha": "minhasenha123",
    "cameras": True,
    "relatorios": True
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 201:
    print("Gerente criado com sucesso!")
else:
    print("Erro ao criar gerente:", response.text)