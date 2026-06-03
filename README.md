# 🐍 Estudos Python — Tratamento de Exceções

Repositório dedicado ao estudo prático de **exceções em Python**: captura de erros, fluxo try/except/else/finally e criação de exceções personalizadas.

---

## 📁 Estrutura do Projeto

```
📦 python-excecoes
 ┣ 📄 diviPorZero.py            # Captura de ZeroDivisionError
 ┣ 📄 tryExceptElseFinally.py   # Fluxo completo try/except/else/finally
 ┗ 📄 exceçaoPersonalizada.py   # Criação e uso de exceção customizada
```

---

## 📌 Descrição dos Arquivos

### `diviPorZero.py`
Demonstra como capturar o erro `ZeroDivisionError` em duas situações:

- Divisão fixa por zero com retorno `None`
- Divisão com input do usuário usando o fluxo completo `try/except/else/finally`

---

### `tryExceptElseFinally.py`
Demonstra o fluxo completo de tratamento de exceções ao tentar abrir um arquivo:

| Bloco | Comportamento |
|---|---|
| `try` | Tenta abrir o arquivo |
| `except` | Captura `FileNotFoundError` se o arquivo não existir |
| `else` | Executa se nenhum erro ocorreu |
| `finally` | Executa sempre, independente do resultado |

---

### `exceçaoPersonalizada.py`
Criação de uma exceção personalizada (`idadeValidaError`) que herda de `Exception`:

- Lança o erro se a idade for `<= 0` ou `> 150`
- Valida se o usuário é maior ou menor de idade
- Captura a exceção customizada com `except`

---

## 🚀 Como executar

**Pré-requisito:** Python 3 instalado.

1. Clone o repositório:
```bash
git clone https://github.com/lu1z-st/python-excecoes.git
cd python-excecoes
```

2. Execute os scripts individualmente:
```bash
python diviPorZero.py
python tryExceptElseFinally.py
python exceçaoPersonalizada.py
```

---

## 🧠 Conceitos Praticados

- Captura de exceções com `try/except`
- Fluxo completo `try/except/else/finally`
- Criação de exceções personalizadas com `class` herdando `Exception`
- Uso do `raise` para lançar exceções manualmente
- Tratamento de `ZeroDivisionError` e `FileNotFoundError`

---

## 👨‍💻 Autor

**Luiz Paulo Soares**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-luiz--paulo--soares-blue?logo=linkedin)](https://linkedin.com/in/luiz-paulo-soares)
[![Instagram](https://img.shields.io/badge/Instagram-lu1z__st-E4405F?logo=instagram&logoColor=white)](https://instagram.com/lu1z_st)

---

> Projeto desenvolvido como parte dos estudos de lógica de programação e Python. 🚀
> 
