# osm-extract-validator
Compare the OSM extraction procedures for OSMnx, OSM2GMNS and SharedStreets.

## Background
The travel modeling community is embracing OpenStreemMap (OSM) as a source for roadway networks. To use OSM in travel models, the source map needs to be [transformed into a routable network](https://medium.com/zephyrfoundation/osmnx-software-badge-3e206db65825). This repository compares the extractions created by several tools, including [OSMnx](https://github.com/gboeing/osmnx), [OSM2GMNS](https://github.com/jiawlu/OSM2GMNS), and [SharedStreets](https://sharedstreets.io/).  

## Instructions
The repository contains the OSM data for Portland, Oregon in both `XML` and protobuffer formats. Separate Python scripts and corresponding Docker containers are used to extract a database of routeable links from the OSM files using each of the packages. 

### OSMnx
1. `docker-compose up --build osmnx`
2. `docker-compose run osmnx bash`
3. `conda activate ox`
4. `python get-osmnx.py`

### OSM2GMNS
1. `docker-compose up --build osm2gmns`
2. `docker-compose run osm2gmns bash`
3. `python get-gmns.py`

### SharedStreets
1. `docker-compose up --build sharedstreets`
2. `docker run -it --rm sharedstreets shst extract usr/node/nw_pdx.geojson --out=usr/node/shst.geojson --metadata --tile-hierarchy=8 --tiles`

### Create Comparsions Between Extractions
1. See `compare-osm2gmns.ipynb` (no special Python environment needed)




