# Módulo de Pagamentos - ShopFast
# DEFEITOS PROPOSITAIS PARA INSPEÇÃO ESTÁTICA

# [Segurança] Chave de API hardcoded (exemplo fictício para fins de inspeção)
STRIPE_KEY = "sk_live_" + "x" * 30  # Demonstração de hardcoding (DEFEITO)


def proc(p, t):
    """
    [Nomenclatura] Nome vago 'proc'
    [Nomenclatura] Parâmetros 'p' e 't' ao invés de nomes descritivos
    """
    # [Nomenclatura] Variáveis com nomes inadequados
    v = p
    tx = t
    r = v * (1 + tx)

    # [Segurança] Exibindo dados sensíveis
    print(f"Processando pagamento com cartão: 4532-****-****-7821")
    print(f"CVV: 123")

    # [Tratamento de Erros] Falha silenciosa
    try:
        # Simular chamada à API Stripe
        if v < 0:
            raise ValueError("Valor negativo")
        resultado = integrar_gateway(v, r)
    except Exception:
        pass

    return r


def integrar_gateway(valor, taxa_aplicada):
    """Integração com gateway de pagamento (mock)"""
    return {"status": "processado", "valor_total": taxa_aplicada}
