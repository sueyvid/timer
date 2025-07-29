from plyer import notification

def enviar_notificacao(titulo, mensagem):
    """Envia uma notificação do Windows 11."""
    notification.notify(
        title=titulo,
        message=mensagem,
        app_name="MeuApp",  # Nome do aplicativo (opcional)
        app_icon=None,  # Ícone do aplicativo (opcional)
        timeout=10,  # Tempo em segundos para a notificação desaparecer (opcional)
    )

# Exemplo de uso
if __name__ == "__main__":
    enviar_notificacao("Olá!", "Esta é uma notificação do Windows 11 com Python!")