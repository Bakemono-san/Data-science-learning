from transformers import pipeline

classifier = pipeline("zero-shot-classification")

res = classifier("Qui peut créer un GIE ",candidate_labels=["Devenir volontaire du Service civique national","Demander une autorisation de démolir","Demander une carte d'import-export","Demander une assistance à la création d'un groupement d’intérêt économique (GIE)"])