 # Sexta 02 — FUNDAMENTOS

## Objetivo
Entender Tokens, janela de contexto e custo.

## Vídeos Assistidos

- [O Que São Tokens? O Que É Janela De Contexto? Entenda Mais Sobre ChatGPT, Claude, Gemini e Llama](https://www.youtube.com/watch?v=HuO2KeW2es4)  
- [Tokens: A Base da Linguagem para a IA - @CursoemVideo Inteligência Artificial](https://www.youtube.com/watch?v=JfJJIrOhWwQ&t=153s)  
- [Entenda o que é token e como ele afeta o preço dos modelos de IA](https://www.youtube.com/watch?v=euR1NRbxycc) 


# O que aprendi

## O que são tokens?

Tokens são as unidades mínimas de texto que um LLM consegue processar. Eles não representam necessariamente palavras completas, mas partes de palavras, símbolos ou padrões frequentes de linguagem. Antes de gerar uma resposta, todo texto enviado ao modelo é convertido em tokens, que são processados como números.

Ex: o modelo recebe - "o que é um token?" - o modelo converte em tokens - "o" "que" "é" "um" "token" "?" = [46, 661, 1212, 1713, 6602, 1423] e então com base no contexto, gera respostas prevendo o token mais proveavel (exemplo testado no tokenizer da openai).

Tokens são fundamentais não apenas para o funcionamento do modelo, mas também para decisões de arquitetura, custo e experiência do usuário, já que chamadas de API são cobradas com base na quantidade de tokens processados.

## Janela de Contexto


A janela de contexto representa o limite de tokens que um modelo de linguagem consegue considerar simultaneamente para gerar uma resposta. Ela funciona como a memória ativa do modelo: tudo o que influencia a resposta precisa estar presente dentro desse espaço.

Esse limite existe por razões arquiteturais e computacionais. À medida que o número de tokens cresce, o custo de processamento, a latência e o consumo de memória aumentam significativamente.

Por isso, decisões sobre o que incluir ou excluir do contexto impactam diretamente a arquitetura do sistema, a experiência do usuário e o custo operacional de soluções baseadas em IA generativa.

## Custo em Sistemas de IA Generativa

Toda vez que um LLM responde a uma solicitação, ocorre um processo bem definido. Primeiro, o texto enviado pelo usuário é convertido em tokens. Em seguida, esses tokens são inseridos dentro de uma janela de contexto, que representa o limite de informação que o modelo consegue processar simultaneamente.

O modelo então processa todos esses tokens em conjunto e passa a gerar novos tokens como resposta. É exatamente nesse processamento que o custo está concentrado. Tanto os tokens de entrada — como prompts, histórico de conversa, instruções do sistema e dados adicionais — quanto os tokens de saída — o texto gerado pelo modelo — contribuem diretamente para o custo da operação.

Quanto maior a quantidade de tokens envolvidos em uma interação, maior será o consumo de recursos computacionais, impactando custo financeiro, tempo de resposta e escalabilidade do sistema.

## Trade-offs relacionados ao uso de contexto

As decisões sobre quanto contexto fornecer ao modelo envolvem compromissos claros entre qualidade, custo e desempenho. Esses trade-offs podem ser resumidos da seguinte forma:

| Escolha           | Ganho            | Perda             |
| ----------------- | ---------------- | ----------------- |
| Contexto grande   | Maior coerência  | Custo elevado     |
| Contexto pequeno  | Menor custo      | Esquecimento      |
| Histórico longo   | Conversa natural | Maior latência    |
| Contexto resumido | Eficiência       | Perda de nuances  |

Essas escolhas não possuem uma resposta única correta. Elas dependem do tipo de aplicação, do volume de usuários, das restrições de custo e da experiência desejada para o usuário final.

## Minha conclusão

Em sistemas de IA generativa, o custo está diretamente ligado à quantidade de tokens processados em cada interação. Por esse motivo, decisões relacionadas ao gerenciamento de contexto, histórico e estrutura do prompt são tão importantes quanto a qualidade das respostas geradas pelo modelo.

Projetar soluções eficientes em IA generativa exige equilibrar coerência, custo e desempenho, tratando o uso de tokens como uma decisão arquitetural e também como uma decisão de negócio.
