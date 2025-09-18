"""
EXEMPLOS COMPLETOS DE PYTHON
Este arquivo contém diversos exemplos de uso da linguagem Python
"""

# =============================================================================
# 1. HELLO WORLD E COMENTÁRIOS
# =============================================================================
print("=== 1. HELLO WORLD ===")
print("Hello, World!")  # Comentário de linha única
"""
Este é um comentário
de múltiplas linhas
"""

# =============================================================================
# 2. VARIÁVEIS E TIPOS DE DADOS
# =============================================================================
print("\n=== 2. VARIÁVEIS E TIPOS DE DADOS ===")
nome = "Alice"              # String
idade = 30                  # Inteiro
altura = 1.68               # Float
estudante = True            # Boolean
nomes = ["Ana", "João"]     # Lista
pessoa = {"nome": "Carlos", "idade": 25}  # Dicionário

print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}")
print(f"Estudante: {estudante}, Lista: {nomes}, Dicionário: {pessoa}")

# =============================================================================
# 3. ESTRUTURAS CONDICIONAIS
# =============================================================================
print("\n=== 3. ESTRUTURAS CONDICIONAIS ===")
idade = 18
if idade >= 18:
    print("Maior de idade")
elif idade >= 12:
    print("Adolescente")
else:
    print("Criança")

# Operador ternário
status = "Adulto" if idade >= 18 else "Menor"
print(f"Status: {status}")

# =============================================================================
# 4. LAÇOS DE REPETIÇÃO
# =============================================================================
print("\n=== 4. LAÇOS DE REPETIÇÃO ===")
# For loop
print("For loop:")
for i in range(5):
    print(f"Contagem: {i}")

# For com lista
frutas = ["maçã", "banana", "laranja"]
print("\nFrutas:")
for fruta in frutas:
    print(fruta)

# While loop
print("\nWhile loop:")
contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1

# =============================================================================
# 5. FUNÇÕES
# =============================================================================
print("\n=== 5. FUNÇÕES ===")
def saudacao(nome, hora="dia"):
    return f"Bom {hora}, {nome}!"

def calcular_media(*numeros):
    return sum(numeros) / len(numeros) if numeros else 0

# Chamando funções
print(saudacao("Maria"))
print(saudacao("Pedro", "tarde"))
print(f"Média: {calcular_media(7, 8, 9)}")

# Função lambda
quadrado = lambda x: x ** 2
print(f"Quadrado de 5: {quadrado(5)}")

# =============================================================================
# 6. MANIPULAÇÃO DE LISTAS E DICIONÁRIOS
# =============================================================================
print("\n=== 6. MANIPULAÇÃO DE LISTAS E DICIONÁRIOS ===")
# Listas
numeros = [1, 2, 3, 4, 5]
numeros.append(6)           # Adiciona elemento
numeros.remove(3)           # Remove elemento
numeros[0] = 10             # Modifica elemento

# List comprehension
pares = [x for x in numeros if x % 2 == 0]
quadrados = [x**2 for x in range(1, 6)]

print(f"Números: {numeros}")
print(f"Pares: {pares}")
print(f"Quadrados: {quadrados}")

# Dicionários
pessoa = {
    "nome": "Ana",
    "idade": 25,
    "cidade": "Rio de Janeiro"
}
pessoa["profissao"] = "Engenheira"  # Adiciona chave
del pessoa["cidade"]                # Remove chave

print(f"Dicionário: {pessoa}")

# =============================================================================
# 7. MANIPULAÇÃO DE ARQUIVOS
# =============================================================================
print("\n=== 7. MANIPULAÇÃO DE ARQUIVOS ===")
# Escrevendo em um arquivo
with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")

# Lendo um arquivo
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:")
    print(conteudo)

# Lendo linha por linha
with open("exemplo.txt", "r") as arquivo:
    print("Linhas do arquivo:")
    for linha in arquivo:
        print(linha.strip())

# =============================================================================
# 8. TRATAMENTO DE EXCEÇÕES
# =============================================================================
print("\n=== 8. TRATAMENTO DE EXCEÇÕES ===")
try:
    numero = int("abc")  # Isso vai causar um erro
