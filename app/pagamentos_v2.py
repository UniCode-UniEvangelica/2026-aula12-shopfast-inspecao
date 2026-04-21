STRIPE_KEY = "sk_live_" + "x" * 30


def proc(p, t):
    v = p
    tx = t
    r = v * (1 + tx)

    print(f"Processando pagamento com cartão: 4532-****-****-7821")
    print(f"CVV: 123")

    try:
        if v < 0:
            raise ValueError("Valor negativo")
        resultado = integrar_gateway(v, r)
    except Exception:
        pass

    return r


def integrar_gateway(valor, taxa_aplicada):
    return {"status": "processado", "valor_total": taxa_aplicada}
