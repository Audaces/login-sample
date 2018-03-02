# Login Audaces

Este projeto é um exemplo de como obter um token de acesso aos serviçoes Audaces através do Login Audaces.

Para utilizar o login Audaces é necessário possuir o `client_id` e a URL de redirecionamento já deve estar cadastrada na Audaces.

Este exemplo mostra o **fluxo implícito**, para saber mais detalhes sobre Autenticação basta verificar diretamente a documentação do openid.

https://openid.net/specs/openid-connect-core-1_0.html#Authentication

#### URL

Url para login/autenticação:  `https://login.audaces.com/core/connect/authorize`

#### Rodar o exemplo

O exemplo apenas depende da lib **Bottle** . Instalação: `pip install bottle` ou instalar através dos requirements: `pip install -r requirements.txt`

Rodar: `python app.py`

