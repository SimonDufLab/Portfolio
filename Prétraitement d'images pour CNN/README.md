## Prétraitement : Réduire le bruit et recentrer les images

Dans le cadre du projet final pour IFT6390, nous devions, en équipe, élaborer un CNN qui devait être en mesure de classifier des images entourées de bruits dans leurs catégories respectives (31 classes).

Comme les images en entrée étaient énormément bruitées, j'ai élaboré le code suivant pour faire subir un prétraitement aux données. Le prétraitement permettait de détecter la figure centrale de l'entrée pour se recadrer autour de celle-ci. Le maximum de bruit possible était enlevé, tout en essayant de garder au maximum les informations pertinentes de l'image.

Ce prétraitement présentait le double avantage d'éliminer une grande partie du bruit des données et de réduire la taille des images en entrée, ce qui améliora la vitesse d'entraînement. Suite à ce prétraitement, les performances de notre CNN a augmenté d'environ 7%.

Grosso modo, le prétraitement se fait en balayant chaque image successivement pour détecter la taille des "amas" de pixel. On recadre ensuite autour de la zone comportant le plus grand amas, ce qui correspond au dessin présent au milieu du bruit. L'image résultante est ensuite nettoyée en supprimant les groupes de pixels jugés comme étant du bruit.

Note : les images étant en noir et blanc, la première étape pour calculer la taille des amas a été de ne considérer que les pixels dont la valeur dépassait un certain seuil. On comptait ensuite le nombre de pixels se touchant pour déterminer la taille des amas.

Par la suite, différentes variations de ce prétraitement ont été explorées : lissage des pixels, ajout d'une mesure de densité, etc.
