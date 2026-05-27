from abc import ABC, abstractmethod


class Notificador(ABC):
    @abstractmethod
    def notificar(self, mensagem):
        pass


class NotificadorEmail(Notificador):
    def notificar(self, mensagem):
        print(f"[E-mail] {mensagem}")


class NotificadorSms(Notificador):
    def notificar(self, mensagem):
        print(f"[SMS] {mensagem}")


class NotificadorWhatsApp(Notificador):
    def notificar(self, mensagem):
        print(f"[WhatsApp] {mensagem}")


class Pedido:
    def __init__(self, notificador):
        self.notificador = notificador

    def finalizar(self):
        self.notificador.notificar("Pedido finalizado com sucesso.")


if __name__ == "__main__":
    Pedido(NotificadorEmail()).finalizar()
    Pedido(NotificadorSms()).finalizar()
    Pedido(NotificadorWhatsApp()).finalizar()
