Python4Linguist
=============

Description
----------
This is a school project containing a parser for KAF or NAF files in python.

Installation
-----------
Clone the repository from github

````shell
git clone git@github.com:SBelkaid/Python4Linguist.git
````
You will need to have installed the lxml library for python (http://lxml.de/). Usually just by running`pip install --user lxml` should be enough for installing lxml.


Usage
-----

This library is a python module, that reads a KAF or NAF file and parses it. It basically parses one KAF/NAF file
and allows to access to all the layers through different methods and functions. This is one example of usage:
```shell
python

python parser.py

python v2_vis.py
```

Results
-------------
parser.py generates scripties.json file containing parsed information from the XML files. It's a dictionairy
with the original folder structure of where the files where located and as mentioned earlier data that is parsed

scraper.py retrieves all dbpedia location urls from the scripties.json file and orders them on study program. Next it crawles the urls, parses the source and creates a dictionairy containing urls as keys and coordinates as values.

v2_vis.py creates a folder containing kml files ordered on study program, that can be used to visualize the locations on a map. 

Documentation
-------------
The documentation can be generated automatically by running:
```shell
epydoc --config documentation.cfg
```

This will call to the external program epydoc (http://epydoc.sourceforge.net/) with the provided configuration file, and will create the HTML documents
for the API in the folder `apidocs`. As said before the already generated documentation can be seen at http://kyoto.let.vu.nl/~izquierdo/api/KafNafParserPy

Contact
------

* Soufyan Belkaid
* s.belkaid@student.vu.nl
* Vrije University of Amsterdam

License
------
nothing special