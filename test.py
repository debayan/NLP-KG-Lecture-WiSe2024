from rdflib import Graph

# Create a Turtle string
ttl_data = """
	@prefix dbr: <http://dbpedia.org/resource/> .
	@prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>.
	@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
	dbr:Ulm geo:lat "48.400002"^^xsd:double ;
		geo:long "9.983333"^^xsd:double .
"""

# Parse the Turtle data into a graph
graph = Graph()
graph.parse(data=ttl_data, format="turtle")

# Print all triples in the graph
print("Triples in the graph:")
for subj, pred, obj in graph:
    print(f"{subj} {pred} {obj}")

# Note: RDFLib does not enforce RDFS constraints
print("\nGraph successfully loaded.")

