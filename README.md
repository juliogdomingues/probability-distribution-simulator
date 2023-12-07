# probability-distribution-simulator

Documentação do Projeto

Simulador de Distribuição de Probabilidade
Julio Guerra Domingues (2022431280)
Samuel Sales Nogueira Viana (2021078455)

Introdução

Foi proposta a implementação de um programa que simula as seguintes distribuições de probabilidade: normal, binomial, exponencial, uniforme, qui-quadrado, Poisson e t de Student. O programa retorna gráficos do tipo histograma para a visualização da simulação. Foi decidido que seria utilizado o Python como linguagem de programação desse projeto. 

A visualização do projeto é feita através do link a seguir: https://probability-distribution-simulator.streamlit.app/ 

Caso prefira, o código pode ser baixado na íntegra a partir do respositório do GitHub: https://github.com/juliogdomingues/probability-distribution-simulator

Para cada distribuição de probabilidade escolhida, é possível definir o(s) parâmetro(s) (como por exemplo a probabilidade no caso da Binomial), alterar o número de amostras e o tamanho de cada amostra. Foi utilizado a biblioteca Streamlit para a visualização dos gráficos de forma dinâmica. 
Métodos

Foi criada a função ‘gerar_amostras_e_medias’ que recebe como parâmetros: dist_func, n, m e *params. O parâmetro ‘dist_func’ define o nome da função da probabilidade da qual utiliza a biblioteca numpy (biblioteca para manipulação numérica no python), ‘n’ é o tamanho de cada amostra, ‘m’ é o número de amostras e ‘*params’ são os parâmetros que devem estar contidos dentro da função de probabilidade. A função ‘gerar_amostras_e_medias’ retorna um array (lista de listas) contendo as m amostras de tamanho n e, é retornada também uma lista com as médias amostrais.

A função ‘padronizar_media’ realiza a padronização das médias amostrais através da média real com a seguinte função: (médias-médiareal )(real/ n) , os parâmetros são: medias, media_verdadeira, desvio_padrao_verdadeiro e tamanho_amostra. 

A função ‘plot_histograms_lado_a_lado’ foi criada para gerar os gráficos propostos, ela recebe como parâmetros: amostras, medias_padronizadas e title, onde ‘title’ define o nome da distribuição. Essa função realiza o tratamento dos dados e a normalização para plotar o histograma das amostras e o histograma das médias amostrais.

Resultados

Para distribuições com variância finita, como esperado pelo Teorema Central do Limite (TCL), os resultados mostram que, conforme o tamanho da amostra aumenta, a distribuição das médias amostrais tende a se aproximar de uma distribuição normal, independentemente da forma da distribuição original.
Isso é claramente observado nos histogramas gerados, em que as médias amostrais de distribuições não normais (como exponencial, binomial, etc.) começam a assumir forma característica da distribuição normal.

Influência do Tamanho da Amostra (n): Conforme o tamanho da amostra aumenta, a aproximação para a distribuição normal torna-se mais evidente, confirmando a previsão do TCL. Em tamanhos de amostra pequenos, a distribuição das médias amostrais pode não parecer normal, especialmente para distribuições altamente assimétricas ou discretas.

Influência do Número de Amostras (m): Aumentar o número de amostras (m) melhora a estimativa da distribuição das médias amostrais. Com um número maior de amostras, o histograma torna-se mais suave e a convergência para a normalidade é mais facilmente observável.

Variabilidade e Dispersão: Os resultados também demonstram a redução na variabilidade das médias amostrais em comparação com a distribuição original. Isso é uma consequência direta do TCL, que afirma que a variância da distribuição das médias amostrais é igual à variância da população dividida pelo tamanho da amostra.

Discussão

Os resultados gerados pelo programa são consistentes com as previsões teóricas do TCL. Eles oferecem uma visualização prática de como, independentemente da forma da distribuição original, as médias amostrais tendem a uma distribuição normal à medida que o tamanho da amostra aumenta.

Tal comportamento tem implicações significativas na prática estatística, especialmente em inferência estatística, onde frequentemente assumimos normalidade para grandes amostras. Os resultados gerados pelo programa podem ajudar os alunos a compreender a justificativa por trás de várias técnicas estatísticas, como intervalos de confiança e testes de hipóteses.


Conclusão

Os resultados gerados pelo programa fornecem uma confirmação visual e interativa dos conceitos fundamentais do TCL, tornando-o uma ferramenta valiosa para fins educacionais. Eles permitem aos usuários observar diretamente o efeito do tamanho da amostra e do número de amostras na distribuição das médias amostrais, ajudando a solidificar o entendimento teórico com evidências práticas.


Bibliografia
Ross, S. (2010). Probabilidade: Um Curso Moderno com Aplicações (8ª ed.). LTC Editora.
Alura. (2021, 9 de novembro). Streamlit: compartilhando sua aplicação de dados sem dor de cabeça. Alura. https://www.alura.com.br/artigos/streamlit-compartilhando-sua-aplicacao-de-dados-sem-dor-de-cabeca 
Kanaries. (n.d.). Dataframe Histogram. Kanaries. https://docs.kanaries.net/pt/topics/Pandas/dataframe-histogram 
Educação LAT. (n.d.). Distribuição Normal em Python. Tutoriais Educação LAT. https://tutoriais.edu.lat/pub/python-data-science/python-normal-distribution/python-distribuicao-normal 
Data Hackers. (2018, 28 de março). Normalizar ou padronizar as variáveis? Data Hackers. https://medium.com/data-hackers/normalizar-ou-padronizar-as-vari%C3%A1veis-3b619876ccc9 
