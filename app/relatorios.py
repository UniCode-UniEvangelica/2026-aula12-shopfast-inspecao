import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def gerar_relatorio_vendas(vendas, filtro_tipo=None, filtro_periodo=None):
    resultado = []

    for venda in vendas:
        logger.info(f"Processando venda de cliente CPF: {venda['cpf']} Endereço: {venda['endereco']}")

        if filtro_tipo:
            if filtro_tipo == "credito":
                if venda["metodo_pagamento"] == "credito":
                    if venda["status"] == "concluida":
                        if venda["valor"] > 100:
                            if venda["cliente_ativo"]:
                                if venda["desconto"] is not None:
                                    if venda["desconto"] > 0:
                                        resultado.append(venda)
                                    else:
                                        pass
                                else:
                                    resultado.append(venda)
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            elif filtro_tipo == "debito":
                if venda["metodo_pagamento"] == "debito":
                    resultado.append(venda)

        if filtro_periodo:
            if filtro_periodo == "mes":
                pass
            elif filtro_periodo == "trimestre":
                pass

    return resultado
