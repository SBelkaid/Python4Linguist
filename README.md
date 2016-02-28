Python4Linguist
=============

Description
----------
This is a school project containing script that parses KAF / NAF files in python.

Installation
-----------
Clone the repository from github

````shell
git clone git@github.com:SBelkaid/Python4Linguist.git
````
You will need to have installed the lxml library for python (http://lxml.de/). Usually just by running`pip install --user lxml` should be enough for installing lxml.

You will need to have installed the pykml library for python. Usually just by running`pip install --user pykml` should be enough for installing pykml.

You will need to have installed the nltk library for python nltk.org. Best thing to do is install Anaconda https://www.continuum.io/downloads, contains more usefull stuff. 

Usage
-----

These are python scripts, that read a KAF or NAF file and parses it. It basically parses one KAF/NAF file
and extracts data using XPath. Make sure to place the folder containing theses in the same folder as the parser script. Example of usage:

```shell

SomeonesComputer:python parser.py

SomeonesComputer:python v2_vis.py
```

Results
-------------
parser.py generates scripties.json file containing parsed information from the XML files. It's a dictionairy
with the original folder structure of where the files where located and as mentioned earlier data that is parsed

scraper.py retrieves all dbpedia location urls from the scripties.json file and orders them on study program. Next it crawles the urls, parses the source and creates a dictionairy containing urls as keys and coordinates as values.

v2_vis.py extract all locations from all theses from one master programme, gather all coordinates for these entities and visualize them using KML.

Future Work
------
Add multithreading

Contact
------

* Soufyan Belkaid
* s.belkaid@student.vu.nl
* Vrije University of Amsterdam

License
------
nothing special