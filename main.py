import streamlit as st
from azure.storage.blob import BlobServiceClient
import os
import pyodbc
import uuid
import json
from dotenv import load_dotenv
load_dotenv()

blobConnectionString = os.getenv("CONNECTION_STRING")
blobContainerName = os.getenv("CONTAINER_NAME")
blobaccountName = os.getenv("ACCOUNT_NAME")

SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_USERNAME = os.getenv("SQL_USERNAME")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")

st.title("Cadastro de Produtos")

product_name = st.text_input("Nome do Produto")
product_price = st.number_input("Preço do Produto", min_value=0.0, format="%.2f")
product_description = st.text_area("Descrição do Produto")
product_image = st.file_uploader("Imagem do Produto", type=["jpg", "jpeg", "png"])

def get_sql_connection():
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={SQL_SERVER};"
        f"DATABASE={SQL_DATABASE};"
        f"UID={SQL_USERNAME};"
        f"PWD={SQL_PASSWORD}"
    )
    return pyodbc.connect(conn_str)

def insert_product(product_name, product_price, product_description, product_image):
    try:
        # Upload da imagem para o Azure Blob Storage
        if product_image is not None:
            blob_service_client = BlobServiceClient.from_connection_string(blobConnectionString)
            blob_client = blob_service_client.get_blob_client(container=blobContainerName, blob=str(uuid.uuid4()) + "_" + product_image.name)
            blob_client.upload_blob(product_image, overwrite=True)
            image_url = f"https://{blobaccountName}.blob.core.windows.net/{blobContainerName}/{blob_client.blob_name}"
        else:
            image_url = None

        conn = get_sql_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Produtos (nome, preco, descricao, imagem_url) VALUES (?, ?, ?, ?)",
                       (product_name, product_price, product_description, image_url))
        conn.commit()
        conn.close()
    except Exception as e:
        st.error(f"Erro ao cadastrar produto: {e}")
        return False
    return True

if st.button("Salvar"):
    insert_product(product_name, product_price, product_description, product_image)
    st.success("Produto salvo com sucesso!")

if st.button("Carregar Produtos"):
    try:
        conn = get_sql_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Produtos")
        produtos = cursor.fetchall()
        conn.close()
        for produto in produtos:
            st.write(f"ID: {produto[0]}")
            st.write(f"Nome: {produto[1]}")
            st.write(f"Preço: {produto[3]}")
            st.write(f"Descrição: {produto[2]}")
            st.image(produto[4])
            st.write("---")
    except Exception as e:
        st.error(f"Erro ao carregar produtos: {e}")
