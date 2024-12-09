import hashlib
from scripts.conexao import Conexao

def hashConvertor(text):
    hash_obj = hashlib.sha256(text.encode())
    return hash_obj.hexdigest()

def validar_dados(email, senha):
    hashSenha = hashConvertor(senha)
    try:
        with Conexao() as minha_conexao:
            query = "SELECT * FROM usuario WHERE email = %s AND senha = %s"
            minha_conexao.cursor_dict.execute(query, (email, hashSenha))
            resultado = minha_conexao.cursor_dict.fetchone()
            return resultado is not None
    except Exception as e:
        print(f"Erro ao validar dados: {e}")
        return False
