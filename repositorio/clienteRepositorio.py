from fabricas import fabricaConexao


class ClienteRepositorio():

    @staticmethod
    def listarClientes():
        fabrica = fabricaConexao.FabricaConexao.conectar()
        try:
            cursor = fabrica.cursor()
            cursor.execute("SELECT * FROM cliente")
            return cursor.fetchall()
        finally:
            fabrica.close()

    @staticmethod
    def inseirCliente(cliente):
        fabrica = fabricaConexao.FabricaConexao.conectar()
        try:
            cursor = fabrica.cursor()
            cursor.execute("INSERT INTO cliente (nome,idade) VALUES(%s, %s)",
                         (cliente.nome, cliente.idade))
        finally:
            fabrica.close()

    @staticmethod
    def editarCliente(idCliente, cliente):
        fabrica = fabricaConexao.FabricaConexao.conectar()
        try:
            cursor = fabrica.cursor()
            cursor.execute("UPDATE cliente SET nome=%(nome)s, idade =%(idade)s where idcliente = %(idCliente)",
                         ({'nome': cliente.nome, 'idade': cliente.idade, 'idCliente': idCliente}))
        finally:
            fabrica.close()

    @staticmethod
    def removerCliente(idCliente):
        fabrica = fabricaConexao.FabricaConexao.conectar()
        try:
            cursor = fabrica.cursor()
            cursor.execute("DELETE FROM cliente WHERE idcliente=%s", (idCliente,))
        finally:
            fabrica.close()
