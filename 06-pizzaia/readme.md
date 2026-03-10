# PizzAI - Atendente Virtual de Pizzaria

Chatbot com LLM que simula um atendente de pizzaria, conduzindo a conversa do pedido até a entrega.

## Objetivo

* Praticar **LLMs** (Google Gemini)
* Criar **prompt de sistema** para definir a persona do atendente
* **Gerenciar contexto** da conversa usando histórico
* Integrar com **LangChain**

O foco é entender como o contexto é mantido e como o prompt guia o comportamento do modelo.

## Estrutura do Projeto

```
06-pizzaia/
├── main.py       # Lógica do chatbot
├── config.py     # Configuração da API (Pydantic Settings)
└── README.md     # Este arquivo
```

## Como Funciona

1. **System Message**: Define o comportamento do PizzAI (cumprimento, coleta de pedido, pagamento e entrega).
2. **Histórico de Mensagens**: Mantém o contexto de toda a conversa.
3. **Loop Conversacional**: A conversa continua até o usuário digitar `sair`, `satisfeito` ou `so isso`.

## Tecnologias

* **Python 3.8+**
* **LangChain** — integração com o modelo
* **Google Gemini 2.5 Flash** — LLM via API
* **Pydantic** — para gerenciar settings via `.env`

## Como Rodar

1. no seu terminal:

```bash
cd 06-pizzaia
```

2. Instale as dependências:

```bash
pip install langchain langchain-google-genai pydantic python-dotenv
```

3. Crie um arquivo `.env` na raiz com sua chave:

```
GOOGLE_API_KEY=sua_chave_aqui
```

4. Execute o chatbot:

```bash
python ia.py
```

## Aprendizados

* **Prompt bem estruturado** garante comportamento consistente
* **Histórico completo** mantém contexto, mas aumenta custo
* **Janela deslizante** controla custo, mas pode perder informações
* **API vs. modelo local**: API é prática, mas tem custo; modelo local é gratuito, mas exige hardware
