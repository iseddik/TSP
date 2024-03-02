import random
import streamlit as st
import itertools
from backend import TSPSolver
import numpy as np

from streamlit_agraph import agraph, Node, Edge, Config


integer_input = 0

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

conf_edges = [(s, t, random.randint(1, 100) if s!= t else 0) for s, t in itertools.product([i for i in range(config_nodes)], [i for i in range(config_nodes)])]


cities = sorted(list(set([city for city_tuple in conf_edges for city in city_tuple[:2]])))

num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities), dtype=int)
city_index_map = {city: index for index, city in enumerate(cities)}

for city_tuple in conf_edges:
    city1, city2, distance = city_tuple
    index1 = city_index_map[city1]
    index2 = city_index_map[city2]
    distance_matrix[index1, index2] = distance
    distance_matrix[index2, index1] = distance
print(distance_matrix)
print(conf_edges)

solver = TSPSolver(distance_matrix, integer_input)
solver.solve_tsp()
print("Best tour:", solver.best_tour)
print("Length of best tour:", solver.best_length)

for edg in conf_edges:
    if (edg[0] != edg[1]):

        edges.append( Edge(source=str(edg[0]), 
                        label=str(edg[2]), 
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