except ValueError as e:
    print(f"Erro de valor: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
else:
    print("Nenhum erro ocorreu")
finally:
    print("Este bloco sempre é executado")

# =============================================================================
# 9. PROGRAMAÇÃO ORIENTADA A OBJETOS
# =============================================================================
print("\n=== 9. PROGRAMAÇÃO ORIENTADA A OBJETOS ===")
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        pass

class Cachorro(Animal):  # Herança
    def fazer_som(self):  # Polimorfismo
        return "Au Au!"
    
    def __str__(self):  # Método especial
        return f"Cachorro: {self.nome}"

# Criando objetos
meu_animal = Animal("Generic")
meu_cachorro = Cachorro("Rex")

print(meu_animal.nome)
print(meu_cachorro.fazer_som())
print(meu_cachorro)  # Usa o método __str__

# =============================================================================
# 10. MÓDULOS E BIBLIOTECAS
# =============================================================================
print("\n=== 10. MÓDULOS E BIBLIOTECAS ===")
import math
from datetime import datetime

# Usando math
print(f"Raiz quadrada de 16: {math.sqrt(16)}")
print(f"Pi: {math.pi}")

# Usando datetime
agora = datetime.now()
print(f"Data e hora atual: {agora}")
print(f"Ano: {agora.year}, Mês: {agora.month}, Dia: {agora.day}")

# =============================================================================
# 11. EXPRESSÕES REGULARES
# =============================================================================
print("\n=== 11. EXPRESSÕES REGULARES ===")
import re

texto = "Meu email é exemplo@email.com e meu telefone é (11) 99999-9999"

# Procurando email
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(email_pattern, texto)
print(f"Emails encontrados: {emails}")

# Procurando telefone
phone_pattern = r'\(\d{2}\) \d{5}-\d{4}'
phones = re.findall(phone_pattern, texto)
print(f"Telefones encontrados: {phones}")

# =============================================================================
# 12. TRABALHANDO COM JSON
# =============================================================================
print("\n=== 12. TRABALHANDO COM JSON ===")
import json

# Convertendo dicionário para JSON
dados = {
    "nome": "Maria",
    "idade": 30,
    "hobbies": ["leitura", "natação", "viagem"]
}

json_str = json.dumps(dados, indent=2)
print("JSON formatado:")
print(json_str)

# Convertendo JSON de volta para dicionário
dados_de_volta = json.loads(json_str)
print(f"Nome: {dados_de_volta['nome']}")

# =============================================================================
# 13. ITERAÇÕES E GERADORES
# =============================================================================
print("\n=== 13. ITERAÇÕES E GERADORES ===")
# Gerador simples
def contador(maximo):
    num = 0
    while num < maximo:
        yield num
        num += 1

# Usando o gerador
print("Gerador:")
for numero in contador(5):
    print(numero)

# =============================================================================
# 14. DECORADORES
# =============================================================================
print("\n=== 14. DECORADORES ===")
def meu_decorador(funcao):
    def wrapper(*args, **kwargs):
        print("Antes da função")
        resultado = funcao(*args, **kwargs)
        print("Depois da função")
        return resultado
    return wrapper

@meu_decorador
def dizer_ola(nome):
    print(f"Olá, {nome}!")

dizer_ola("João")

# =============================================================================
# 15. CONTEXT MANAGERS (COM STATEMENT)
# =============================================================================
print("\n=== 15. CONTEXT MANAGERS ===")
class MeuContextManager:
    def __enter__(self):
        print("Entrando no contexto")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saindo do contexto")
    
    def fazer_algo(self):
        print("Fazendo algo no contexto")

with MeuContextManager() as cm:
    cm.fazer_algo()

# =============================================================================
# 16. TESTES UNITÁRIOS (EXEMPLO BÁSICO)
# =============================================================================
print("\n=== 16. TESTES UNITÁRIOS ===")
import unittest

def somar(a, b):
    return a + b

class TestSomar(unittest.TestCase):
    def test_somar_positivos(self):
        self.assertEqual(somar(2, 3), 5)
    
    def test_somar_negativos(self):
        self.assertEqual(somar(-1, -1), -2)

# Executando os testes
if __name__ == "__main__":
    unittest.main(exit=False)  # exit=False para continuar a execução

# =============================================================================
# 17. EXEMPLOS AVANÇADOS
# =============================================================================
print("\n=== 17. EXEMPLOS AVANÇADOS ===")
# Enumerate
print("Enumerate:")
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")

# Zip
nomes = ["Ana", "João", "Maria"]
idades = [25, 30, 35]
print("\nZip:")
for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")

# Map
print("\nMap:")
numeros = [1, 2, 3, 4, 5]
dobros = list(map(lambda x: x * 2, numeros))
print(f"Dobros: {dobros}")

# Filter
print("\nFilter:")
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares: {pares}")

print("\n=== FIM DOS EXEMPLOS ===")