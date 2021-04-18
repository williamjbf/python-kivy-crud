from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from entidades import cliente
from repositorio import clienteRepositorio


class Principal(BoxLayout):
    def cadastrarCliente(self):
        nome = self.ids.nome.text
        idade = self.ids.idade.text

        cli = cliente.Cliente(nome, idade)
        clienteRepositorio.ClienteRepositorio.inseirCliente(cli)
        self.ids.nome.text = ' '
        self.ids.idade.text = ' '
        clienteRepositorio.ClienteRepositorio.listarClientes()

class Crud(App):
    def build(self):
        return Principal()

