# LobbyView
Exploring the structure and development of networks between lobbying firms and politicians using data from the LobbyView API.

## Motivation
One area of interest for our group is social network analysis. While we have scratched the surface of this subject in a couple of our classes, we want to focus on a project that will allow us to explore the structure and development of such networks and to build machine learning models that can accurately predict changes in them. We are also interested in the influence of lobbying in American politics and hope our work can contribute, in some small way, to the discussion around politics, influence, and democracy in the U.S. 

## Methods
We expect to apply k-means clustering, agglomerative clustering and link prediction, while using a variety of models (logistic regression, Naive Bayes, etc.) as well as related techniques like feature extraction, cross validation, and hyper-parameter search.

## Datasets
We will use data from LobbyView which provides an API for accessing data on lobbying firms, lobbyists, congressional bills, government entities, dollar amounts, and related details. We may add in data from other sources including OpenSecrets.org and FollowTheMoney.org.

## Evaluation
The core aspect of our experiment will be link prediction between lobbyists and politicians. As mentioned, we have various methods/models in mind to lead to “successful” link prediction. In terms of evaluating our work we plan to 1) rely on a random predictor to create edges between lobbyist and politician nodes that didn’t exist in the training set (this will act as a benchmark), 2) generate edge predictions at various time intervals using the aforementioned models, and 3) measure the accuracy of the models using some combination of graph distance, common neighbors and an Adamic/Adar similarity measure based on neighbors. 

## Computing
We assume we will require a database like PostgreSQL, local storage on the order of 10s of GBs, and approximately 12 to 16 GB of RAM.

## Existing Work
The closest related work was completed by the creators of Lobby View (see the paper Kim, In Song (2018). "LobbyView: Firm-level Lobbying & Congressional Bills Database."), tangentially related research on link prediction in bipartite networks (see the paper Benchettara, N., Kanawati, R., & Rouveirol, C. (2010, August). Supervised machine learning applied to link prediction in bipartite social networks. In 2010 International Conference on Advances in Social Networks Analysis and Mining (pp. 326-330). IEEE.), and research on link prediction (see the paper Liben‐Nowell, D., & Kleinberg, J. (2007). The link‐prediction problem for social networks. Journal of the American society for information science and technology, 58(7), 1019-1031.)

## Duty of each group member
While tasks have not been divided at this time, the group will split responsibilities evenly, using either a GitHub repository or a Google Colab notebook to share code, analysis, model building, and model evaluation tasks.
