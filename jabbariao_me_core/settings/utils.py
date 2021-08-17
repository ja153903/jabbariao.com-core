import os
from typing import Dict

from dotenv import load_dotenv

load_dotenv()


def get_database_credentials() -> Dict[str, str]:
    return {
        'NAME': os.getenv('SUPABASE_NAME'),
        'USER': os.getenv('SUPABASE_USER'),
        'PASSWORD': os.getenv('SUPABASE_PASSWORD'),
        'HOST': os.getenv('SUPABASE_HOST'),
        'PORT': os.getenv('SUPABASE_PORT')
    }


def get_django_secret_key() -> str:
    return os.getenv('DJANGO_SECRET_KEY')
