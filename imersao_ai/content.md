# Imersão IA - 2 edição

    Gemini é um modelo LLM (Large Language Model – modelo de linguagem grande) desenvolvido pela Google DeepMind.

    Trabalha com linguagem de modelo, é trabalhar com uma área da inteligência artificial chamada de NLP (Natural Language Processing - Processamento de Lunguagem Natural).


## Tecnologias

    Gemini
    AI Studio
    Google Colab


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





## Modulo 3: Explorando os parâmetros do Google AI Studio

No ambiente do AI Studio, temos 3 opções na criação de um novo prompt [Create_new]()


##### Chat prompt
   
    É semelhante ao prompt usado no Gemini, o IA Studio guardando o histórico e contexto das conversas como os exemplos usados anteriormente.


##### Freeform prompt

    Uma maneira de embutir um prompt maior dentro de uma aplicação/solução (tem algo mais elaborado) e não tem necessidade de ter uma interação de chat, com Freeform agrega as perguntas em requisição única.


##### Structured prompt

    É a habilidade que tem na interface do AI Studio de montar uma estrutura tabular para usar a estratégia de few-shot prompting.


#### Visão computacional

    Dentro de machine learning tem uma área chamada de "Visão computacional", são as soluções que lindam com imagem, vídeos e identificação de objetos fornecidos por imagens.


#### Detecção de objeto
    
    AI generativa tem um tratamento muito mais rápido em questões de segundos.


#### System instructions
    
    Localizado acima do chat da interface do Google IA Studio, é um diretriz ou regra de como o modelo tem que se comportar/agir, independente de qual comando prompt é inserido.

    Exemplo:
        Você é um assistente muito sarcástico e que usa muitas gírias


#### Model
    
    Está localizado do lado direito da tela do AI Studio.

    Gemini 1.0 Pro - pode usar as diferentes modalidades, assim como 1.5, porém tem algumas opções adicionais de customização dessa geração de prompt.
    Gemini 1.5 Flash
    Gemini 1.5 Pro - mais robusto, mais capacidade de contexto, ingestão de informação, mas no momento que está dentro do AI Studio, não é possível fazer uma customização de parâmetros.
    Gemini 1.0 Pro 001 (Tuning)


#### Temperature
    
    Está localizado do lado direito da tela do AI Studio.
    
    Quando usar o valor igual a 0 ou próximo a 0, é para indicar que p contexto mais conservador ou mais especifica em relação ao controle, é para o modelo não usar outra característica que não seja a maior probabilidade.
    No caso de colocar no 1 ou próximo de 1, são usados para contextos mais criativos, o modelo usará textos diferentes para o mesmo texto inserido no prompt.


#### Add stop sequence
    
    Está localizado do lado direito da tela do AI Studio.

    Em um contexto controlado de geração de conteúdo, pode ser definido que caracteres ou sequencia a ser usada para o modelo marcar como final da criação, podendo ser útil para reprocessar o resultado para embutir em uma página ou artigo, por exemplo, deixando mais claro de onde está finalizando.


#### Safety settings
    
    Está localizado do lado direito da tela do AI Studio.

    É para ajustar o nível de segurança Harassment (Assédio), Hate (Ódio), Sexually Explicit (Sexualmente Explicito) e Dagerous Content (Conteúdo Perigoso).


#### Advanced settings
    
    Está localizado do lado direito da tela do AI Studio.

    Top K - diminuição do glossário de palavras com o mesmo significa, sem escolher as palavras especifica, como um controle do uso de determinadas palavras, por exemplo, "mas", "porém", "entretanto", pode limitar quantas palavras dessa mesma categoria vai ser usada.
    
    Top P - também é uma seleção de palavras, porém ao invés de ser numérica como o top K, é usada probabilidade. Define a probabilidade agregada definida para trabalhar, isto é a soma das probabilidades de cada palavra e qual é a soma máxima toleravel.

    Temperature - segue a mesma ideia da Temperature anterior, quanto igual a 0 ou mais próxima de 0, é usada a probabilidade da palavra que vai se mais usada e quando for igual a 1 ou próximo de 1, é uma escolha aleatória, podendo ser qualquer uma das palavras disponíveis.

#### API Key

    É uma forma de identificar, por exemplo, um computador se identificar com outro (uma chave não compartilhada).


## Links

1. [Prompt-design-strategies](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompt-design-strategies?hl=pt-br)
2. [Google-gallery](https://ai.google.dev/examples?hl=pt-br)
3. [Entendendo a Tokenização nos Modelos de Inteligência Artificial](https://www.dio.me/articles/entendendo-a-tokenizacao-nos-modelos-de-inteligencia-artificial)
4. [Google-AI-Studio](https://aistudio.google.com/)
5. [Google-Gemini](https://gemini.google.com/)