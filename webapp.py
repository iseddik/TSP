import random
import streamlit as st
import itertools
from backend import TSPSolver
import numpy as np
import time

random.seed(42)

from streamlit_agraph import agraph, Node, Edge, Config

st.set_page_config(layout="wide")

integer_input = 0
st.markdown("<h1 style='text-align: center;'>Travelling salesman problem with DP </h1>", unsafe_allow_html=True)

with st.container(border=True):
    st.image("./images/123.png",use_column_width=True, width=300)
    st.markdown("<h1 style='text-align: lift;'>Parameter Tuning</h1>", unsafe_allow_html=True)
    config_nodes = st.slider('How many Cities?', 3, 100, 5)
    start_point = st.text_input("Enter the start city")

    try:
        value = int(start_point)
        if 0 <= value < int(config_nodes):
            start_point = value
        else:
            st.warning(f"Please enter an integer between 0 and {config_nodes-1}.")
            start_point = 0
    except ValueError:
        st.warning("The default value is 0.")
        start_point = 0

    try:
        integer_input = int(start_point)
        st.write("You entered:", integer_input)
    except ValueError:
        st.write("The default value is 0")

    start_solve = st.button("Find stream !")

    

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

conf_edges = [(s, t, random.randint(1, 10) if s!= t else 0) for s, t in itertools.product([i for i in range(config_nodes)], [i for i in range(config_nodes)])]

cities = sorted(list(set([city for city_tuple in conf_edges for city in city_tuple[:2]])))
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

start = time.time()
solver = TSPSolver(distance_matrix, integer_input)
solver.solve_tsp()
end = time.time()
print("Best tour:", solver.best_tour)
print("Length of best tour:", solver.best_length)




            
if(start_solve != True):
    for i in range(config_nodes):
        for j in range(config_nodes):
            if (i!=j):
                edges.append(Edge(source=str(i), 
                            label=str(distance_matrix[i, j]), 
                            target=str(j), 
                            length=700,
                            ) 
                        ) 
    
    
else:
    for edg in range(len(solver.best_tour)):
        edges.append(Edge(source=str(solver.best_tour[edg]), 
                        label=str(distance_matrix[solver.best_tour[edg], solver.best_tour[edg+1] if edg != len(solver.best_tour)-1 else 0]), 
                        target=str(solver.best_tour[edg+1] if edg != len(solver.best_tour)-1 else solver.best_tour[0]), 
                        length=500,
                        color="green"
                        ) 
                    ) 
    st.markdown(f"<h3 style='text-align: center;'>The optimal path is {'-'.join([str(v) for v in solver.best_tour])}-{integer_input}</h3>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center;'>With length tour equal to {solver.best_length}</h3>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center;'>This was done in {'{:.6f}'.format(end - start)} s </h3>", unsafe_allow_html=True)
config = Config(width=2000,
                height=1000,
                directed=True, 
                physics=True, 
                hierarchical=False,
                )



return_value = agraph(nodes=nodes, 
                    edges=edges, 
                    config=config)
