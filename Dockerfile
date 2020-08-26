#docker build -t shst .
#docker run -it --rm -v ~/Documents/GitHub/osm-extract-validator:/usr/node/ shst:latest /bin/bash
#docker run -it --rm -v ~/Documents/GitHub/osm-extract-validator:/usr/node/ shst:latest shst extract usr/node/Portland_Administrative_Sextants.geojson --out=usr/node/shst.geojson --metadata --tile-hierarchy=8 --tiles

FROM node:10

ENV NPM_CONFIG_PREFIX=/home/node/.npm-global
ENV PATH=$PATH:/home/node/.npm-global/bin

USER node
RUN npm install -g sharedstreets@0.12.4
