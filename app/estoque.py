class GerenciadorEstoque:

    def consultar_e_notificar(self, produto_id, quantidade_minima):
        db = self._criar_conexao_banco()

        query = f"SELECT quantidade FROM produtos WHERE id = {produto_id}"
        estoque_atual = db.executar(query)

        if estoque_atual is None:
            return None

        if estoque_atual < quantidade_minima:
            necessita_compra = True
            quantidade_necessaria = quantidade_minima - estoque_atual
        else:
            necessita_compra = False

        if necessita_compra:
            self._enviar_email_compras(produto_id, quantidade_necessaria)

        return {"produto": produto_id, "estoque": estoque_atual}

    def _criar_conexao_banco(self):
        return MockDatabase()

    def _enviar_email_compras(self, produto_id, quantidade):
        pass


class MockDatabase:
    def executar(self, query):
        return 5
