# Autenticação JWT com Django

Este repositório contém um modelo básico de autenticação utilizando JSON Web Tokens (JWT) em Django. Ele pode ser utilizado como base para projetos que requerem autenticação de usuários.

## Tecnologias Utilizadas

- Django
- Django REST Framework
- djangorestframework-simplejwt

## Instalação

1. Clone o repositório:

   ```bash
   git clone <URL do repositório>
   cd <nome do diretório>
   ```

2. Crie um ambiente virtual e ative-o:

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # Para Linux ou Mac
   myenv\Scripts\activate     # Para Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Faça as migrações do banco de dados:

   ```bash
   python manage.py migrate
   ```

5. Crie um superusuário:

   ```bash
   python manage.py createsuperuser
   ```

6. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

## Endpoints

### Obter Token

- **URL**: `/api/token/`
- **Método**: `POST`
- **Dados do Corpo**:
  ```json
  {
      "username": "<seu_username>",
      "password": "<sua_senha>"
  }
  ```

### Refresh Token

- **URL**: `/api/token/refresh/`
- **Método**: `POST`
- **Dados do Corpo**:
  ```json
  {
      "refresh": "<refresh_token_obtido_no_login>"
  }
  ```

### Acesso Protegido

- **URL**: `/autenticacao/protected/`
- **Método**: `GET`
- **Headers**:
  ```
  Authorization: Bearer <access_token_obtido_no_login>
  ```

## Observações

- Certifique-se de que `DEBUG = True` no arquivo de configurações do Django durante o desenvolvimento.
- Altere as configurações de CORS e permissões conforme necessário, dependendo do ambiente em que você está implantando a aplicação.
- Este modelo pode ser adaptado conforme a necessidade de cada projeto.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).