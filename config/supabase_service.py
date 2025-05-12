# config/supabase_service.py
import os
from supabase import create_client, Client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
BUCKET_NAME = os.getenv("SUPABASE_BUCKET", "media")

def upload_imagem_supabase(caminho_arquivo, nome_no_bucket):
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise RuntimeError("Variáveis de ambiente do Supabase não estão configuradas")

    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    with open(caminho_arquivo, "rb") as f:
        supabase.storage.from_(BUCKET_NAME).upload(file=f, path=nome_no_bucket, upsert=True)

    url_publica = f"{SUPABASE_URL}/storage/v1/object/public/{BUCKET_NAME}/{nome_no_bucket}"
    return url_publica
