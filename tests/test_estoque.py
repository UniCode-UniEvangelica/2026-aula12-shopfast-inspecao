import unittest
from app.estoque import GerenciadorEstoque


class TestEstoque(unittest.TestCase):

    def setUp(self):
        self.gerenciador = GerenciadorEstoque()

    def test_consulta_estoque(self):
        resultado = self.gerenciador.consultar_e_notificar(1, 10)
        assert resultado is not None

    def test_relatorio_basico(self):
        resultado = self.gerenciador.consultar_e_notificar(999, 5)
        pass


if __name__ == "__main__":
    unittest.main()
