# Detectoy - Sistema de Detecção de Defeitos em Maquininhas

O Detectoy é um sistema para detecção automática de defeitos em maquininhas de pagamento, utilizando visão computacional com YOLO para identificar telas quebradas e carcaças danificadas em tempo real.

## Estrutura do Projeto

O projeto está dividido em duas partes principais:

### Backend (Python/FastAPI)
- API RESTful para gerenciamento de usuários, autenticação e detecções
- Integração com modelo YOLO para processamento de imagens
- Serviço de webcam para captura em tempo real
- Comunicação via WebSockets para streaming de vídeo
- Sistema de relatórios e histórico de detecções

### Frontend (React/JavaScript)
- Interface de usuário moderna e responsiva
- Dashboard para visualização de detecções em tempo real
- Gerenciamento de usuários (gerentes e funcionários)
- Visualização de histórico e relatórios
- Organização por setores

## Pré-requisitos

### Backend
- Python 3.8+
- PostgreSQL 13+

### Frontend
- Node.js 14+
- npm 6+

## Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/Detectoy.git
cd Detectoy
```

### 2. Configure o ambiente backend
```bash
# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

# Instale as dependências
pip install -r detectoyBackEnd/requirements.txt
```

### 3. Configure o ambiente frontend
```bash
cd detectoy-front-end
npm install
```

### 4. Configure o banco de dados PostgreSQL
- Instale PostgreSQL se ainda não estiver instalado
- Crie um banco de dados chamado "detectoy"
- Configure o arquivo .env na raiz do projeto com suas credenciais

Exemplo de arquivo .env:
```
DATABASE_URL=postgresql://postgres:postgres@127.0.0.1:8000/detectoy
SECRET_KEY=sua_chave_secreta_aqui
MODEL_PATH=models/thebest.pt
```

### 5. Prepare o modelo YOLO
- Baixe ou treine um modelo YOLO para detecção de defeitos
- Coloque o arquivo do modelo em `models/thebest.pt`
- Se você não tiver um modelo, o sistema funcionará sem detecções, mas ainda poderá capturar imagens

## Configuração do Banco de Dados

Execute o script de configuração do banco de dados para criar as tabelas necessárias:

```bash
cd Detectoy
python detectoyBackEnd/db_setup.py
```

## Executando o Sistema

### 1. Inicie o backend
```bash
cd Detectoy
python detectoyBackEnd/run.py
```
O servidor FastAPI será iniciado em http://127.0.0.1:8080

### 2. Inicie o frontend
```bash
cd detectoy-front-end
npm start
```
O aplicativo React será iniciado em http://localhost:3000

## Uso do Sistema

### Acesso ao Sistema
1. Acesse http://localhost:3000 no navegador
2. Faça login com as credenciais (CPF/Email e senha)
   - Gerentes têm acesso a todas as funcionalidades
   - Funcionários têm acesso limitado, configurável pelo gerente

### Funcionalidades Principais

#### Detecção de Defeitos
- Visualização em tempo real da câmera com detecção automática de defeitos
- Histórico de detecções com timestamp e imagens salvas
- Classificação entre tela quebrada e carcaça quebrada

#### Gerenciamento de Usuários
- Criação, edição e remoção de gerentes e funcionários
- Configuração de permissões por tipo de usuário
- Autenticação segura com JWT

#### Relatórios
- Geração de relatórios por período, tipo de defeito ou setor
- Visualização das estatísticas de detecções
- Exportação de dados

#### Organização por Setores
- Criação e gerenciamento de setores
- Associação de câmeras a setores específicos
- Visualização de detecções por setor

## Arquitetura Técnica

### Backend
- **FastAPI**: Framework web de alta performance
- **SQLAlchemy**: ORM para interação com o banco de dados
- **Pydantic**: Validação de dados e serialização
- **YOLO**: Modelo de detecção de objetos em tempo real
- **OpenCV**: Processamento de imagens e captura de vídeo
- **WebSockets**: Comunicação em tempo real com o frontend

### Frontend
- **React**: Biblioteca JavaScript para construção de interfaces
- **Axios**: Cliente HTTP para comunicação com a API
- **TailwindCSS**: Framework CSS para estilização
- **React Router**: Navegação entre páginas

## Resolução de Problemas

### Erro de conexão com o banco de dados
- Verifique se o PostgreSQL está em execução na porta correta (8000)
- Verifique as credenciais no arquivo .env
- Execute o script db_setup.py novamente

### Erro no modelo de detecção
- Verifique se o arquivo do modelo existe em models/thebest.pt
- O sistema funcionará mesmo sem o modelo, mas sem realizar detecções

### Problemas de WebSockets ou streaming
- Certifique-se de que as portas 8080 estão abertas e acessíveis
- Verifique se a câmera está conectada e funcionando
