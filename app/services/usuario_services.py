from models.usuario import Usuario
from repositories.usuario_repository import usuarioRepository

class UsuarioService:
    def __init__(self,repository: usuarioRepository) -> None:
        self.repository = repository

    def criar_usuario(self,nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email,senha=senha)
            self.repository.salvar_usuario(usuario)
            print("Usúario salvo com sucesso!")
        except TypeError as erro:
            print(f"Erro ao salvar o arquivo: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def listar_todos_usuarios(self):
        return self.repository.lista_todos_usuario()