# Módulo de Controle de Estoque - ShopFast
# DEFEITOS PROPOSITAIS PARA INSPEÇÃO ESTÁTICA

import smtplib


class GerenciadorEstoque:
    """
    [Testabilidade] Instância de banco criada dentro da classe
    [Tratamento de Erros] Retorna None silenciosamente
    """

    def consultar_e_notificar(self, produto_id, quantidade_minima):
        """
        [Testabilidade] Função com 3 responsabilidades:
        1. Busca produto no banco (sem injeção de dependência)
        2. Calcula se precisa reabastecer
        3. Envia email de notificação
        """
        # [Testabilidade] Banco instanciado aqui, impossível mockar
        db = self._criar_conexao_banco()

        # Responsabilidade 1: Busca
        query = f"SELECT quantidade FROM produtos WHERE id = {produto_id}"
        estoque_atual = db.executar(query)

        # [Tratamento de Erros] Retorna None sem exceção ou log
        if estoque_atual is None:
            return None

        # Responsabilidade 2: Cálculo
        if estoque_atual < quantidade_minima:
            necessita_compra = True
            quantidade_necessaria = quantidade_minima - estoque_atual
        else:
            necessita_compra = False

        # Responsabilidade 3: Envio de email (misturado na mesma função)
        if necessita_compra:
            self._enviar_email_compras(produto_id, quantidade_necessaria)

        return {"produto": produto_id, "estoque": estoque_atual}

    def _criar_conexao_banco(self):
        """Simula conexão com banco (sem injeção)"""
        return MockDatabase()

    def _enviar_email_compras(self, produto_id, quantidade):
        """Simula envio de email"""
        pass


class MockDatabase:
    def executar(self, query):
        return 5
