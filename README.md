# Sistema de Controle de Créditos Pré-Pagos para Impressão

Este projeto é um sistema desenvolvido em Python para gerenciar usuários e seus créditos pré-pagos para serviços de impressão. Ele permite cadastrar usuários, adicionar e debitar créditos, listar usuários cadastrados e excluir registros. As informações são armazenadas em um arquivo CSV.

## Funcionalidades

1. **Cadastrar Usuários:**
   - Cadastro de usuários com número de telefone (formato: `(ddd)xxxxx-xxxx`), nome e saldo inicial em reais.

2. **Adicionar Créditos:**
   - Adiciona créditos pré-pagos com base em uma taxa de conversão (R$30,00 = 100 impressões).

3. **Debitar Créditos:**
   - Debita impressões do saldo do usuário cadastrado.

4. **Listar Usuários:**
   - Lista todos os usuários cadastrados com seus respectivos saldos de impressões.

5. **Exibir Saldo:**
   - Mostra o saldo de um usuário específico.

6. **Excluir Usuários:**
   - Remove um usuário cadastrado do sistema.

7. **Persistência de Dados:**
   - Os dados dos usuários são armazenados em um arquivo CSV chamado `usuarios.csv` para garantir a persistência entre execuções.

## Como Usar

### Pré-requisitos
- Python 3.x
- Biblioteca `csv` (inclusa na biblioteca padrão do Python)
- Biblioteca `re` (inclusa na biblioteca padrão do Python)

### Instruções

1. **Clone ou Baixe o Repositório**
   ```bash
   git clone <url-do-repositorio>
   cd <nome-do-diretorio>
   ```

2. **Execute o Script**
   ```bash
   python nome_do_arquivo.py
   ```

3. **Siga o Menu Interativo**
   - O menu apresenta opções para gerenciar usuários e seus créditos.

### Exemplo de Uso

#### Cadastro de Usuário
- Telefone: `(011)98765-4321`
- Nome: `Usuário Genérico`
- Saldo inicial: `R$30,00`

#### Conversão de Créditos
- Para cada R$30,00 adicionados, o usuário recebe 100 impressões.
- Se o saldo inicial for R$60,00, o usuário terá 200 impressões.

#### Exemplo de Execução
```text
--- Menu ---
1. Cadastrar usuário
2. Exibir saldo
3. Adicionar créditos
4. Debitar créditos
5. Listar usuários
6. Excluir usuário
7. Sair
Escolha uma opção: 1
Digite o telefone do usuário (formato: (ddd)xxxxx-xxxx): (011)98765-4321
Digite o nome do usuário: Usuário Genérico
Digite o saldo inicial em reais: 30
Usuário Usuário Genérico cadastrado com sucesso com saldo equivalente a 30 reais.
```

## Estrutura do Código

- **Classe `Usuario`:**
  Representa um usuário com atributos de telefone, nome e saldo.

- **Classe `SistemaDeImpressao`:**
  Gerencia o sistema, incluindo validações, persistência de dados e operações de crédito.

- **Arquivo `usuarios.csv`:**
  Armazena os dados dos usuários no formato:
  ```csv
  Telefone,Nome,Saldo
  (011)98765-4321,Usuário Genérico,100.0
  ```

## Contribuições

Sinta-se à vontade para contribuir com melhorias. Faça um fork do projeto e envie um pull request.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

**Desenvolvido por Luiz Carlos França.**
