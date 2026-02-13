# Jornada em IA Generativa

Repositório de estudos sobre IA Generativa, LLMs e arquiteturas modernas. Este é um projeto de aprendizado contínuo onde documento conceitos fundamentais, faço experimentos práticos e construo projetos para consolidar o conhecimento adquirido.

## Objetivo

Compreender profundamente os conceitos, arquiteturas e trade-offs reais de sistemas de IA Generativa através de:

- **Pesquisa guiada** sobre tópicos fundamentais
- **Anotações estruturadas** em Markdown
- **Projetos práticos** que aplicam os conceitos estudados
- **Reflexões críticas** sobre aplicações e limitações

O foco não é apenas código, mas **entendimento conceitual, arquitetural e de decisões reais de mercado**.

---

## Estrutura do Repositório

```
jornada-genai/
├── 01-fundamentos/
│   └── readme.md              # Conceitos básicos de IA Generativa
├── 02-tokens-e-contexto/
│   └── readme.md              # Tokenização e janelas de contexto
├── 03-embeddings/
│   └── readme.md              # Representações vetoriais e similaridade
├── 04-RAG/
│   └── readme.md              # Retrieval-Augmented Generation
├── 05-projeto-rag/
│   ├── data/                  # Base de conhecimento (anotações .md)
│   ├── src/
│   │   ├── ingest.py         # Processamento de documentos
│   │   └── rag.py            # Sistema de perguntas e respostas
│   └── README.md             # Documentação do projeto
└── README.md                 # Este arquivo
```

---

## Tópicos Estudados

### 01 - Fundamentos de IA Generativa
Introdução aos conceitos básicos de modelos generativos, diferenças entre IA tradicional e generativa.

### 02 - Tokens e Contexto
Como modelos de linguagem processam texto através de tokenização, limites de janela de contexto, e impacto nos custos computacionais.

### 03 - Embeddings
Representações vetoriais de texto, busca semântica, e como embeddings permitem que sistemas compreendam similaridade de significado.

### 04 - RAG (Retrieval-Augmented Generation)
Arquitetura que combina recuperação de informação com geração de texto, resolvendo limitações de janela de contexto e conhecimento desatualizado.

### 05 - Projeto RAG
**Aplicação prática:** Sistema de perguntas e respostas baseado em RAG que permite consultar minhas anotações de estudo usando busca semântica e LLM local.

**Tecnologias:** Python, LangChain, Ollama (Llama 3), ChromaDB, HuggingFace Embeddings

[Ver documentação completa do projeto](./05-projeto-rag/README.md)

---

## Como Funciona

### Metodologia de Estudo

**1. Pesquisa Semanal (Sextas-feiras)**
- Seleção de um tópico fundamental
- Assistir vídeos, ler documentação e artigos
- Tomar notas sobre conceitos-chave

**2. Documentação Estruturada**
- Criar arquivo `readme.md` no formato padrão
- Incluir: objetivo, fontes, o que aprendi, e reflexões
- Foco em explicar com minhas próprias palavras

**3. Projetos Práticos**
- Construir aplicações que consolidam os conceitos
- Documentar processo, desafios e aprendizados
- Compartilhar no repositório para referência futura

## Projetos Práticos

### Sistema RAG de Perguntas e Respostas

Um assistente de IA que responde perguntas sobre meus estudos em GenAI. O sistema foi construído do zero usando:

**Arquitetura:**
- Processamento de documentos Markdown
- Geração de embeddings locais
- Armazenamento em banco vetorial (ChromaDB)
- Busca semântica por similaridade
- Geração de respostas com Llama 3

[Documentação completa](./05-projeto-rag/README.md)

---

## Aprendizados Consolidados

### Conceitos-Chave Conectados

**Tokens → Embeddings → RAG**

1. **Tokens** são as unidades básicas de processamento. Texto é dividido em pedaços que o modelo consegue processar.

2. **Embeddings** transformam tokens em vetores numéricos que capturam significado semântico, permitindo comparações matemáticas.

3. **RAG** usa embeddings para recuperar informação relevante de uma base de conhecimento antes de gerar respostas, superando limitações de contexto.

### Trade-offs Arquiteturais

**Janela de Contexto vs. RAG:**
- Contexto grande = caro, mas simples
- RAG = mais complexo, mas escalável e econômico

**Embeddings Locais vs. API:**
- Local = privacidade, custo fixo, controle
- API = mais fácil, mas dependência externa

---

## Tecnologias e Ferramentas

**Linguagens:**
- Python 3.8+

**Frameworks e Bibliotecas:**
- LangChain - Orquestração de componentes RAG
- ChromaDB - Banco de dados vetorial
- HuggingFace - Modelos de embeddings
- Ollama - Execução de LLMs localmente

---

## Sobre

Este repositório documenta minha jornada de aprendizado em IA Generativa. O objetivo é construir compreensão sólida dos fundamentos antes de avançar para aplicações mais complexas.
