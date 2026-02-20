# Sistema RAG - Jornada GenAI

## Objetivo
Construir um sistema de perguntas e respostas baseado em RAG (Retrieval-Augmented Generation) que permite consultar minhas anotações de estudo sobre IA Generativa usando busca semântica e LLM local.

## O que é este projeto?

Este é um assistente de IA que responde perguntas sobre os temas que estou estudando em GenAI. O sistema foi treinado com minhas próprias anotações em Markdown sobre:

- **Fundamentos de IA Generativa**
- **Tokens e Contexto**
- **Embeddings**
- **RAG (Retrieval-Augmented Generation)**

**Você pode fazer perguntas simples como:**
- "O que são embeddings?"
- "Como funcionam os tokens?"
- "Explique o que é RAG"
- "O que é contexto em LLMs?"

O sistema busca nas anotações armazenadas e responde em português usando Llama 3 rodando localmente via Ollama.

---

# Como Funciona

O sistema segue este fluxo:

```
1. Você escreve anotações em .md (pasta data/)
2. Script ingest.py processa e armazena em banco vetorial
3. Script rag.py permite fazer perguntas sobre o conteúdo
4. IA busca trechos relevantes e responde baseado nas anotações
```

**Estrutura do projeto:**
```
jornada-genai/
├── data/                          # Anotações de estudo em .md
│   ├── 01-fundamentos.md
│   ├── 02-tokens-e-contexto.md
│   ├── 03-embeddings.md
│   └── 04-RAG.md
├── src/
│   ├── ingest.py                  # Processa documentos
│   └── rag.py                     # Interface de perguntas
├── chroma_db/                     # Banco vetorial (gerado automaticamente)
└── requirements.txt
```

---

# Requisitos de Sistema

Antes de começar, certifique-se de que seu computador atende aos requisitos mínimos:

**Hardware:**
- **RAM:** Mínimo 8GB (recomendado 16GB)
- **Armazenamento:** Pelo menos 10GB livres
  - Ollama + Llama 3: ~4GB
  - Dependências Python: ~2GB
  - Banco vetorial e cache: ~1-2GB
- **Processador:** CPU x64 (Intel/AMD)
- **GPU:** Opcional, mas acelera significativamente o processamento

**Software:**
- Python 3.8 ou superior
- Sistema operacional: Windows 10+, macOS 11+, ou Linux (Ubuntu 20.04+)
- Conexão com internet (para instalação inicial)

> ⚠️ **Nota:** O Llama 3 pode rodar lento em computadores com menos de 8GB de RAM. Se encontrar lentidão, considere usar modelos menores como `ollama pull llama3:8b` ou `ollama pull phi3`.

---

# Instalação Completa

## Passo 1: Instalar o Ollama

O Ollama é necessário para rodar o modelo de IA localmente.

