## Traitement de données de la LNH à partir classificateurs linéaire

Dans ce projet, il s'agissait de tester la capacité de différents classificateurs linéaires à prédire certaines données intéressantes. Le but ici était de savoir si, à partir de données facilement accessibles (temps de glace, position, tirs au but, etc.) il était possible de prédire les différents indices de production offensive d'un joueur de la LNH.

Différents modèles ont d'abord été explorés, puis une sélection de variables a été tentée à l'aide de la méthode dite de "Bolasso". Les modèles ont ensuité été réentraînés avec les variables sélectionnées pour voir quelle serait la variation de perte de nos prédicateurs.

Les modèles ont été produits à l'aide de la bibliothèque Scikit-Learn.
