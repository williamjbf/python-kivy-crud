from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton

from entidades import cliente
from repositorio import clienteRepositorio


class BotarListagem(ToggleButton):
    def __init__(self, clienteID, clienteNome, clienteIdade, **kwargs):
        super(BotarListagem, self).__init__(**kwargs)
        self.idCliente = clienteID
        self.nomeCliente = clienteNome
        self.idadeCliente = clienteIdade
        self.text = self.nomeCliente + " " + self.idadeCliente
        self.group = 'clientes'


class Principal(BoxLayout):
    def __init__(self, **kwargs):
        super(Principal, self).__init__(**kwargs)
        self.listarClientes()


    def cadastrarCliente(self):
        nome = self.ids.nome.text
        idade = self.ids.idade.text

        cli = cliente.Cliente(nome, idade)
        clienteRepositorio.ClienteRepositorio.inseirCliente(cli)
        self.ids.nome.text = ' '
        self.ids.idade.text = ' '
        self.listarClientes()

    def listarClientes(self):
        self.ids.clientes.clear_widgets()
        clientes = clienteRepositorio.ClienteRepositorio.listarClientes()
        for i in clientes:
            id = str(i[0])
            nome = i[1]
            idade = str(i[2])
            self.ids.clientes.add_widget(BotarListagem(id, nome, idade))


class Crud(App):
    def build(self):
        return Principal()
