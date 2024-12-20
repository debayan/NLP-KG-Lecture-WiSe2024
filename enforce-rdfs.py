import rdflib
from rdflib.plugins.sparql import prepareQuery

# Initialize the RDF graph and parse the TTL data
g = rdflib.Graph()

ttl_data = """
	@prefix ex: <http://example.org/> .
	@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
	@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

	ex:isMarriedTo rdfs:domain ex:Person ;
                rdfs:range ex:Person .

	ex:instituteAKSW rdf:type ex:Institution .

	ex:Max ex:isMarriedTo ex:instituteAKSW .
	"""

g.parse(data=ttl_data, format="ttl")
# Enable RDFS reasoning

# SPARQL query to find violations based on domain and range constraints
query = """
SELECT ?subject ?predicate ?object
WHERE {
  ?predicate rdfs:domain ?domain .
  ?predicate rdfs:range ?range .
  ?subject ?predicate ?object .
  FILTER (?subject != ?domain || ?object != ?range)
}
"""

# Prepare and execute the query
results = g.query(query)

# Print the violations
violations = list(results)
if violations:
    for subject, predicate, object_ in violations:
        print(f"Violation: {subject} {predicate} {object_}")
else:
    print("No violations found.")

