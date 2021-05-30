
# Overview

En este repo tenemos dos procesos separados. Por un lado nos encontramos con el paquete spotidy_data, que se encarga de recoger a información que necesitamos a través de la API de spotify.

Por otro lado, tenemos un jupyter notebook donde vamos a realizar un análisis para practicar y entender en mayor medida el algoritmo k-means de la librería scikit-learn de python. ¿Por qué lo utilizo con canciones? Primero, porque creo que tienen una serie de características que las hacen muy apropiadas para este tipo de análisis (aquellas que extraeremos de las features de la canción: danceability, acousticness, loudness...). En segundo lugar, porque lo estoy aplicando a un campo que domino profundamente. Esto me ayudará a detectar problemas mucho más fácilmente que si estuviera analizando radiaciones solares, por ejemplo. Por último, me parece muy divertido conocer cómo va a organizar una máquina la música dependiendo de sus características. Y si esa clasificación tendrá algo que ver con la que nosotros hemos hecho tradicionalmente a través de los géneros musicales.


## Installation

Instalaremos todos los requirements a través de este código:

```bash
pip install -r requirements.txt
```

Una vez instalados los requirements, sólo deberemos lanzar desde nuestra terminal lo siguiente para abrir nuevo servido local y poder trabajar con juypter:

```bash
jupyter notebook
```

## Usage

En este caso he trabajado con un dataset de spotify. Para extraerlo básicamente le he pedido que me devolviera el máximo número de resultados por década (1.000), desde los años 60. Esto hace un total de 7.000 canciones. Todo esto se realiza a través del módulo get_tracks_with_features del módulo spotify_data. Esto genera un csv que podemos trabajar en el jupyter notebook.

Para utilizar el paquete y que el módulos nos genere el csv que necesitamos (si no estáis a gusto con el que ya está listo en el repositorio), podéis lanzar este código:

env/bin/python -m spotify_data.get_tracks_with_features\
  --credentials_path credentials/spotify_credentials.json


## Documentation

- [K-Means](https://en.wikipedia.org/wiki/K-means_clustering)
- [Clustering Scikit-Learn](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
- [Scikit-Learn](https://scikit-learn.org/stable/index.html)
- [Query Explorer](https://ga-dev-tools.appspot.com/query-explorer)
