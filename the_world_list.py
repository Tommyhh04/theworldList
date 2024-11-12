#Ønskeliste over plasser jeg ønsker å besøke i ingen spesifikk rekkefølge

ønskeliste = ["hawaii", "new zealand", "japan", "sør-korea", "thailand", "bora bora"]

#Ønskelisten blir sortert i alfabetisk rekkefølge (sort gjør listen sortert permanent)
ønskeliste.sort()

#Om listen ønskes sortert omvendt alfabetisk så gjør du som kommentert kode under
#ønskeliste.sort(reverse=True)

print(ønskeliste)



#Tilfeldige plasser generert av chatgpt for neste oppgave
#(sorted) gjør at listen ikke blir permanent sortert og som du kan se i koden under så kan orginal listen hentes igjen

plasser = [    "Paris, France",    "Tokyo, Japan",    "Rio de Janeiro, Brazil",    "Dubai, United Arab Emirates",    "Sydney, Australia",    "Cape Town, South Africa",    "New York City, USA",    "Barcelona, Spain",    "Istanbul, Turkey",    "Machu Picchu, Peru"]

print("Her er orginal listen")
print (plasser)

print("\nHer er listen sortert med 'sorted'")
print(sorted(plasser))

print ("\nHer er listen i orginal tilstand igjen")
print(plasser)
