





<h1> Índice </h1>

<h3>

• [Problemas de Negócio](https://github.com/JeffersonMedines/rossmann_store_sales/blob/main/README.md#-problemas-de-neg%C3%B3cio-)

• [Premissas do Negócio](https://github.com/JeffersonMedines/rossmann_store_sales/blob/main/README.md#-premissas-do-neg%C3%B3cio-)

• [Planejamento da Solução](https://github.com/JeffersonMedines/rossmann_store_sales/blob/main/README.md#-planejamento-da-solu%C3%A7%C3%A3o-)

• [Machine Learning e Métricas de Performance](https://github.com/JeffersonMedines/rossmann_store_sales/blob/main/README.md#-machine-learning-e-m%C3%A9tricas-de-performance-)

• [Resultados Financeiros para o Negócio](https://github.com/JeffersonMedines/rossmann_store_sales/blob/main/README.md#-resultados-financeiros-para-o-neg%C3%B3cio-)

• [Deploy do Modelo com o Bot do Telegram](https://github.com/JeffersonMedines/rossmann_store_sales/blob/main/README.md#-deploy-do-modelo-com-o-bot-do-telegram-)

• [Próximo Ciclo](https://github.com/JeffersonMedines/rossmann_store_sales/blob/main/README.md#-pr%C3%B3ximo-ciclo-)
 
 </h3>

<h1> Problemas de Negócio </h1>

<p> A Rossmann opera mais de 3.000 drogarias em 7 países europeus. Atualmente, os gerentes de loja da Rossmann tem a tarefa de prever suas vendas diárias para as próxmas seis semanas. As vendas das lojas são influenciadas por muitos fatores como promoções, competição, feriados escolares e estudais, sazonalidade e localidade. </p>

<p> Com milhares de gerentes individuais prevendo a venda de suas lojas com base nas suas circunstâncias únicas, a precisão dos resultados se mostra bastante variada. Além disso, a entrega das previsões são feitas manualmente dificultando ter uma base de dados completa para análise, e limitando a consulta dessas previsões por um computador. </p>

<p> A previsão das vendas foi solicitada pelo CFO em uma reunião mensal de resultados. O CFO planeja realizar uma reforma das lojas e a causa raiz desse problema é determinar o valor do investimento para a reforma de cada loja, já que o CFO planeja utilizar parte da receita das próximas 6 semanas como fonte desse investimento. </p>

<h1> Premissas do Negócio </h1>

<p> Competition Distance: Esse dado está expresso em metros e as vezes possui valor zero. Será considerado que esses valores zeros indicam que não exista nenhum competidor próximo, e para que isso seja aprendido de forma eficaz pelos algoritmos de Machine Learning, será fixado um valor muito maior que o máximo de distância até o competidor mais próximo (200.000 m). </p>

<p> Assortment: De acordo com as categorias de assortment (A, B e C), será considerada uma ordem hierarquica entre os tipos, onde o tipo A possui o assortment mais simples, e o tipo C o assortment mais variado. </p>

<p> Store Open: Foram removidas todas as linhas onde as lojas estavam fechadas por conta das vendas serem sempre zero nesses dias e não ter necessidade de previsão. Analisar o impacto de se remover esses dias será um ponto em um próximo cíclo de desenvolvimento CRISP-DM. </p>


<h1> Planejamento da Solução </h1>

<p> Esse projeto foi desenvolvido utilizando a metodologia cíclica CRISP-DM. De forma resumida, essa metodologia mostra algumas etapas que devem ser executadas para se desenvolver e aplicar um projeto de ciência de dados na indústria para se gerar valor de forma eficiente. </p>

<p> 00. Entendendo o Problema de Negócio: Nessa etapa buscamos entender a causa raiz do problema, de onde ele surgiu e qual a dor que esse problema gera. Compreender o problema de forma profunda evita o desenvolvimento de uma solução que não solucione o problema por conta de um telefone sem fio entre a pessoa que sente a dor desse problema, e o cientista de dados que irá desenvolver a solução para esse problema. </p>

<p> 01. Descrição dos Dados: Aqui é utilizado estatística descritiva para compreender as características dos dados que serão trabalhados e realizar algumas limpezas como renomear colunas e identificar/preencher NA's. </p>

<p> 02. Feature Engineering: Nessa parte eu criei um mindmap sobre o fenômeno que estou modelando (venda diária das lojas) para entender melhor o funcionamento do modelo de negócio para criar hipóteses. Aqui após criar a lista de hipóteses também criamos novas variáveis ou transformamos as já existentes que serão necessárias para validar essas hipóteses. </p>

<p> 03. Filtragem de Feature: Aqui será selecionada quais linhas e colunas do dataset seguirão para as próximas etapas. Essa seleção envolve o entendimento das restrições de negócio, como por exemplo, no momento da predição não temos a informação de quantos clientes estarão presente na loja, por conta disso a coluna customers é excluída. </p>

<p> 04. Análise Exploratória de Dados: Essa etapa é dividida em 3 partes. Na primeira é feita a análise univariada, onde analisamos a distribuição da variável resposta (aquela que o modelo quer prever, as vendas diárias) e também a distribuição das variáveis preditoras (as demais variáveis) em relação a variável resposta. Na segunda parte é feita a análise bivariada, que é aonde iremos validar a lista de hipóteses que criamos na etapa de engenharia de feature. Na último parte é feita a análise multivariada onde é analisada a correlação entre todas as variáveis do dataset. </p>

<p> 05. Prepração dos Dados: Aqui iremos preparar os dados de uma forma que os algoritmos de ML possam aprender de forma mais eficiente. Como por exemplo fazer o encoding de variáveis categóricas para transformá-las em numéricas. </p>

<p> 06. Feature Selection: Nessa parte é aplica um algoritmo de Machine Learning para identificar quais são as features mais importantes para o aprendizado do fonêmeno modelado (vendas diárias das lojas). Somamos a essa recomendação do algoritmo, o conhecimento de negócios que desenvolvemos até esse momento do projeto para também acrescentar algumas features que acreditamos ser importantes mas que form julgadas como não importantes pelo algoritmo. </p>

<p> 07. Modelagem de Machine Learning: Nessa etapa é definido quais serão os algoritmos de machine learning a serem aplicados, e também é feita a aplicação deles calculando as métricas de performance. </p>

<p> 08. Hyperparameter Fine Tuning: Os algoritmos de Machine Learning possuem parâmetros onde podemos passar valores que irão determinar o quão simples ou complexo será o aprendizado desse algoritmo. Nessa parte do projeto o objetivo é identificar qual o conjunto de valores que permita o algoritmo se aproximar ao máximo do seu desempenho. </p>

<p> 09. Tradução e Interpretação do Erro: Aqui o objetivo é traduzir as métricas de performance dos algoritmos para os resultados de negócio, ou seja, qual o impacto financeiro que a performance desse algoritmo está causando na empresa. </p>

<p> 10. Deploy do Modelo em Produção: Finalmente, após finalizar o projeto chega o momento de publicar essa solução em um ambiente cloud para que possa ser utilizado por outras pessoas de qualquer lugar e em qualquer momento. </p>


<h1> Machine Learning e Métricas de Performance </h1>

<p> A estratégia de apliação dos modelos de previsão nesse projeto seguiram o conceito estatístico de Occams Razor, que diz que entre dois modelos que explicam o mesmo fenômeno, devemos sempre escolher o de menor complexidade, o que faz todo o sentido já que os algoritmos de Machine Learning não devem ser bons em decorar combinações, e sim serem bons em generalizar para conseguir prever a maior quantidade de cenários futuros, até mesmo aqueles que ele não aprendeu quando foi treinado. </p>

<p> Por isso, primeiro foi aplicado um modelo baseline (o modelos mais simples possível para usar como base de desempenho) que foi a média. Após isso, dois algoritmos simples de regressão linear (regressão normal e de Lasso) foram aplicados para comparar com o modelo baseline e compreender o nível de complexidade do fenômeno modelado (venda diária das lojas). Analisando o desempenho dos 3 modelos, o modelo baseline mostra um desempenho muito superior aos modelos de regressão linear nos indicando que esse fenômeno é complexo e necessita de algoritmos mais robustos. </p>

| Model Name  |  MAE  |  MAPE  |  RMSE  |
| ------------------- | ------------------- | ------------------- | ------------------- |
|  Average Model |  1354.80 |  0.2064 |  1835.13 |
|  Linear Regression |  2083.17 +/- 294.98	 |  0.3 +/- 0.02 |  2958.87 +/- 466.72 |
|  Linear Regression - Lasso |  2117.66 +/- 340.94 |  0.29 +/- 0.01 |  3061.89 +/- 503.23 |

<p> Então, foram aplicados dois algoritmos mais robustos, a Random Forest Regressor e o XGBoost Regressor. A performance dos dois algoritmos foram bem próximas e muito melhor do que os 3 primeiros modelos aplicados. Enquanto que a Random Forest apresentou um erro médio menor que o XGBoost, o XGBoost apresentou menor variância. A escolha do algoritmo foi definida então pelo custo de produção sendo escolhido o XGBoost, já que o modelo Random Forest normalmente exige muito mais memória da cloud para ser colocado em produção tendo um custo muito maior que o modelo XGBoost, logo, essa pequena queda na performance é muito compensado por um custo de produção muito menor. </p>

| Model Name  |  MAE  |  MAPE  |  RMSE  |
| ------------------- | ------------------- | ------------------- | ------------------- |
|  Random Forest |  837.7 +/- 219.24 |  0.12 +/- 0.02 |  1256.59 +/- 320.28 |
|  XGBoost Regressor |  913.11 +/- 161.5	 |  0.13 +/- 0.02 |  1306.38 +/- 236.62 |

<p> Após a etapa de ajuste dos hiperparâmetros, o modelo XGBoost apresentou uma melhora no seu desempenho: </p>

| Model Name  |  MAE  |  MAPE  |  RMSE  |
| ------------------- | ------------------- | ------------------- | ------------------- |
|  XGBoost Regressor Tuned |  710.82 |  0.1031 |  1018.85 |

<p> Ao analisar as métricas de desempenho do modelo, podemos perceber:

1. Com o MAE sabemos que o modelo pode errar x tanto acima do valor quanto abaixo do valor real.

2. O MAPE mostra em porcentagem o quanto nossa previsão errou em relação ao valor real, ou seja, ele mostra qual o valor percentual que o MAE representa do valor real.

3. Já o RMSE também como o MAE mostra em valor bruto o quanto uma previsão pode errar acima ou abaixo do valor real, porém, essa métrica de performance é sensível a outliers (valores extremos) e por isso podemos ter uma noção se as previsões possuem muitos outliers ou não comparando com o MAE. </p>


<h1> Resultados Financeiros para o Negócio </h1>

<p> Na tabela abaixo podemos ver qual será o valor total de vendas predito pelo modelo de todas as lojas, e quais os possíveis valores de um melhor e pior cenário. O melhor cenário foi calculado somando o valor total predito com o valor total MAE de todas as lojas, e o pior cenário possível subtraindo o valor toal MAE de todas as lojas: </p>

| Scenarios  |  Values  |
| ------------------- | ------------------- |
|  predictions |  R$ 283,744,256.00 |
|  worst_scenario |  R$ 282,948,122.76 |
|  best_scenario |  R$ 284,540,394.96 |

<p> O gráfico a seguir mostra qual foram os valores reais das vendas e quais foram os valores preditos pelo modelo: </p>

![image](https://user-images.githubusercontent.com/93053350/178326406-0878b201-37bc-4c2d-9ab3-da82eb849237.png)


<p> Essas sãos as 10 lojas que apresentam os maiores valores de MAPE e por isso devem ter uma análise específica para se decidir o budget de investimento para as reformas: </p>

store  |  predictions  |  worst_scenario  |  best_scenario  |  MAE  |  MAPE
| ------------------- | ------------------- | ------------------- | ------------------- | ------------------- | ------------------- 
292  |  R$ 105597.61  |  R$ 102300.05  |  R$ 108895.18  |  3297.56  |  0.550666
909  |  R$ 234382.89  |  R$ 226688.75  |  R$ 242077.03  |  7694.13  |  0.519254
876  |  R$ 190734.37  |  R$ 186527.82  |  R$ 194940.92  |  4206.55  |  0.316381
183  |  R$ 210616.85  |  R$ 209000.06  |  R$ 212233.65  |  1616.79  |  0.276576
274  |  R$ 190166.06  |  R$ 188649.11  |  R$ 191683.01  |  1516.95  |  0.260754
1039  |  R$ 352841.84  |  R$ 350882.09  |  R$ 354801.59  |  1959.74  |  0.258197
286  |  R$ 159969.48  |  R$ 159260.94  |  R$ 160678.02  |  708.54  |  0.217607
931  |  R$ 159882.18  |  R$ 158915.45  |  R$ 160848.92  |  966.73  |  0.206191
534  |  R$ 297989.31  |  R$ 296702.56  |  R$ 299276.05  |  1286.74  |  0.205161
550  |  R$ 222975.89  |  R$ 221989.05  |  R$ 223962.72  |  986.83  |  0.202784

<h1> Deploy do Modelo com o Bot do Telegram </h1>

<p> O modelo foi colocado em produção utilizando o bot do aplicativo telegram. A partir dele é possível acessar as previsões de qualquer lugar e até mesmo pelo celular. Para acessar é super simples, basta pesquisar pelo chat do bot que é o @sales_predict_rossmann_bot no aplicativo e entrar na conversa. Após isso basta clicar em iniciar que a conversa será iniciada.  </p>

<p> Para ter a previsão de uma loja específica é necessário passar o número de ID dessa loja com uma barra antes indicando o comando para o bot, após isso o bot irá retornar qual é o valor total previsto que essa loja irá vender nas próximas 6 semanas. O bot também irá indicar caso o ID da loja não esteja disponível para realizar previsões, ou caso o ID tenha sido digitado no formato errado. </p>



https://user-images.githubusercontent.com/93053350/178326451-6bd2cbc9-02d8-446e-94d0-b046dea45b0a.mp4



<h1> Próximo Ciclo </h1>

<p> Implementar técnicas mais aprofundadas de feature engineering e feature selection para melhorar significativamente o desempenho do modelo. </p>

<p> Durante a análise de resíduos foi identificado que os maiores erros se encontram entre as previsões de R$5.000 a R$10.000. Investigar a causa e implementar uma solução. </p>

![image](https://user-images.githubusercontent.com/93053350/178326367-bfc89db3-dfef-4e82-af48-29740bbb1f5a.png)

