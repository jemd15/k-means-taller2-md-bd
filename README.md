# k-means para el desarrollo del Taller nº2 de Minería de Datos y Big Data

Este respositorio consta de 2 archivos principales con los cuales se calcula el método de agrupación k-means.

Para correr los archivos se necesita un dataset en formato `.csv` separado por `,` (como el archivo `cars.csv` adjunto para este taller en este mismo repositorio), además de instalar las librerías 
`numpy, matplotlib y sklearn`, las cuales se instalan con el siguiente comando:

```sh
pip install numpy matplotlib sklearn
```

Lo primero es correr el archivo `calculate_clusters.py` que muestra un gráfico desde donde se puede aplicar el método 
del codo para determinar cuántos clusteres son óptimos para la implementación del método k-means. El comando para correr el código es:

```sh
python calculate_clusters.py
```

Luego, es necesario modificar la variable `n_clusters` del archivo `k-means.py` con la cantidad de clusters obtenida en la ejecución anterior y correr el archivo con el comando:

```sh
python k-means.py
```

Esto mostrará una gráfica con la agrupación realizada y separada por colores.

License
----

MIT
