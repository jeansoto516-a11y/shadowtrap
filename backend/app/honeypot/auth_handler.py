import paramiko

from app.honeypot.command_logger import log_login_attempt


class SSHAuthHandler(paramiko.ServerInterface):
    def __init__(self, client_ip: str, client_port: int):
        self.client_ip = client_ip
        self.client_port = client_port
        self.username = None
        self.shell_requested = False

    def check_auth_password(self, username, password):
        self.username = username
        log_login_attempt(self.client_ip, self.client_port, username, password)
        return paramiko.AUTH_SUCCESSFUL

    def get_allowed_auths(self, username):
        return "password"

    def check_channel_request(self, kind, chanid):
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED

        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_channel_pty_request(
        self,
        channel,
        term,
        width,
        height,
        pixelwidth,
        pixelheight,
        modes,
    ):
        return True

    def check_channel_shell_request(self, channel):
        self.shell_requested = True
        return True
