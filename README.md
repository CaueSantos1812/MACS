# MACS
Trabalho Semestral de Ciência de Dados
Grupo: Anna Karen, Cauê Santos, Matheus Zaia e Samira

RESUMO DO QUE FIZEMOS ATÉ AGORA

Nosso projeto semestral tinha como objetivo realizar a simulação de uma doença dentro de uma população, visualizando essa dinâmica através de gráficos. Até hoje, dia 30/05, encontramos um modelo matemático que modela a dinâmica de doenças, chamado SIR (Suscetíveis, Infectados, Removidos), entendendo seu funcionamento e construção, e adaptamos ele para um código em Python. Também utilizamos a biblioteca "random" para aumentar a aleatoriedade da doença, assim como a biblioteca "matplotlib" para plotarmos os gráficos e animações dos dados obtidos.  

MAIS DETALHES DO QUE FIZEMOS

Inicialmente, tínhamos a ideia de criar um código que mostrasse de forma visual, a partir de uma animação, a evolução de uma epidemia em um dado período de tempo. O modelo utilizado foi uma variação do modelo epidemiológico SIR (Suscetíveis-Infectados-Recuperados), desenvolvido por McKendrick e Kermack em 1927, e entre as doenças que podem ser estudadas com este modelo encontram-se a Rubéola, o Sarampo e a Varíola. 

Todos os parâmetros usados no modelo podem ser alterados no nosso código, caracterizando assim diferentes doenças, sendo eles: 1. número total da população; 2. número inicial de infectados; 3. número inicial de mortes; 4. número inicial de recuperados; 5. taxa de infecção do patógeno; 6. taxa de recuperação dos infectados; 7. taxa de mortalidade do patógeno; 8. tempo de duração (em dias) da análise de infecção. Desta forma, o código retornaria ao usuário os dados relacionados do: 1. número de pessoas suscetíveis à infecção; 2. número de pessoas infectadas; 3. número de pessoas mortas. No arquivo "MACS - Projeto.py" temos o código com o modelo e os gráficos com as 3 curvas representando as classes de pessoas durante a epidemia, que estão animados através da biblioteca "matplotlib.FuncAnimation".

UTILIZAÇÕES DO PROJETO PARA USUÁRIOS

Com o nosso código, o usuário pode ter uma noção básica do comportamento de uma doença em meio à uma população através dos gráficos obtidos, assim como ter uma noção de como mudar os parâmetros da doença afetam o seu desenvolvimento. Porém, nosso código também pode servir como base para outros tipos de simulação, afinal, dadas as regras sobre como o seu sistema evolui com o tempo, o usuário poderia facilmente modificar o código a fim de utilizá-lo para um outro tipo de simulação com comportamento parecido, como o crescimento de populações, por exemplo. 

FUTURAS ADIÇÕES NO CÓDIGO

Pensando na melhor utilização do código e na verossimilhança com o mundo real, vamos modificar o código para que este consiga simular o comportamento de "ondas de infecções" assim como observamos em casos reais. Além disso, da maneira como o código está funcionando atualmente, tudo está muito sensível à valores iniciais específicos e uma possível alteração neles (principalmente nas taxas de infecção, recuperação e morte) fazem a função explodir. Resultando em um gráfico inconsistente ou então em um erro apontado pelo python. Percebemos que a nossa lógica está funcionando, mas precisamos refinar a maneira que o programa faz isso, possibilitando que o usuário tenha uma experiência mais adequada com o uso.

COMO UTILIZAR O CÓDIGO (E ATUAL ESTADO DO CÓDIGO)

Nosso código, que está no arquivo 'MACS corrigida', consiste em 3 funções: 'simulate_virus_spread', que gera os dados da nossa simulação; 'plotagem', que gera o gráfico para essa simulação e salva essa imagem; e 'gera_gif', que gera um gif do gráfico e salva ele. 

A função 'simulate_virus_spread' recebe 8 argumentos, sendo eles os parâmetros da simulação: N (número total de pessoas do sistema); I0 (número inicial de pessoas infectadas); D0 (número inicial de pessoas mortas); R0 (número inicial de pessoas infectadas); beta (taxa de infecção); gamma (taxa de infecção); mu (taxa de mortalidade) e t_max (tempo de duração da simulação). Como retorno, ela devolve 3 listas que mostram a evolução do nosso sistema, sendo o primeiro retorno a lista 'susceptible', o segundo a lista 'infected' e por último a lista 'dead'. A função recebe os parâmetros da simulação, utiliza a modelagem que adaptamos do modelo SIR, e retorna as listas em questão. Ainda estamos testando o comportamento da nossa função conforme os parâmetros iniciais, e futuramente podemos inserir intervalos de parâmetros ideais para uma melhor simulação, para evitar possíveis comportamentos esquisitos da função. 

As duas outras funções, 'plotagem' e 'gera_gif', são basicamente opções de visualização dos dados obtidos da função 'simulate_virus_spread', sendo  'plotagem' para gerarmos um gráfico, e 'gera_gif' para gerar um gif. 

A função 'plotagem' recebe 4 argumentos: os 3 primeiros são as as listas que obtemos quando realizamos a simulação com a função 'simulate_virus_spread', ou seja, basta definirmos 3 variáveis que vão armazenar as listas de retorno dessa função, e a ordem das listas é: pessoas suscetíveis, infectadas e mortas, então esses 3 argumentos têm que estar nessa ordem. O último argumento, 'string', é o nome da imagem que será salva, sendo ela uma string.

A função 'gera_gif' recebe os mesmos argumentos da função 'simulate_virus_spread', porém temos um último argumento, sendo ele 'nome_arquivo', que é uma string que será o nome do seu arquivo gif. Ainda não decidimos o que é mais funcional para o usuário: deixar as funções independentes, como a 'simulate_virus_spread' e 'gera_gif', ou dependentes, como 'simulate_virus_spread' e 'plotagem', por isso fizemos as duas opções por enquanto, mas vamos dicidir isso e uniformizar todas as funções.
