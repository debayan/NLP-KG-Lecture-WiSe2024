from rdflib import Graph

# Create a Turtle string
ttl_data = """
@prefix ex: <http://example.org/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ex:isMarriedTo rdfs:domain ex:Person ;
               rdfs:range ex:Person .

ex:instituteAKSW rdf:type ex:Institution .

ex:Max ex:isMarriedTo ex:instituteAKSW .
"""

# Parse the Turtle data into a graph
graph = Graph()
graph.parse(data=ttl_data, format="turtle")

# Print all triples in the graph
print("Triples in the graph:")
for subj, pred, obj in graph:
    print(f"{subj} {pred} {obj}")

# Note: RDFLib does not enforce RDFS constraints
print("\nGraph successfully loaded. RDFLib does not enforce RDFS constraints.")

