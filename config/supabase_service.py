# config/supabase_service.py
import os
from supabase import create_client, Client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")  # use a chave de serviço
BUCKET_NAME = os.getenv("SUPABASE_BUCKET", "media")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def upload_imagem_supabase(caminho_arquivo, nome_no_bucket):
    with open(caminho_arquivo, "rb") as f:
        supabase.storage.from_(BUCKET_NAME).upload(file=f, path=nome_no_bucket, upsert=True)

    url_publica = f"{SUPABASE_URL}/storage/v1/object/public/{BUCKET_NAME}/{nome_no_bucket}"
    return url_publica
