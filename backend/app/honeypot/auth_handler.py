import paramiko


class SSHAuthHandler(paramiko.ServerInterface):

    # Método chamado quando alguém tenta login
    def check_auth_password(self, username, password):

        print("\n========== TENTATIVA DE LOGIN ==========")
        print(f"[USUARIO] {username}")
        print(f"[SENHA] {password}")
        print("========================================\n")

        # Sempre falha o login
        return paramiko.AUTH_FAILED

    # Permite autenticação por senha
    def get_allowed_auths(self, username):

        return "password"