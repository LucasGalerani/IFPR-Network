from scripts.conexao import Conexao
import hashlib

def hashConvertor(text):
    hash_obj = hashlib.sha256(text.encode())
    hash_resultado = hash_obj.hexdigest()
    return hash_resultado

def validar_dados(email, senha):
    hashSenha = hashConvertor(senha)
    minha_conexao = Conexao()
    query = "SELECT * FROM usuario WHERE email = %s AND senha = %s"
    minha_conexao.cursor.execute(query, (email, hashSenha))
    resultado = minha_conexao.cursor.fetchone()
    if resultado is None:
        return False
    else:
        return True