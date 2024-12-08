from scripts.conexao import Conexao
from scripts.modelo import *


class UsuarioDAO:  

    @staticmethod
    def buscar_todos() -> list:
        with Conexao() as conexao:
            conexao.cursor_dict.execute("SELECT * FROM usuario")
            usuarios_data = conexao.cursor_dict.fetchall()
        return usuarios_data

    @staticmethod
    def mudar_dados(usuario: Usuario):
        with Conexao() as conexao:
            sql = """
                UPDATE usuario 
                SET nome = %s, senha = %s, cpf = %s, email = %s, data_nasc = %s, data_entrada = %s
                WHERE numero_matricula = %s
            """
            valores = (usuario.nome, usuario.senha, usuario.cpf, usuario.email, 
                       usuario.data_nasc, usuario.data_entrada, usuario.numero_matricula)
            conexao.cursor.execute(sql, valores)
            conexao.conn.commit()

    @staticmethod
    def salvar_usuario(usuario: Usuario):
        with Conexao() as conexao:
            sql = """
                INSERT INTO usuario 
                (nome, senha, cpf, email, data_nasc, data_entrada, numero_matricula) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            valores = (usuario.nome, usuario.senha, usuario.cpf, usuario.email, 
                       usuario.data_nasc, usuario.data_entrada, usuario.numero_matricula)
            conexao.cursor.execute(sql, valores)
            conexao.conn.commit()

    @staticmethod
    def buscar_id_por_email(email: str) -> list:
        with Conexao() as conexao:
            query = "SELECT * FROM usuario WHERE email = %s"
            conexao.cursor_dict.execute(query, (email,))
            pergunta_data = conexao.cursor_dict.fetchall()
            
        if pergunta_data:
            return pergunta_data[0]["numero_matricula"]
        else:
            return None

    @staticmethod
    def buscar_por_id(id):
        with Conexao() as conexao:
            query = "SELECT * FROM usuario WHERE numero_matricula = %s"
            conexao.cursor_dict.execute(query, (id,))
            pergunta_data = conexao.cursor_dict.fetchall()

        if pergunta_data:
            return pergunta_data[0]
        else:
            return None


class PerguntaDAO:  

    @staticmethod
    def buscar_todos() -> list:
        with Conexao() as conexao:
            conexao.cursor_dict.execute("SELECT * FROM pergunta")
            pergunta_data = conexao.cursor_dict.fetchall()
        return pergunta_data
    
    @staticmethod
    def deletar_pergunta(id_pergunta):
        try:
            with Conexao() as conexao:
                query = "DELETE FROM pergunta WHERE idpergunta = %s"
                conexao.cursor_dict.execute(query, (id_pergunta,))
                conexao.conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao deletar pergunta: {e}")
            return False

    @staticmethod
    def buscar_por_matricula(numero) -> list:
        with Conexao() as conexao:
            query = "SELECT * FROM pergunta WHERE estudante = %s"
            conexao.cursor_dict.execute(query, (numero,))
            pergunta_data = conexao.cursor_dict.fetchall()
        return pergunta_data
    
    @staticmethod
    def buscar_por_categoria(categoria) -> list:
        with Conexao() as conexao:
            query = "SELECT * FROM pergunta WHERE categoria = %s"
            conexao.cursor_dict.execute(query, (categoria,))
            pergunta_data = conexao.cursor_dict.fetchall()
        return pergunta_data
    
    @staticmethod
    def buscar_por_id(idpergunta) -> list:
        with Conexao() as conexao:
            query = "SELECT * FROM pergunta WHERE idpergunta = %s"
            conexao.cursor_dict.execute(query, (idpergunta,))
            pergunta_data = conexao.cursor_dict.fetchall()
        return pergunta_data

    @staticmethod
    def salvar_pergunta(pergunta: Pergunta):
        with Conexao() as conexao:
            sql = """
                INSERT INTO pergunta 
                (idpergunta, titulo, pergunta, estudante, categoria) 
                VALUES (%s, %s, %s, %s, %s)
            """
            valores = (pergunta.idpergunta, pergunta.titulo, pergunta.pergunta, 
                       pergunta.estudante, pergunta.categoria)
            conexao.cursor.execute(sql, valores)
            conexao.conn.commit()


class RespostaDAO:  

    @staticmethod
    def buscar_todos() -> list:
        with Conexao() as conexao:
            conexao.cursor_dict.execute("SELECT * FROM resposta")
            resposta_data = conexao.cursor_dict.fetchall()
        return resposta_data
    
    @staticmethod
    def deletar_resposta(id_resposta):
        try:
            with Conexao() as conexao:
                query = "DELETE FROM resposta WHERE idresposta = %s"
                conexao.cursor_dict.execute(query, (id_resposta,))
                conexao.conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao deletar resposta: {e}")
            return False
    
    @staticmethod
    def salvar_resposta(resposta: Resposta):
        with Conexao() as conexao:
            sql = """
                INSERT INTO resposta 
                (idresposta, pergunta_referente, texto, estudante) 
                VALUES (%s, %s, %s, %s)
            """
            valores = (resposta.idresposta, resposta.pergunta_referente, 
                       resposta.texto, resposta.estudante)
            conexao.cursor.execute(sql, valores)
            conexao.conn.commit()

    @staticmethod
    def buscar_por_idpergunta(idpergunta) -> list:
        with Conexao() as conexao:
            query = "SELECT * FROM resposta WHERE pergunta_referente = %s"
            conexao.cursor_dict.execute(query, (idpergunta,))
            pergunta_data = conexao.cursor_dict.fetchall()
        return pergunta_data
    
    @staticmethod
    def buscar_por_numero_matricula(numero_matricula) -> list:
        with Conexao() as conexao:
            query = "SELECT * FROM resposta WHERE estudante = %s"
            conexao.cursor_dict.execute(query, (numero_matricula,))
            pergunta_data = conexao.cursor_dict.fetchall()
        return pergunta_data
