Python4Linguist
=============

Description
----------
This is a school project containing a script that parses KAF / NAF files in Python.

Installation
-----------
Clone the repository from github

````shell
git clone git@github.com:SBelkaid/Python4Linguist.git
````
You will need to have installed the lxml library for Python (http://lxml.de/). Usually just by running`pip install --user lxml` should be enough for installing lxml.

You will need to have installed the BeautifulSoup library for python (http://www.crummy.com/software/BeautifulSoup/). Usually just by running`pip install --user bs4` should be enough for installing bs4.

You will need to have installed the pykml library for Python. Usually just by running`pip install --user pykml` should be enough for installing pykml.

You will need to have installed the numpy library for Python. Usually just by running`pip install --user numpy` should be enough for installing numpy.

You will need to have installed the nltk library for Python nltk.org. Best thing to do is install Anaconda https://www.continuum.io/downloads, contains more usefull modules, such as numpy and pandas. 

Usage
-----

These are python scripts, that read a KAF or NAF file and parses it. It basically parses one KAF/NAF file
and extracts data using XPath. Make sure to place the folder containing theses (defined in parser.py as: ``DIR_NAME = 'thesis_vu_2015'``) in the same folder as the parser script. Example of usage:

```shell

NameOfComputer: python parser.py

NameOfComputer: python v2_vis.py
```

Results
-------------
parser.py generates scripties.json file containing parsed information from the XML files. It's a dictionairy
with the original folder structure of where the files where located and as mentioned earlier data that is parsed

scraper.py retrieves all dbpedia location urls from the scripties.json file and orders them on study program. Next it crawles the urls, parses the source and creates a dictionairy containing urls as keys and coordinates as values.

showStats.py prints some stats per language in programme and programme alone. To view the stats individually for a thesis do the folowing:

```shell

>>> import json
>>> scripties = json.load(open('scripties.json', 'r'))
>>> scripties['ges']['en'][u'Scriptie_Alders_trim.txt.naf.nohyphen']

```

The above will show all the stats available for the author. 

generateKML.py extracts all locations from all theses from one master programme, gather all coordinates for these entities and put them in KML.

Testing
-------------
In some docstrings test have been made available. These can be run like so: 

```shell 
python -m doctest parser.py -v
```

Visualistion
-------------
This is the visualisation of the frequency of the types per language:

![alt tag](https://github.com/SBelkaid/Python4Linguist/blob/master/images/Screen%20Shot%202016-03-30%20at%206.39.11%20PM.png)


Future Work
------------
Add multithreading

Contact
------

* Soufyan Belkaid
* s.belkaid@student.vu.nl
* Vrije University of Amsterdam

License
------
nothing special