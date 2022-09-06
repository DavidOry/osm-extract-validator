import geopandas as gpd
import osm2gmns as og

pdx_pbf_filename = "Portland.osm.pbf"
boundary_filename = "nw_pdx.geojson"

nw_pdx_gdf = gpd.read_file(boundary_filename)

nw_pdx_bbox = (
    nw_pdx_gdf.bounds.miny[0], 
    nw_pdx_gdf.bounds.minx[0], 
    nw_pdx_gdf.bounds.maxy[0], 
    nw_pdx_gdf.bounds.maxx[0]
)

net = og.getNetFromFile(
    filename = pdx_pbf_filename,
    network_types = ('auto','bike','walk'),
    bbox = nw_pdx_bbox,
    default_lanes = True,
    default_speed = True,
    default_capacity = True,
) 

og.outputNetToCSV(net, output_folder = ".")


