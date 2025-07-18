# Level 1
it_companies = {"Google", "Apple", "Microsoft", "Amazon", "Facebook"}
print("Length:", len(it_companies))
# agregar 'Twitter'
it_companies.add("Twitter")
print("After adding Twitter:", it_companies)
# Insertar multiples empresas
it_companies.update(["IBM", "Oracle", "SAP"])
print("After adding multiple companies:", it_companies)
# Eliminaruna empresa
it_companies.remove("Google")
print("After removing Google:", it_companies)


# Level 2
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# unir a y b
print("A union B:", A | B)
# Interseccion
print("A intersection B:", A & B)

print("A subset of B:", A.issubset(B))

print("A and B disjoint:", A.isdisjoint(B))
# Unirse en A y B
print("A union B:", A.union(B))
print("B union A:", B.union(A))
# Eliminar conjuntos completamente
del A
del B

# Level 3
ages = [22, 19, 24, 25, 24, 25, 24]
ages_set = set(ages)
print("Length of list:", len(ages))
print("Length of set:", len(ages_set))
print("Set is smaller" if len(ages_set) < len(ages) else "List is smaller or equal")


print("String: Cadena de texto, List: Secuencia mutable, Tuple: Secuencia inmutable, Set: Colección única y no ordenada")

sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))