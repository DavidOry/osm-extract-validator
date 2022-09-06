import geopandas as gpd
import pandas as pd
import osmnx as ox
import pickle

boundary_filename = "nw_pdx.geojson"
osm_filename = "Portland.osm"
pickle_filename = "osmnx-graph.pickle"

print("Reading boundary file...")
nw_pdx_gdf = gpd.read_file(boundary_filename)
print("Creating graph from XML...")
graph = ox.graph_from_xml(osm_filename, simplify = False)

print("Trimming graph...")
small_graph = ox.truncate.truncate_graph_bbox(
    graph, 
    nw_pdx_gdf.bounds.maxy[0], 
    nw_pdx_gdf.bounds.miny[0], 
    nw_pdx_gdf.bounds.maxx[0], 
    nw_pdx_gdf.bounds.minx[0]
)

link_gdf = ox.graph_to_gdfs(small_graph, nodes = False, edges = True)
link_gdf['osmid'] = (
 pd.DataFrame(link_gdf.osmid.tolist())
   .fillna('')
   .astype(str)
   .agg(','.join, 1)
   .str.strip(',')
)
link_gdf = link_gdf.reset_index()

print("Writing to disk...")
osmnx_gdf = link_gdf[['osmid', 'u', 'v', 'geometry']]
osmnx_gdf.to_file('osmnx_link_disk.geojson', driver='GeoJSON')
