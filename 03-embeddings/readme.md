# Sexta 03 — EMBEDDINGS

## Objetivo
Entender o que são embeddings e como eles permitem que sistemas de IA compreendam
similaridade e significado entre textos.

## Vídeos Assistidos

- [Embeddings](https://www.youtube.com/watch?v=B5uAdHP7K_I&t=105s)
- [Desvendando o Mundo dos Embeddings na Inteligência Artificial](https://www.youtube.com/watch?v=ihcZMEoXH7c) 
- [Embeddings e Vector Search para IA Generativa – O que são e como usar](https://www.youtube.com/watch?v=fvRyziDmvoA)  
  

# O que aprendi

## O que são embeddings?

Embeddings são representações numéricas de textos, frases ou documentos que capturam o significado semântico dessas informações. Em vez de trabalhar diretamente com palavras, a IA transforma o conteúdo em vetores (listas de números),permitindo que conceitos semelhantes sejam comparados matematicamente.

Ou seja, embeddings não representam texto de forma literal, mas sim o sentido do texto. Frases diferentes que falam da mesma coisa tendem a gerar vetores próximos, enquanto frases com significados distintos geram vetores distantes.

Exemplo conceitual:

"comprar celular"  
"adquirir smartphone"  

Mesmo com palavras diferentes, os embeddings dessas frases ficam próximos, pois o significado é semelhante.

## Conexão com Tokens e o Processo até Embeddings

Seguindo com a explicação de [**o que são tokens?**](../02-tokens-e-contexto/readme.md), os embeddings se encaixam como a **próxima etapa lógica** no processamento de texto por modelos de linguagem.

Quando um texto é enviado para um LLM, o primeiro passo é a tokenização. O modelo não trabalha diretamente com palavras, mas com unidades menores chamadas tokens, que são convertidas em identificadores numéricos (token IDs) e depois embeddings.

Exemplo:.

"o" "que" "é" "um" "token" "?" = [46, 661, 1212, 1713, 6602, 1423]

46   ("o")     = [ 0.01, -0.02,  0.03,  0.01, -0.01 ]

661  ("que")   = [ 0.10, -0.08,  0.05,  0.07, -0.02 ] 

1212 ("é")     = [ 0.09, -0.04,  0.02,  0.06, -0.01 ]

1713 ("um")    = [ 0.02, -0.01,  0.01,  0.02, -0.01 ] 

6602 ("token") = [ 0.80,  0.65, -0.10,  0.72,  0.40 ]

1423 ("?")     = [ 0.00,  0.00,  0.00,  0.01,  0.00 ]

**⚠️ Esses números são inventados, só pra ilustrar.**


Os tokens IDs são números que funcionam apenas como **índices técnicos**. Sozinhos, eles não carregam nenhum significado. O token ID `46`, por exemplo, não “sabe” que representa a palavra `"o"` — ele apenas aponta para uma posição interna no modelo.

O próximo passo é transformar esses token IDs em **vetores numéricos**, chamados de *embeddings*. Cada token ID é usado como referência para acessar um vetor previamente aprendido durante o treinamento do modelo.

De forma conceitual, o processo funciona assim:

Texto - Tokens - Tokens IDs - Embeddings


## Por que embeddings são necessários?

Modelos de linguagem não entendem texto como humanos. Internamente, eles operam apenas com números. Embeddings funcionam como uma ponte entre a linguagem humana e a matemática, permitindo que a IA:

- Compare textos
- Meça similaridade semântica
- Encontre informações relevantes
- Relacione perguntas com respostas possíveis

Sem embeddings, não seria possível realizar buscas inteligentes, recomendações ou recuperação de conhecimento baseada em significado.

## Similaridade semântica

A principal função dos embeddings é permitir a comparação de significado entre textos. Essa comparação não é feita verificando palavras iguais, mas sim medindo a distância entre vetores em um espaço matemático.

Quanto menor a distância entre dois embeddings, maior a similaridade semântica entre os textos que eles representam. Isso permite que sistemas encontrem conteúdos relacionados mesmo quando as palavras utilizadas são diferentes.

## Aplicações práticas de embeddings

Embeddings são amplamente utilizados em sistemas modernos de IA generativa, como:

- **Busca semântica:** encontrar documentos relevantes mesmo sem correspondência exata
  de palavras.
- **Sistemas de recomendação:** sugerir conteúdos com base na proximidade de interesses
  representados por vetores.
- **RAG (Retrieval-Augmented Generation):** recuperar trechos relevantes de uma base de
  conhecimento antes de gerar respostas com um LLM.


## Minha conclusão

Ao longo das semanas anteriores, foi possível entender como textos são processados por modelos de linguagem a partir de tokens, limites de contexto e custos computacionais. Embeddings surgem como uma continuação natural desses conceitos.

Inicialmente, todo texto é convertido em tokens, que são representações mínimas de linguagem. Esses tokens recebem identificadores numéricos (token IDs), que por si só não carregam significado semântico. A partir desses IDs, o modelo gera embeddings — vetores numéricos de alta dimensionalidade que capturam o significado dos tokens no contexto da linguagem.

Diferentemente dos tokens, que servem para processamento sequencial dentro da janela de contexto, embeddings permitem representar o significado do texto de forma matemática e comparável. A similaridade entre textos não é avaliada comparando palavras ou token IDs, mas sim calculando a distância ou proximidade entre seus vetores no espaço vetorial.

Essa abordagem permite resolver limitações da janela de contexto, pois informações podem ser recuperadas com base em similaridade semântica, sem que todo o conteúdo precise estar presente no prompt. Além disso, a comparação entre embeddings é computacionalmente mais barata do que reprocessar grandes volumes de texto em um modelo de linguagem, impactando diretamente o custo e a arquitetura de sistemas de IA generativa.

Dessa forma, embeddings funcionam como a ponte entre compreensão semântica, eficiência computacional e escalabilidade em aplicações modernas de IA.
