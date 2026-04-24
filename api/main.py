import os
from typing import Any

import mysql.connector
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pymongo.errors import PyMongoError


app = FastAPI()


def get_mysql_conn():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "db_mysql"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        database=os.getenv("MYSQL_DATABASE", "myapp"),
        user=os.getenv("MYSQL_USER", "appuser"),
        password=os.getenv("MYSQL_PASSWORD", ""),
    )


def get_mongo_client() -> MongoClient:
    uri = os.getenv("MONGO_URI")
    if not uri:
        raise RuntimeError("MONGO_URI manquant")
    return MongoClient(uri, serverSelectionTimeoutMS=3000)


@app.get("/posts")
def posts() -> dict[str, list[dict[str, Any]]]:
    db_name = os.getenv("MONGO_DB", "blog_db")
    try:
        client = get_mongo_client()
        db = client[db_name]
        docs = list(db["posts"].find({}, {"_id": 0}))
        return {"posts": docs}
    except PyMongoError as e:
        raise HTTPException(status_code=503, detail=f"Mongo indisponible: {e.__class__.__name__}") from e


@app.get("/users")
def users() -> dict[str, list[dict[str, Any]]]:
    try:
        conn = get_mysql_conn()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, name, email, created_at FROM utilisateur ORDER BY id ASC")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return {"utilisateurs": rows}
    except mysql.connector.Error as e:
        raise HTTPException(status_code=503, detail=f"MySQL indisponible: {e.__class__.__name__}") from e

