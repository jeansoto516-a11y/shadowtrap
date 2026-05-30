from app.honeypot.command_logger import log_command


PROMPT = "root@ubuntu:~# "


def _response_for(command: str, username: str | None) -> str:
    normalized = command.strip()

    if not normalized:
        return ""
    if normalized in {"exit", "logout"}:
        return "logout\n"
    if normalized == "help":
        return "bash: help: no help topics match\n"
    if normalized == "whoami":
        return f"{username or 'root'}\n"
    if normalized == "pwd":
        return "/root\n"
    if normalized == "uname -a":
        return "Linux ubuntu 5.15.0-91-generic #101-Ubuntu SMP x86_64 GNU/Linux\n"
    if normalized == "ls":
        return "backup.sh  config  notes.txt\n"
    if normalized.startswith("cat "):
        return "Permission denied\n"
    if normalized.startswith("sudo "):
        return "[sudo] password for root: Sorry, try again.\n"

    return f"bash: {normalized}: command not found\n"


def run_fake_shell(channel, ip: str, port: int, username: str | None) -> None:
    channel.send("Welcome to Ubuntu 22.04.3 LTS\r\n")
    channel.send(PROMPT)

    buffer = ""

    while True:
        data = channel.recv(1024)
        if not data:
            break

        text = data.decode("utf-8", errors="ignore")

        for char in text:
            if char in {"\r", "\n"}:
                command = buffer.strip()
                buffer = ""
                channel.send("\r\n")

                if command:
                    log_command(ip, port, username, command)

                response = _response_for(command, username)
                channel.send(response.replace("\n", "\r\n"))

                if command in {"exit", "logout"}:
                    return

                channel.send(PROMPT)
            elif char == "\x7f":
                buffer = buffer[:-1]
            else:
                buffer += char
                channel.send(char)
