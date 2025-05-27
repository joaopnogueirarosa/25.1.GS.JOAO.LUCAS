## 🗂️ Descrição
 
O sistema permite que o usuário cadastre múltiplos desastres, informando:
 
- Tipo do desastre (ex.: incêndio, enchente, deslizamento, etc.)
- Localização completa (país, cidade, bairro, rua)
- Quantidade total de pessoas afetadas
- Detalhamento das pessoas afetadas por categoria:
  - Crianças
  - Adultos
  - Idosos
  - Pessoas com mobilidade reduzida
  - Feridos
 
O programa realiza validações para garantir que a soma das pessoas nas categorias corresponda ao total de afetados.
 
Após o cadastro, o sistema gera análises e um relatório com:
 
- Total de desastres registrados
- Total geral de pessoas afetadas
- Total de pessoas afetadas por categoria
- Qual categoria foi mais afetada no geral
- Local do desastre com maior número de afetados
 
## 🚀 Funcionalidades
 
- Cadastro de múltiplos desastres
- Validação dos dados inseridos
- Análise estatística simples
- Relatório final resumindo todos os dados coletados
 
## 📑 Estrutura do Código
 
O código está organizado em 3 blocos principais:
 
1. **Entrada de Dados e Armazenamento**
   - Solicita ao usuário informações dos desastres e das pessoas afetadas.
   - Armazena os dados em listas.
 
2. **Análise dos Dados**
   - Calcula totais, identifica a categoria mais afetada e o desastre mais grave.
 
3. **Saída dos Resultados**
   - Apresenta um resumo dos dados e das análises de forma estruturada no terminal.
