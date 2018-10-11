# Análisis Bayesiano de datos

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/PrACiDa/EBAD/master)

Este repositorio contiene una introducción a la estadística Bayesiana usando Python. Este material es **trabajo en progreso** pero es en general usable.


## Cómo usar este material

* Versión estática: Al hacer click en los archivos que se muestran arriba (los que empiezan con 01_, 02_, 03_, etc) podrás leer una versión estática del material. Es decir podrás ver el texto y las figuras pero no podrás modificarlos, ni interactuar con el material.

* Versión interactiva online. Al hacer click [acá](https://mybinder.org/v2/gh/PrACiDa/EBAD/master) podrás correr una versión _online_.

* Versión interactiva local. También es posible descargar el material y ejecutarlo en tu propia computadora. Para ello has click [acá](https://github.com/PrACiDa/EBAD/archive/master.zip) y sigue las instrucciones de la próxima sección (Instalación).


## Instalación
Para usar este material es necesario tener instalado Python. Se recomienda la versión 3.6 o superior. Además es necesario instalar los siguientes paquetes:

* PyMC3 3.5
* NumPy 1.15
* SciPy 1.1
* Matplotlib 2.2.2
* Ipython 6.5
* Jupyter 1.0.0
* seaborn 0.9
* ArviZ 0.1

Se recomienda instalar primero [Anaconda](https://www.continuum.io/downloads). Luego instalar el resto de los paquetes con los comandos:

* `conda install -c conda-forge pymc3 jupyter ipython seaborn`

* `pip install git+git://github.com/arviz-devs/arviz.git`


## Contribuciones
Todo el contenido de este repositorio es abierto, esto quiere decir que cualquier persona interesada puede contribuir al mismo. Todas las contribuciones serán bien recibidas incluyendo:

* Correcciones ortográficas
* Nuevas figuras
* Correcciones en el código Python, incluidas mejoras de estilo
* Mejores ejemplos
* Mejores explicaciones 
* Correcciones de errores conceptuales

La forma de contribuir es vía Github, es decir los cambios deberán ser hechos en forma de _pull requests_ y los problemas/bugs deberán reportarse como _Issues_.


## Para seguir leyendo

* [Statistical Rethinking](http://xcelab.net/rm/statistical-rethinking/) de Richard McElreath
* [Doing Bayesian Data Analysis](https://sites.google.com/site/doingbayesiandataanalysis/) (2 edición) de John Kruschke
* [Data Analysis: A Bayesian Tutorial](https://www.amazon.com/Data-Analysis-Bayesian-Devinderjit-Sivia/dp/0198568320) de Devinderjit Sivia & John Skilling
* [Bayesian Data Analysis](http://www.stat.columbia.edu/~gelman/book/) de Andrew Gelman y otros.

* Material online con tópicos Bayesianos:
    * [Publishable Stuff](http://sumsar.net/)
    * [Probably Overthinking It](http://allendowney.blogspot.com.ar/)
    * [While My MCMC Gently Samples](http://twiecki.github.io/)
    * [Count Bayesie](https://www.countbayesie.com/)
    * [Bayesian Methods for Hackers](http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/#contents)


* Las plantillas utilizadas para generar los diagramas de Kruschke, fueron creadas por [Rasmus Bååth's](http://sumsar.net/blog/2013/10/diy-kruschke-style-diagrams/)
