# Imersão IA - 2 edição

## Modulo 1: Mergulhando no Gemini, a IA do Google

O ecossistema Gemini é seja um switch de desenvolvimento ou conjunto de opções de ferramentas para desenvolvimento para diferentes cenários.

Na plataforma podemos encontrar duas opções:
#### Gemini
    - Gemini é uma versão (modelo Gemini 1.0 Pro) que tem toda a capacidade de reasoning, ou de raciocínio do Gemini, como interpretação de imagem, vídeo e tudo mais.
#### Gemini Advanced
    - Gemini Advanced é para cenários que precisa de um grande volume de informação de entrada, basicamente são enviados grande volumes de texto ou vídeo, na qual o Advanced suporta esses cenários.

Um modelo de linguagem como o Gemini, conceitualmente, dentro do mundo de IA, temos dois grandes grupos ou duas grandes formas de desenvolver um modelo.
#### AI preditiva
    - AI preditiva é quando treinamos um modelo de uma forma que aprende uma lógica, uma fórmula matemática para dado uma entrada, gere um resultado.
#### AI generativa
    - AI generativa é abordado a criação do modelo de forma diferente, é apresentado um conteúdo vasto de informação e o modelo aprende a modelar a informação, como uma análise linguística daquele texto.




## Modulo 2: Melhores Técnicas em Engenharia de Prompt

### Dicas:
#### 1. Detalhar bem o que você está buscando dentro do Gemini
    Modelo não recomendado: "Crie uma campanha de viagem para o Japão.
    Modelo recomendado: "Aja como um agente de marketing. Crie uma campanha de viagem para o Japão focada em brasileiros que se interessam pela cultura de artes marciais e samurais. Liste os principais pontos turisticos que os viajantes irão visitar no Japão que tenham relação com esses temas.
    
    * No modelo recomendado, podemos ser ainda mais especificos, solicitando uma cidade especifica (Tokio), hotéis, restaurantes e outros pontos relevantes para busca.
    
#### 2. Dividir tarefa muito complexa em tarefas menores
    1: análise todos os pontos turísticos que estão relacionados aos samurais e artes marciais em uma viagem ao Japão
    2: liste quais são os mais relevante e próximo da cidade de Tokio
    3: encontre hoteis próximos a esses pontos turisticos
    
    * Essa dica pode ser feito em um unico comando de prompt ou vários comandos de prompt, cada escolha feita pode gerar resultados finais diferentes, na escolha da segunda opção seu próximo passo pode ser influenciado de acordo com a resposta do comando anterior 
    
#### 3. Solicitar uma justificativa do resultado gerado
    Seguindo a mesma dica anterior, após o Gemini responder a primeira etapa, podemos solicitar uma justificativa porque daquela resposta
        
#### 4. Refinar muito bem o que está buscando com um alto grau de acuracia, grau de certeza e o grau de realidade
    Modelo tem muito conhecimento para gerar muitos coisa e com a falta de precisão na busca, pode gerar o conceito "ALUCINA"



### As quatro camadas (perspectivas) do Gemini:
#### 1. Engenharia de Prompt
#### 2. Parâmetros de execução
    são os parâmetros que podem ser definidos que o modelo pode considerar quando ele está compondo a resposta
#### 3. Configurações de segurança
    filtragem de qualidade de resultado, sobre discurso de ódio, preconceitoe relacionados, já está embutido no Gemini
#### 4. Informações inventadas ou alucinadas
    Redução intrínseca do modelo para informações inventadas ou alucinadas



### Estratégias para melhores resultados para usar o Prompt Gemini (AI Studio)
#### 1. Zero-shot Prompting
    Sem usar exemplos quando executa um comando no prompt

    Exemplo:
        Usuário {
            análise todos os pontos turísticos que estão relacionados aos samurais e artes marciais em uma viagem ao Japão
        }
        
        Modelo {
            Explorando o Japão Samurai e das Artes Marciais: Guia Completo de Pontos Turísticos
            Sua viagem ao Japão será ainda mais enriquecedora se você mergulhar na rica história samurai e nas artes marciais do país. Para te ajudar a planejar sua jornada, preparei um guia completo com os principais pontos turísticos relacionados a esse tema:
            Tóquio:
            Museu do Samurai: Uma viagem no tempo para o mundo dos samurais, com exposições de armaduras, espadas, documentos históricos e artefatos da época feudal.
            Museu Nacional de Tóquio: Possui uma seção dedicada à história e cultura japonesa, incluindo peças sobre os samurais e suas armas.
            Templo Sensō-ji: Um dos templos mais antigos de Tóquio, com forte ligação com a história samurai e a arte da caligrafia.
            Mercado de Peixes de Tsukiji: O local mais movimentado da capital, com a energia dos guerreiros em cada canto.
            Akihabara: O paraíso da cultura pop japonesa, onde você encontrará lojas de artigos de samurais, mangás e animes que exploram a temática das artes marciais...
        }

#### 2. Few-shot prompting
    Alguns exemplos para o modelo saber a área de atualção

    Exemplo:
        Usuário {
            Pergunta: O Pedro tem 2 bolas vermelhas e 5 boalas azuis. Quantas bolas ele tem no total?

            Resposta: O Pedro tem 7 bolas no total.

            Pergunta: Um diretor de cinema já dirigiu 16 filmes. Metade dos filmes que ele dirigiu são de ação. e ,etade dos filmes de ação tem a participação de Nicolas Cage, e na metade deles o Nikolas Cage tem bigode. Quantos filmes de ação com a participação de Nicolas Cage com bigode ele dirigiu?

            Resposta:
        }

        Modelo {
            Resposta: O diretor dirigiu 2 filmes de ação com a participação de Nicolas Cage com bigode.
        }

#### 3. Chain-of-thought
    Cadeia de pensamentos, é fazer o modelo replicar a maneira que raciocinamos sobre um problema. Então, se existe uma tarefa complexa pode resolver dividindo em subtarefas e a partir das sub-tarefas, consegue ter evoluções passo a passo até que no final temos a conclusão do que precisa.
    O que é feito matematicamente com modelo, é refinar uma pergunta maior e mais complexa nas etapas das informações intermediárias que precisa ter para que no final tenha a resposta que precisa.

#### 4. least-to-most prompting
    Do minimo ao máximo, envia um prompt grande e solicita para o modelo dividir em problemas menores antes de responder

#### 5. self-consistency
    auto consistencia é usado para dados mais precisas, pode ser usado na frequência dos dados

### Links
1. [Prompt-design-strategies](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompt-design-strategies?hl=pt-br)




## Modulo 3: Explorando os parâmetros do Google AI Studio
