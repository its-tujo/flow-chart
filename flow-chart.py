import graphviz
import uuid
name = "Zuckerschnecke"

id = name + "-"+ str(uuid.uuid4())


# CHANGE !Nodes! and !edges! to your needs
nodes = [
    ("Start", "Anruf erhalten (Z. 1-5)"),
    ("Anruf", "Treffen vereinbart (Z. 5-12)"),
    ("Treffen", "Erstes Treffen im Café und Kino (Z. 12-20)"),
    ("Kennenlernen", "Weitere Treffen, sie lernen sich kennen (Z. 20-25)"),
    ("Distanz", "Frage nach Geld bleibt unbeantwortet (Z. 25-32)"),
    ("Selbstständigkeit", "Ich-Erzählerin sorgt selbst für sich (Z. 32-36)"),
    ("Krankheit", "Vater ist krank, Treffen im Krankenhaus (Z. 37-45)"),
    ("Bitte", "Bitte um Morphium, sie zögert (Z. 45-52)"),
    ("Tod", "Vater stirbt, Streuselschnecken gebacken (Z. 52-60)"),
    ("Beerdigung", "Beerdigung ohne Mutter (Z. 60-65)")
]

edges = [
    ("Start", "Anruf"),
    ("Anruf", "Treffen"),
    ("Treffen", "Kennenlernen"),
    ("Kennenlernen", "Distanz"),
    ("Distanz", "Selbstständigkeit"),
    ("Selbstständigkeit", "Krankheit"),
    ("Krankheit", "Bitte"),
    ("Bitte", "Tod"),
    ("Tod", "Beerdigung")
]


dot = graphviz.Digraph(format="png")


for node_id, label in nodes:
    dot.node(node_id, label)


for start, end in edges:
    dot.edge(start, end)


diagram_path = 'PATH(CHANGE THIS !!)' + id
diagram_path = dot.render(filename=diagram_path)

print(f"Flow chart saved as: {id}.png")



print(f"Endgültiger Pfad: {diagram_path}")
