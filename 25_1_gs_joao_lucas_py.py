# -*- coding: utf-8 -*-
"""25.1.GS.JOAO.LUCAS.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14j9-kTRgWwBY2WyMyw7GKWcZJlOR9ekH
"""

tipos_desastres = []
paises = []
cidades = []
bairros = []
ruas = []
total_afetados = []
criancas = []
adultos = []
idosos = []
mobilidade_reduzida = []
feridos = []

quantidade = int(input("Quantos desastres você quer registrar? "))


for i in range(quantidade):
    print(f"\nDesastre {i + 1}:")

    tipos_desastres.append(input("Tipo de desastre: "))
    paises.append(input("País: "))
    cidades.append(input("Cidade: "))
    bairros.append(input("Bairro: "))
    ruas.append(input("Rua: "))

    while True:
        total = int(input("Quantidade total de pessoas afetadas: "))
        c = int(input("Quantidade de crianças: "))
        a = int(input("Quantidade de adultos: "))
        idoso = int(input("Quantidade de idosos: "))
        m = int(input("Quantidade de pessoas com mobilidade reduzida: "))
        f = int(input("Quantidade de feridos: "))

        soma = c + a + idoso + m + f

        if soma == total:
            total_afetados.append(total)
            criancas.append(c)
            adultos.append(a)
            idosos.append(idoso)
            mobilidade_reduzida.append(m)
            feridos.append(f)
            break
        else:
            print("\n Erro: A soma das categorias não corresponde ao total de pessoas afetadas. Tente novamente.\n")

print("\n Dados registrados com sucesso!")

total_desastres = len(tipos_desastres)

total_geral_afetados = sum(total_afetados)

total_criancas = sum(criancas)
total_adultos = sum(adultos)
total_idosos = sum(idosos)
total_mobilidade = sum(mobilidade_reduzida)
total_feridos = sum(feridos)


categorias = ["Crianças", "Adultos", "Idosos", "Mobilidade reduzida", "Feridos"]
valores_categorias = [total_criancas, total_adultos, total_idosos, total_mobilidade, total_feridos]

indice_mais_afetada = valores_categorias.index(max(valores_categorias))
categoria_mais_afetada = categorias[indice_mais_afetada]

indice_maior_desastre = total_afetados.index(max(total_afetados))

rua_mais_grave = ruas[indice_maior_desastre]
bairro_mais_grave = bairros[indice_maior_desastre]
cidade_mais_grave = cidades[indice_maior_desastre]
pais_mais_grave = paises[indice_maior_desastre]
evento_mais_grave = tipos_desastres[indice_maior_desastre]

print("----------------- RELATÓRIO FINAL -----------------")
print(f"Total de desastres registrados: {total_desastres}")
print(f"Total geral de pessoas afetadas: {total_geral_afetados}")

print("\nTotal de pessoas em cada categoria:")
print(f"Crianças: {total_criancas} | Adultos: {total_adultos} | Idosos: {total_idosos} | Mobilidade reduzida: {total_mobilidade} | Feridos: {total_feridos}")

print(f"\nCategoria mais afetada no geral: {categoria_mais_afetada}")

print(f"\nDesastre com maior número de afetados ocorreu no evento:")
print(f"Tipo: {evento_mais_grave}")
print(f"Rua: {rua_mais_grave}, Bairro: {bairro_mais_grave}, Cidade: {cidade_mais_grave}, País: {pais_mais_grave}")
print("-"*50)