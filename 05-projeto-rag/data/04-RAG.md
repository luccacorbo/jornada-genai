# Sexta 04 — RAG (RETRIEVAL-AUGMENTED GENERATION)

## Objetivo
Entender RAG e como ele utiliza embeddings para superar limitações dos LLMs.

## Vídeos Assistidos

- [O que é RAG (Retrieval-Augmented Generation)? O cérebro por trás da personalização](https://www.youtube.com/watch?v=D2qGKX-bIL8)
- [RAG: Tudo que você PRECISA SABER para criar IAs especializadas](https://www.youtube.com/watch?v=s5gv0bdALFA)
- [RAG (Retrieval-Augmented Generation) // Dicionário do Programador](https://www.youtube.com/watch?v=CuPKOGdA46Q)

# O que aprendi

## O que é RAG?

O RAG (Retrieval-Augmented Generation) é uma arquitetura de IA que melhora a precisão de modelos generativos ao buscar informações em fontes externas antes de gerar uma resposta, ele combina um sistema de recuperação de informações com um modelo gerativo de linguagem, permitindo que o modelo acesse fontes de conhecimento externas antes de gerar uma resposta.

Seguindo com a explicação de [**o que são embeddings?**](../03-embeddings/readme.md), o RAG se encaixa como a aplicação prática dos conceitos de embeddings e similaridade semântica em sistemas de IA generativa.


## Por que RAG é necessário?

Modelos de linguagem como GPT, Llama e Claude têm conhecimento limitado ao que foi aprendido durante seu treinamento. Eles sofrem com:

- Data de corte: Não sabem eventos recentes
- Conhecimento estático: Não acessam documentos específicos
- Alucinações: Podem inventar informações quando não sabem

O RAG resolve esses problemas permitindo que o modelo "consulte" uma base de conhecimento atualizada antes de responder, funcionando como um estudante que pode abrir livros durante uma prova.

## Como o RAG funciona na prática

1. **Indexação** (preparação da base de conhecimento):
   - Documentos são divididos em chunks (pedaços menores)
   - Cada chunk é convertido em embeddings
   - Os embeddings são armazenados em um banco vetorial

2. **Recuperação** (quando o usuário pergunta):
   - A pergunta é convertida em embedding
   - Busca no banco vetorial pelos chunks mais similares
   - Retorna os documentos mais relevantes

3. **Geração aumentada**:
   - Os documentos recuperados são inseridos no contexto do prompt
   - O LLM gera uma resposta baseada nesse contexto aumentado
   - A resposta pode incluir citações das fontes



## Conexão com Embeddings

Quando um usuário faz uma pergunta em um sistema RAG o sistema busca informações relevantes usando embeddings, e só então gera uma resposta contextualizada.

O fluxo completo conectando todos os conceitos ate agora:

Texto da pergunta - Tokenização - Tokens IDs - Embeddings da pergunta -
Busca por similaridade - Recuperação de documentos - Contexto aumentado -
Geração da resposta

## Similaridade semântica em ação

No RAG, a [**similaridade semântica**](../03-embeddings/readme.md) é o mecanismo central de recuperação. Quando um usuário pergunta "Como cuidar de uma horta?", o sistema não busca por correspondência exata de palavras, mas sim por conteúdos que tenham significado similar:

"cuidados com hortas" - embedding - busca por vetores próximos -
encontra "manual de cultivo"

## Minha conclusão

Ao longo das semanas anteriores, foi possível entender como textos são transformados em tokens, processados dentro de janelas de contexto e representados como embeddings que capturam significado semântico. O RAG surge como a síntese prática desses conceitos, criando sistemas mais inteligentes e úteis.

Essa abordagem resolve problemas fundamentais: o custo de processar grandes documentos é reduzido (apenas os chunks relevantes são inseridos no contexto), a atualização de conhecimento é simples (basta atualizar a base vetorial), e a precisão aumenta (as respostas são ancoradas em fontes confiáveis) 