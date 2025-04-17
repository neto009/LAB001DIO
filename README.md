# LAB001DIO# E-Commerce - Cadastro de Produtos

Este projeto é uma aplicação web simples para cadastro e exibição de produtos, desenvolvida com [Streamlit](https://streamlit.io/). As imagens dos produtos são armazenadas no [Azure Blob Storage](https://azure.microsoft.com/en-us/products/storage/blobs/), e os dados dos produtos são salvos em um banco de dados SQL Server.

## Funcionalidades

- Cadastro de produtos com nome, preço, descrição e imagem.
- Upload de imagens para o Azure Blob Storage.
- Listagem dos produtos cadastrados com exibição das imagens.

## Requisitos

- Python 3.8+
- Conta no Azure com um Blob Storage configurado
- Banco de dados SQL Server acessível

## Instalação

1. Clone este repositório:
    ```sh
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd E-COMMERCE
    ```

2. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

3. Configure as variáveis de ambiente em um arquivo `.env`:
    ```
    CONNECTION_STRING=SuaConnectionStringDoBlob
    CONTAINER_NAME=SeuContainer
    ACCOUNT_NAME=SeuAccountName
    SQL_SERVER=SeuServidorSQL
    SQL_DATABASE=SeuBanco
    SQL_USERNAME=SeuUsuario
    SQL_PASSWORD=SuaSenha
    ```

4. Crie a tabela no SQL Server usando o script em [`infos.txt`](infos.txt).

## Uso

Execute o aplicativo com o comando:

```sh
streamlit run [main.py](http://_vscodecontentref_/0)