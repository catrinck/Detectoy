# detectoyBackEnd
## 1. Como rodar o servidor na própria máquina

Eu recomendo que você crie um ambiente virtual para fazer isso :)

### 1.1 Abra o terminal no diretório do projeto

Abra o terminal no seu computador e depois use o seguinte comando:\
```cd <diretorio-do-projeto>```\
Onde está ```<diretorio-do-projeto>``` você deve pôr o caminho da pasta detectoyBackEnd no seu computador.\
No final o resultado deve ser algo semelhante a isso:\
```C:\Users\user\Detectoy\detectoyBackEnd```

### 1.2. Baixe os requisitos do projeto

Execute o seguinte comando no terminal (diretorio do projeto):\
```pip install -r requirements.txt```

### 1.3. Rodando o servidor

Execute o seguinte comando no terminal (diretorio do projeto):\
```python manage.py runserver```

## 2. Utilizando a API

Após ter iniciado o servidor, abra o navegador e acesse http://127.0.0.1:8000/.

### 2.1. GET e POST

Para utilizar os métodos GET e POST dos gerentes vá a http://127.0.0.1:8000/api/gerentes/. \
Para utilizar os métodos GET e POST dos usuários vá a http://127.0.0.1:8000/api/usuarios/. 

O GET é feito automaticamente ao entrar no site e aparece logo no início.

Logo abaixo do campo de GET, tem um espaço em que você pode escrever o POST. \
O POST é feito com o formato json da classe.\
Para criar um gerente, você coloca no campo de POST algo nesse formato:
```json
{
        "cpf": 99538199200,
        "nome": "Pedro Ituassú",
        "email": "pcmi.eng23@uea.edu.br",
        "senha": "xxxx"
}
```
Para criar um usuário, você coloca no campo de POST algo nesse formato:
```json
{
        "cpf": 99538199200,
        "nome": "Pedro Ituassú",
        "email": "pcmi.eng23@uea.edu.br",
        "senha": "xxxx",
        "cameras": false,
        "relatorios": false
    }
```

### 2.2. PUT e DELETE

Para utilizar os métodos PUT e DELETE dos gerentes vá a http://127.0.0.1:8000/api/gerentes/cpf \
Para utilizar os métodos PUT e DELETE dos gerentes vá a http://127.0.0.1:8000/api/gerentes/cpf \
No lugar de cpf você deve colocar o cpf do Gerente ou Usuário que deseja acessar.

Para utilizar o DELETE, aperte no botão DELETE na parte superior do site.

Da mesma maneira que na página de GET e POST, tem um espaço em que você pode escrever o PUT. \
O PUT é feito com o formato json da classe.\
Para modificar um gerente, você coloca no campo de PUT algo nesse formato:
```json
{
        "cpf": 99538199200,
        "nome": "Pedro Ituassú",
        "email": "pcmi.eng23@uea.edu.br",
        "senha": "pedroituassu"
}
```
Para modificar um usuário, você coloca no campo de PUT algo nesse formato:
```json
{
        "cpf": 99538199200,
        "nome": "Pedro Ituassú",
        "email": "pcmi.eng23@uea.edu.br",
        "senha": "xxxx",
        "cameras": false,
        "relatorios": false
    }
```