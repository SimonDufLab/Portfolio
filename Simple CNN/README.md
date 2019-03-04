## Simple CNN, modèle VGG, classifications entre chiens et chats.

Petit CNN, construit avec Pytorch

Voici un CNN construit pour le cours IFT 6135 pour distinguer des images de chiens et de chats. Les paramètres présentés dans le code plus haut sont ceux qui ont été retenus
après avoir exploré différents paramètres.

Notons que l'utilisation de certaines fonctionnalités de Pytorch (batchnorm, dropout) n'était pas permise. De même seule l'utilisation de la SGD par mini-batch était permise,
ce qui explique que ADAM ou d'autres méthodes d'optimisation ne soient pas utilisées.

Le code était exécuté à l'aide de Google Colab pour pouvoir rouler sur un GPU.
