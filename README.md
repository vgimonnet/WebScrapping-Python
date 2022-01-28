# ECV Digital M2 DEV - Python Webscrapping
## Valentin GIMONNET

J'ai décidé d'aller scrapper le site [l'atelier de la bière](https://www.latelierdesbieres.fr) pour récupérer du contenu sur les bières, brasseries, styles de bières.

Pour le projet personnel de fin d'année je suis en train de faire une application de collection / partage de données sur la bière avec deux app (frontoffice et backoffice) en Vue.js et une api en Node.js.

Les données scrappées sur le site vont me permettre de commencer à remplir ma base de données.

Le script Python me génère 1 fichier db.json avec des tableaux d'objets beers[], breweries[], styles[]

Utilisation de [json-server](https://pypi.org/project/json-server.py/) pour une api rapide basée sur le fichier db.json.
Je vais faire des calls à l'api json-server depuis mon api Nodejs pour remplir ma base de données.

L'utilisation de l'api json-server dans mon api me permet de coupler le projet Scripting Python avec le projet NodeJs de Louis et de répondre à un de ces critères d'évalutations en faisant des calls vers une autre api.
