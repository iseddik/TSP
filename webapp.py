import random
import streamlit as st
import itertools

from streamlit_agraph import agraph, Node, Edge, Config




with st.container(border=True):
    st.markdown("<h1 style='text-align: center;'>Parameter Tuning</h1>", unsafe_allow_html=True)
    config_nodes = st.slider('How many Nodes?', 3, 100, 5)
    start_point = st.text_input("Enter an integer")
    try:
        integer_input = int(start_point)
        st.write("You entered:", integer_input)
    except ValueError:
        st.write("Please enter a valid integer")

print(type(start_point))

nodes = []
edges = []

for i in range(config_nodes):
    nodes.append( Node(id=str(i), 
                    label="city(" + str(i) +")", 
                    size=25, 
                    shape="circularImage",
                    image="https://github.com/iseddik/ViT/blob/main/rect3110.png",
                    color = "red" if i==integer_input else None)
                ) 

conf_edges = [(s, t) for s, t in itertools.product([i for i in range(config_nodes)], [i for i in range(config_nodes)])]

print(conf_edges)

for edg in conf_edges:
    if (edg[0] != edg[1]):

        edges.append( Edge(source=str(edg[0]), 
                        label=str(random.randint(5, 50)), 
                        target=str(edg[1]), 
                        length=700,
                        ) 
                    ) 

config = Config(width=2000,
                height=1000,
                directed=True, 
                physics=True, 
                hierarchical=False,
                )

return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)
