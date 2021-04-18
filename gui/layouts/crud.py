from kivy.app import App
from kivy.properties import partial
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.togglebutton import ToggleButton

from entidades import cliente
from repositorio import clienteRepositorio


class ExclusaoPopup(Popup):
    pass


class MensagemPopup(Popup):
    pass


class BotarListagem(ToggleButton):
    def __init__(self, clienteID, clienteNome, clienteIdade, **kwargs):
        super(BotarListagem, self).__init__(**kwargs)
        self.idCliente = clienteID
        self.nomeCliente = clienteNome
        self.idadeCliente = clienteIdade
        self.text = self.nomeCliente + " " + self.idadeCliente
        self.group = 'clientes'

    def _do_release(self, *args):
        Principal().clienteSelecionado(self.idCliente)


class Principal(BoxLayout):
    idCliente = 0

    def __init__(self, **kwargs):
        super(Principal, self).__init__(**kwargs)
        self.listarClientes()

    def limparCampos(self):
        self.ids.nome.text = ' '
        self.ids.idade.text = ' '


    def clienteSelecionado(self, id):
        Principal.idCliente = id

    def removerCliente(self):
        id = Principal.idCliente
        popup = ExclusaoPopup()
        popup.funcao = partial(self.remover, id)
        popup.open()

    def remover(self, id):
        clienteRepositorio.ClienteRepositorio.removerCliente(id)
        self.listarClientes()

    def editarCliente(self):
        id = Principal.idCliente

        nome = self.ids.nome.text
        idade = self.ids.idade.text
        if nome == '' or idade == '':
            MensagemPopup().open()
        else:
            cli = cliente.Cliente(nome, idade)
            clienteRepositorio.ClienteRepositorio.editarCliente(id, cli)
            self.limparCampos()
            self.listarClientes()

    def cadastrarCliente(self):
        nome = self.ids.nome.text
        idade = self.ids.idade.text

        if nome == '' or idade == '':
            MensagemPopup().open()
        else:
            cli = cliente.Cliente(nome, idade)
            clienteRepositorio.ClienteRepositorio.inseirCliente(cli)
            self.limparCampos()
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
