import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
from handlers import * 


m = leafmap.Map(tiles="stamentoner")



with st.sidebar:
    st.markdown("<h1 style='color: aqua; text-align: center;'>AS MAP</h1>",unsafe_allow_html=True)
    baseList = st.selectbox("Choose your Basemap",('Open Street Map','Google HYBRID','Esri NatGeoWorld'))
    if baseList == "Open Street Map":
        pass         
    elif  baseList == "Google HYBRID":
         m.add_basemap("HYBRID")
        # m.add_tile_layer(
        #     url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
        #     name="Google Satellite",
        #     attribution="Google",
        #     )
    elif baseList == 'Esri NatGeoWorld':
        m.add_basemap("Esri.NatGeoWorldMap")
    heatFile = st.file_uploader("upload file for heat map",type="geojson")
    if heatFile:
        # filepath = "./reprojected.geojson"
        gfile = gpd.read_file(heatFile)
        st.write(gfile.crs)
        st.write(gfile.crs==3857)
        if not gfile.crs == 3857:
            gfile = gfile.to_crs(3857)
        m.add_gdf(gfile)
    #     m.add_heatmap(
    #     filepath,
    #     latitude="latitude",
    #     longitude="longitude",
    #     value="pop_max",
    #     name="Heat map",
    #     radius=20,
    # )




m.to_streamlit(width=1000,height=700)



