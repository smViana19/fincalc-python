# FinCalc - Sistema de Cálculos Financeiros em Python

def calcular_juros_simples(
    capital: float,
    taxa_anual: float,
    anos: int
) -> float:
    """Calcula o montante final obtido por juros simples."""
    juros = capital * (taxa_anual / 100) * anos
    return capital + juros


def calcular_aposentadoria(
    patrimonio_atual: float,
    aporte_mensal: float,
    anos: int,
    taxa_anual: float
) -> float:
    """Calcula o patrimônio acumulado para aposentadoria."""
    meses = anos * 12
    taxa_mensal = (taxa_anual / 100) / 12
    saldo = patrimonio_atual

    for _ in range(meses):
        saldo = (saldo + aporte_mensal) * (1 + taxa_mensal)

    return saldo


def calcular_juros_compostos(
    capital: float,
    taxa_anual: float,
    anos: int
) -> float:
    """Calcula o montante final obtido por juros compostos."""
    if capital < 0:
        raise ValueError("O capital não pode ser negativo.")
    if taxa_anual < 0:
        raise ValueError("A taxa anual não pode ser negativa.")
    if anos < 0:
        raise ValueError("O número de anos não pode ser negativo.")
    montante = capital * ((1 + (taxa_anual / 100)) ** anos)
    return montante


def calcular_irrf(
    salario_bruto: float
) -> float:
    """Calcula a alíquota simplificada de Imposto de Renda Retido na Fonte."""

    if salario_bruto <= 2259.20:
        return 0.0

    elif salario_bruto <= 2826.65:
        return (salario_bruto * 0.075) - 169.44

    elif salario_bruto <= 3751.05:
        return (salario_bruto * 0.15) - 381.44

    else:
        return (salario_bruto * 0.225) - 662.77


def calcular_lucro_liquido(
    receita_total: float,
    custos_totais: float,
    despesas_totais: float
) -> float:
    """Calcula o lucro líquido de uma operação."""
    return receita_total - custos_totais - despesas_totais


def calcular_margem_operacional(
    receita_total: float,
    custos_totais: float,
    despesas_operacionais: float
) -> float:
    """Calcula a margem operacional percentual."""
    lucro_operacional = (
        receita_total
        - custos_totais
        - despesas_operacionais
    )

    if receita_total == 0:
        return 0.0

    return (lucro_operacional / receita_total) * 100


def calcular_valor_futuro(
    aporte_mensal: float,
    taxa_mensal: float,
    meses: int
) -> float:
    """Calcula o valor futuro acumulado com aportes mensais recorrentes."""
    i = taxa_mensal / 100
    vf = aporte_mensal * (((1 + i) ** meses - 1) / i)
    return vf


def calcular_depreciacao_linear(
    valor_inicial: float,
    valor_residual: float,
    vida_util_anos: int
) -> float:
    """Calcula o valor de depreciação anual de um ativo corporativo."""
    return (valor_inicial - valor_residual) / vida_util_anos


if __name__ == "__main__":
    print("Iniciando o sistema FinCalc...")

    patrimonio = calcular_aposentadoria(
        10000.0,
        500.0,
        20,
        6.0
    )
    print(f"Patrimônio Estimado para Aposentadoria: R$ {patrimonio:.2f}")

    montante = calcular_juros_simples(1000.0, 5.0, 2)
    print(f"Juros Simples: R$ {montante:.2f}")
    montante_comp = calcular_juros_compostos(1000.0, 5.0, 2)
    print(f"Juros Compostos: R$ {montante_comp:.2f}")
    valor_futuro = calcular_valor_futuro(10.0, 5.0, 2)
    print(f"Valor futuro: R$ {valor_futuro:.2f}")

    # Teste do cálculo de lucro líquido
    receita = 10000.0
    custos = 4000.0
    despesas = 2000.0

    lucro_liquido = calcular_lucro_liquido(
        receita,
        custos,
        despesas
    )

    print(f"Lucro Líquido: R$ {lucro_liquido:.2f}")

    margem_operacional = calcular_margem_operacional(
        receita,
        custos,
        despesas
    )

    print(f"Margem Operacional: {margem_operacional:.2f}%")

    calculo_irrf = calcular_irrf(1000.0)
    print(f"Calculo imposto de renda: R$ {calculo_irrf:.2f}")

    calculo_depreciacao_linear = calcular_depreciacao_linear(1000.0, 200.0, 2)
    print(f"Calculo depreciacao linear: R$ {calculo_depreciacao_linear:.2f}")
