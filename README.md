# ShopFast — Repositório de Inspeção | Aula 12

## Objetivo

Este repositório contém código Python **propositalmente defeituoso** do sistema ShopFast. O objetivo é praticar **inspeção estática** — análise de código sem executar, sem fazer commits, sem abrir pull requests.

Os alunos devem identificar e rastrear **todos os defeitos** a uma das 4 categorias do checklist da aula:

1. **Nomenclatura** — nomes vagos, variáveis sem significado
2. **Testabilidade** — dificuldades para criar testes
3. **Segurança** — exposição de dados sensíveis, hardcoding de chaves
4. **Tratamento de Erros** — falhas silenciosas, exceções genéricas

## Clone do Repositório

```bash
git clone https://github.com/UniCode-UniEvangelica/2026-aula12-shopfast-inspecao.git
cd 2026-aula12-shopfast-inspecao
```

## Estrutura de Arquivos

```
app/
  ├── pagamentos_v2.py      # Módulo de pagamentos com defeitos
  ├── estoque.py            # Módulo de estoque com defeitos
  └── relatorios.py         # Módulo de relatórios com defeitos
tests/
  └── test_estoque.py       # Testes incompletos propositalmente
```

## ⚠️ AVISO IMPORTANTE

**Este repositório é SOMENTE LEITURA para os alunos.**

- ❌ Não faça commits
- ❌ Não abra pull requests
- ❌ Não modifique nenhum arquivo

Sua tarefa é **analisar** o código, não alterá-lo.

## Como Usar Esta Atividade

1. Clone o repositório
2. Abra os arquivos em `app/` e `tests/`
3. Identifique **cada defeito** no código
4. Classifique cada defeito em uma das 4 categorias
5. Documente suas descobertas no formulário de atividade

## Referência

**Disciplina:** Teste de Software | 2026.1  
**Professor:** Carlos Roberto Gomes Júnior  
**Universidade:** Universidade Evangélica de Brasília
