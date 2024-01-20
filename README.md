# InventoryManager

## Pre-reqs

- O BackEnd do projeto foi criado usando Python v3.11.4 e Node.js v18.17.1
- O Banco de dados usado foi o MySQL.

## Running

### Banco
- Para utilizar as API's será necessário antes criar um banco de dados no localhost/phpmyadmin com o nome "userdb", caso não queira utilizar este banco pode criá-lo na ferramenta de sua preferência e após isso configurando os arquivos BackEnd\LoginApi\DataBank\dbConnection.py e BackEnd\StockApi\.env.

### BackEnd

#### Login Api
- Execute `pip install -r requirements.txt` para instalar os pacotes;
- Execute `py app.py` e o servidor irá iniciar.

#### StockApi
- Execute `npm install` para instalar os pacotes;
- Execute npm run dev;
