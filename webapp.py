import random
import streamlit as st

from streamlit_agraph import agraph, Node, Edge, Config




with st.container(border=True):
    st.markdown("<h1 style='text-align: center; color: white;'>Parameter Tuning</h1>", unsafe_allow_html=True)
    clusters = st.slider('How many Nodes?', 3, 100, 5)



nodes = []
edges = []
nodes.append( Node(id="Spiderman", 
                   label="Peter Parker", 
                   size=25, 
                   shape="circularImage",
                   image="images\path1582.png") 
            ) # includes **kwargs
nodes.append( Node(id="Captain_Marvel", 
                   size=25,
                   shape="circularImage",
                   image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png") 
            )
edges.append( Edge(source="Captain_Marvel", 
                   label="friend_of", 
                   target="Spiderman", 
                   # **kwargs
                   ) 
            ) 

config = Config(width=750,
                height=950,
                directed=True, 
                physics=True, 
                hierarchical=False,
                # **kwargs
                )

return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)
