import random
import streamlit as st

from streamlit_agraph import agraph, Node, Edge, Config




with st.container(border=True):
    st.markdown("<h1 style='text-align: center; color: white;'>Parameter Tuning</h1>", unsafe_allow_html=True)
    config_nodes = st.slider('How many Nodes?', 3, 100, 5)



nodes = []
edges = []

for i in range(config_nodes):
    nodes.append( Node(id=str(i), 
                    label="city(" + str(i+1) +")", 
                    size=25, 
                    shape="circularImage",
                    image="images\path1582.png") 
                ) # includes **kwargs




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