**Windows/Mac/Linux:**
1. Acesse [ollama.ai](https://ollama.ai/)
2. Baixe o instalador para seu sistema operacional
3. Execute o instalador
4. Verifique a instalação:
```bash
ollama --version
```

**Baixar o modelo Llama 3:**
```bash
ollama pull llama3
```
> ⏱️ Download de ~4GB, pode levar alguns minutos

## Passo 2: Clonar o Repositório

```bash
git clone https://github.com/luccacorbo/jornada-genai.git
cd jornada-genai
```

## Passo 3: Criar Ambiente Virtual Python

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Você verá `(venv)` no início da linha do terminal.

## Passo 4: Instalar Dependências Python

```bash
pip install -r requirements.txt
```

**O que será instalado:**
- `langchain-community` - Framework para RAG
- `chromadb` - Banco de dados vetorial
- `sentence-transformers` - Para embeddings
- `ollama` - Integração com Ollama

> ⏱️ Instalação leva ~2-3 minutos

---

# Como Usar

## Passo 1: Processar suas Anotações

Certifique-se de que o Ollama está rodando (abra em outro terminal):
```bash
ollama serve
```

Agora processe os documentos da pasta `data/`:
```bash
python src/ingest.py
```

**Você verá:**
```
4 documentos carregados.
127 chunks criados.
Ingestão finalizada com sucesso!
```

> 💡 **Quando executar novamente?** Sempre que adicionar ou modificar arquivos .md na pasta `data/`

## Passo 2: Fazer Perguntas

```bash
python src/rag.py
```

**Exemplos de perguntas que você pode fazer:**

```
Pergunta: O que são embeddings?
Resposta: Embeddings são representações vetoriais que capturam o significado 
semântico do texto. Eles transformam palavras e frases em vetores numéricos...

Pergunta: Como funcionam os tokens?
Resposta: Tokens são as unidades básicas que os modelos de linguagem processam.
O texto é dividido em tokens que podem ser palavras, partes de palavras...

Pergunta: Explique o que é RAG
Resposta: RAG (Retrieval-Augmented Generation) é uma técnica que combina
recuperação de informação com geração de texto...
```

**Para sair:** Digite "sair" no terminal para encerrar

---

# Personalizações (Opcional)

## Adicionar Mais Anotações

1. Crie novos arquivos `.md` na pasta `data/`
2. Execute novamente: `python src/ingest.py`
3. Pronto! O sistema já conhece o novo conteúdo

## Ajustar Tamanho dos Pedaços de Texto

Em `src/ingest.py`, linha 15-18:
```python
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,      # Tamanho do pedaço (caracteres)
    chunk_overlap=50     # Sobreposição entre pedaços
)
```

**Quando modificar?**
- Textos muito técnicos: aumente para `800-1000`
- Respostas genéricas: diminua para `300-400`

---

## ⚠️ Sistema muito lento / Travando

**Causas possíveis:**
- RAM insuficiente (menos de 8GB)
- Modelo muito pesado para seu hardware

**Soluções:**

1. **Usar modelo menor:**
```bash
ollama pull llama3:8b     # Versão mais leve do Llama 3
# ou
ollama pull phi3          # Modelo ainda menor (~2GB)
```

Depois altere em `src/rag.py`:
```python
llm = Ollama(
    model="llama3:8b",  # ou "phi3"
    system="..."
)
```

2. **Reduzir chunk_size:**
Em `src/ingest.py`, diminua para processar menos texto por vez:
```python
chunk_size=300,  # Reduzido de 500
```

3. **Fechar outros programas** para liberar RAM durante o uso

---

# Tecnologias Utilizadas

- **Python 3.8+** - Linguagem base
- **LangChain** - Framework para RAG
- **Ollama + Llama 3** - Modelo de IA local
- **ChromaDB** - Banco de dados vetorial
- **HuggingFace Embeddings** - Geração de embeddings

---

# O que aprendi construindo este projeto

Ao desenvolver este sistema RAG, foi possível consolidar conceitos fundamentais de IA Generativa estudados ao longo da jornada:

## Arquitetura RAG na prática

RAG (Retrieval-Augmented Generation) combina busca semântica com geração de texto. Em vez de depender apenas do conhecimento interno do LLM, o sistema primeiro recupera informações relevantes de uma base de conhecimento e então gera respostas contextualizadas.

No meu caso, a base de conhecimento são minhas próprias anotações de estudo. Quando faço uma pergunta, o sistema:

1. Converte a pergunta em embedding
2. Busca os trechos mais similares semanticamente no banco vetorial
3. Envia esses trechos junto com a pergunta para o LLM
4. O LLM gera uma resposta baseada no contexto fornecido

## Processamento e chunking de documentos

Documentos longos não podem ser processados de uma só vez devido aos limites de contexto dos LLMs. Por isso, o sistema divide os arquivos `.md` em pedaços menores (chunks) de ~500 caracteres.

O `chunk_overlap` de 50 caracteres garante que informações importantes que aparecem entre chunks não sejam perdidas, mantendo continuidade semântica.

## Embeddings e busca semântica

Conforme estudado anteriormente, embeddings são representações vetoriais que capturam o significado do texto. Cada chunk é transformado em um vetor numérico usando o modelo `all-MiniLM-L6-v2`.

A busca não procura palavras exatas, mas sim **similaridade de significado**. Por exemplo:
- Pergunta: "Como funcionam os tokens?"
- Chunk relevante: "Tokenização é o processo de dividir texto..."

Mesmo sem palavras idênticas, os embeddings são matematicamente próximos.

## Integração de LLMs locais com LangChain

LangChain abstrai a complexidade de conectar diferentes componentes:
- Carregamento de documentos
- Divisão em chunks
- Geração de embeddings
- Armazenamento vetorial
- Recuperação semântica
- Integração com LLM

O Ollama permite rodar modelos como Llama 3 localmente, sem depender de APIs externas ou custos por token.

## Bancos vetoriais e recuperação de informação

ChromaDB armazena os embeddings e permite busca eficiente por similaridade. Quando uma pergunta é feita:

1. A pergunta é convertida em embedding
2. ChromaDB calcula a distância entre o embedding da pergunta e todos os chunks
3. Os chunks mais próximos (mais similares) são retornados
4. Esses chunks contextualizam a resposta do LLM

Isso resolve o problema de limite de contexto: não preciso enviar todo o conhecimento, apenas os trechos mais relevantes.

**Projeto desenvolvido como parte da jornada de estudos em IA Generativa** 
