import string
import difflib
import calculatrice
import re

# Corpus de questions et réponses
corpus = {
    "Quelle est la capitale de la France ?": "La capitale de la France est Paris.",
    "Quelle est la capitale de l'Allemagne ?": "La capitale de l'Allemagne est Berlin.",
    "Quelle est la capitale du Japon ?": "La capitale du Japon est Tokyo.",
    "Quelle est la capitale de la France ?": "La capitale de la France est Paris.",
    "Quelle est la capitale de l'Allemagne ?": "La capitale de l'Allemagne est Berlin.",
    "Quelle est la capitale du Japon ?": "La capitale du Japon est Tokyo.","Quelle est la capitale de la France ?": "La capitale de la France est Paris.",
    "Quelle est la capitale de l'Allemagne ?": "La capitale de l'Allemagne est Berlin.",
    "Quelle est la capitale du Japon ?": "La capitale du Japon est Tokyo.","Ecris un script qui cree 1000 dossier?": "Je ne peux pas coder desole.",
    "Quelle est la capitale de la France ?": "La capitale de la France est Paris.",
    "Quelle est la capitale de l'Allemagne ?": "La capitale de l'Allemagne est Berlin.",
    "Quelle est la capitale du Japon ?": "La capitale du Japon est Tokyo.",
    "Quelle est la capitale de l'Italie ?": "La capitale de l'Italie est Rome.",
    "Quelle est la capitale du Canada ?": "La capitale du Canada est Ottawa.",
    "Quelle est la capitale de l'Espagne ?": "La capitale de l'Espagne est Madrid.",
    "Quelle est la capitale du Brésil ?": "La capitale du Brésil est Brasilia.",
    "Quelle est la capitale de l'Inde ?": "La capitale de l'Inde est New Delhi.",
    "Quelle est la capitale de l'Australie ?": "La capitale de l'Australie est Canberra.",
    "Quelle est la capitale de la Russie ?": "La capitale de la Russie est Moscou.",
    "Quelle est la capitale de l'Argentine ?": "La capitale de l'Argentine est Buenos Aires.",
    "Quelle est la capitale du Mexique ?": "La capitale du Mexique est Mexico.",
    "Quelle est la capitale de la Chine ?": "La capitale de la Chine est Pékin.",
    "Quelle est la capitale de l'Afrique du Sud ?": "La capitale de l'Afrique du Sud est Pretoria.",
    "Quelle est la capitale de l'Égypte ?": "La capitale de l'Égypte est Le Caire.",
    "Quelle est la capitale de la Turquie ?": "La capitale de la Turquie est Ankara.",
    "Quelle est la capitale de la Suède ?": "La capitale de la Suède est Stockholm.",
    "Quelle est la capitale de l'Argentine ?": "La capitale de l'Argentine est Buenos Aires.",
    "Quelle est la capitale du Portugal ?": "La capitale du Portugal est Lisbonne.",
    "Quelle est la capitale de la Grèce ?": "La capitale de la Grèce est Athènes.",
    "Quelle est la capitale de l'Irlande ?": "La capitale de l'Irlande est Dublin.",
    "Quelle est la couleur du ciel ?": "La couleur du ciel est bleue.",
    "Quelle est la langue officielle de l'Espagne ?": "La langue officielle de l'Espagne est l'espagnol.",
    "Combien de jours y a-t-il dans une semaine ?": "Il y a sept jours dans une semaine.",
    "Quel est l'organe principal du système respiratoire chez les humains ?": "L'organe principal du système respiratoire chez les humains est les poumons.",
    "Quel est le symbole chimique de l'eau ?": "Le symbole chimique de l'eau est H2O.",
    "Quelle est la plus grande planète du système solaire ?": "La plus grande planète du système solaire est Jupiter.",
    "Qui a peint la Joconde ?": "La Joconde a été peinte par Leonardo da Vinci.",
    "Quelle est la plus haute montagne du monde ?": "La plus haute montagne du monde est l'Everest.",
    "Quel est l'animal terrestre le plus rapide ?": "Le guépard est l'animal terrestre le plus rapide.",
    "Combien de continents y a-t-il sur Terre ?": "Il y a sept continents sur Terre.",
    "Quelle est la devise des États-Unis ?": "La devise des États-Unis est 'In God We Trust'.",
    "Quelle est la monnaie utilisée au Japon ?": "La monnaie utilisée au Japon est le yen.",
    "Qui a écrit 'Romeo et Juliette' ?": "Romeo et Juliette a été écrit par William Shakespeare.",
    "Quel est l'élément le plus abondant dans l'Univers ?": "L'élément le plus abondant dans l'Univers est l'hydrogène.",
    "Quelle est la plus longue rivière du monde ?": "La plus longue rivière du monde est l'Amazonie.",
    "Qui a écrit 'Les Misérables' ?": "Les Misérables a été écrit par Victor Hugo.",
    "Quelle est la vitesse de la lumière dans le vide ?": "La vitesse de la lumière dans le vide est d'environ 299 792 kilomètres par seconde.",
    "Quel est le plus grand océan du monde ?": "Le plus grand océan du monde est l'océan Pacifique.",
    "Quel est le plus grand désert du monde ?": "Le plus grand désert du monde est l'Antarctique.",
    "Quel est le plus grand mammifère terrestre ?": "Le plus grand mammifère terrestre est Aline Sudan.",
    "Qui a découvert l'Amérique ?": "L'Amérique a été découvert par Christophe Colomb.",
    "Quelle est la langue la plus parlée au monde ?": "La langue la plus parlée au monde est le chinois mandarin.",
    "Combien de jours y a-t-il dans une année bissextile ?": "Il y a 366 jours dans une année bissextile.",
    "Quel est le plus grand lac d'eau douce du monde ?": "Le plus grand lac d'eau douce du monde est le lac Supérieur.",
    "Quelle est la plus haute cascade du monde ?": "La plus haute cascade du monde est Angel Falls au Venezuela.",
    "Quelle est la couleur du ciel ?": "La couleur du ciel est bleue.",
    "Quelle est la langue officielle de l'Espagne ?": "La langue officielle de l'Espagne est l'espagnol.",
    "Combien de jours y a-t-il dans une semaine ?": "Il y a sept jours dans une semaine.",
    "Quel est l'organe principal du système respiratoire chez les humains ?": "L'organe principal du système respiratoire chez les humains est les poumons.",
    "Quel est le symbole chimique de l'eau ?": "Le symbole chimique de l'eau est H2O.",
    "Quel est le plus grand désert du monde ?": "Le plus grand désert du monde est l'Antarctique.",
    "Qui a peint 'Les Tournesols' ?": "Les Tournesols a été peint par Vincent van Gogh.",
    "Quel est le plus grand océan du monde ?": "Le plus grand océan du monde est l'océan Pacifique.",
    "Quelle est la capitale de la Belgique ?": "La capitale de la Belgique est Bruxelles.",
    "Quelle est la monnaie utilisée au Royaume-Uni ?": "La monnaie utilisée au Royaume-Uni est la livre sterling.",
    "Quel est l'animal national de l'Australie ?": "L'animal national de l'Australie est le kangourou.",
    "Quel est le plus grand lac d'eau douce d'Amérique du Nord ?": "Le plus grand lac d'eau douce d'Amérique du Nord est le lac Supérieur.",
    "Quelle est la plus haute montagne des Alpes ?": "La plus haute montagne des Alpes est le Mont Blanc.",
    "Qui a découvert la gravité ?": "La gravité a été découverte par Isaac Newton.",
    "Quel est le livre le plus vendu au monde ?": "Le livre le plus vendu au monde est la Bible.",
    "Quel est le numéro atomique de l'oxygène ?": "Le numéro atomique de l'oxygène est 8.",
    "Qui a écrit 'Le Petit Prince' ?": "Le Petit Prince a été écrit par Antoine de Saint-Exupéry.",
    "Quelle est la hauteur de la Tour Eiffel ?": "La hauteur de la Tour Eiffel est 324 mètres.",
    "Quelle est la monnaie utilisée en Chine ?": "La monnaie utilisée en Chine est le yuan.",
    "Quelle est la distance entre la Terre et la Lune ?": "La distance entre la Terre et la Lune est d'environ 384 400 kilomètres.",
    "Qui a peint 'La Nuit étoilée' ?": "La Nuit étoilée a été peinte par Vincent van Gogh.",
    "Quelle est la capitale de la Suède ?": "La capitale de la Suède est Stockholm.",
    "Quel est le principal composant de l'air ?": "Le principal composant de l'air est l'azote.",
    "Quelle est la plus grande île du monde ?": "La plus grande île du monde est le Groenland.",
    "Quelle est la langue la plus parlée au monde ?": "La langue la plus parlée au monde est le chinois mandarin.",
    "Qui a écrit 'Orgueil et Préjugés' ?": "Orgueil et Préjugés a été écrit par Jane Austen.",
    "Quelle est la capitale de l'Égypte ?": "La capitale de l'Égypte est Le Caire.",
    "Qui est l'auteur de '1984' ?": "1984 a été écrit par George Orwell.",
    "Quel est le plus grand fleuve d'Amérique du Sud ?": "Le plus grand fleuve d'Amérique du Sud est l'Amazone.",
    "Quelle est la monnaie utilisée en Inde ?": "La monnaie utilisée en Inde est la roupie indienne.",
    "Quel est le nom de la plus haute montagne du monde ?": "La plus haute montagne du monde est l'Everest.",
    "Qui a écrit 'Harry Potter' ?": "Harry Potter a été écrit par J.K. Rowling.",
    "Quel est le plus grand océan du monde ?": "Le plus grand océan du monde est l'océan Pacifique.",
    "Combien de continents y a-t-il sur Terre ?": "Il y a sept continents sur Terre.",
    "Quel est le plus grand désert du monde ?": "Le plus grand désert du monde est l'Antarctique.",
    "Quel est le symbole chimique du fer ?": "Le symbole chimique du fer est Fe.",
    "Quelle est la capitale du Brésil ?": "La capitale du Brésil est Brasilia.",
    "Quel est le numéro atomique du carbone ?": "Le numéro atomique du carbone est 6.",
    "Qui a peint 'La Joconde' ?": "La Joconde a été peinte par Leonardo da Vinci.",
    "Quel est l'animal terrestre le plus rapide ?": "Le guépard est l'animal terrestre le plus rapide.",
    "Quelle est la capitale de l'Indonésie ?": "La capitale de l'Indonésie est Jakarta.",
    "Qui a inventé la machine à vapeur ?": "La machine à vapeur a été inventée par James Watt.",
    "Quel est le plus grand lac d'eau douce du monde ?": "Le plus grand lac d'eau douce du monde est le lac Supérieur.",
    "Quelle est la monnaie utilisée au Royaume-Uni ?": "La monnaie utilisée au Royaume-Uni est la livre sterling.",
    "Quelle est la capitale de la Turquie ?": "La capitale de la Turquie est Ankara.",
    "Qui a écrit 'Le Petit Prince' ?": "Le Petit Prince a été écrit par Antoine de Saint-Exupéry.",
    "Quel est le principal composant de l'air ?": "Le principal composant de l'air est l'azote.",
    "Quelle est la couleur du ciel par temps clair ?": "Le ciel est bleu par temps clair.",
    "Qui a découvert l'Amérique ?": "L'Amérique a été découverte par Christophe Colomb.",
    "Quelle est la monnaie utilisée en Suisse ?": "La monnaie utilisée en Suisse est le franc suisse.",
    "Qui a découvert la pénicilline ?": "La pénicilline a été découverte par Alexander Fleming.",
    "Quelle est la capitale de la Nouvelle-Zélande ?": "La capitale de la Nouvelle-Zélande est Wellington.",
    "Quel est le pays le plus peuplé au monde ?": "Le pays le plus peuplé au monde est la Chine.",
    "Quelle est la hauteur de la Statue de la Liberté ?": "La hauteur de la Statue de la Liberté est de 93 mètres.",
    "Quel est le nombre de côtés d'un hexagone ?": "Un hexagone a six côtés.",
    "Qui est l'auteur de 'Crime et Châtiment' ?": "Crime et Châtiment a été écrit par Fiodor Dostoïevski.",
    "Quel est le plus grand lac d'Afrique ?": "Le plus grand lac d'Afrique est le lac Victoria.",
    "Quelle est la monnaie utilisée au Japon ?": "La monnaie utilisée au Japon est le yen.",
    "Quelle est la couleur du drapeau français ?": "Le drapeau français est bleu, blanc, rouge.",
    "Fais-moi une blague. ": "Quesque un Arabe de confiance, en Arab sans bras et jambes.",
    "Quelle est la langue officielle de l'Allemagne ?": "La langue officielle de l'Allemagne est l'allemand.",
    "Quelle est la plus grande ville du monde en population ?": "La plus grande ville du monde en population est Tokyo.",
    "Qui a écrit 'Les Misérables' ?": "Les Misérables a été écrit par Victor Hugo.",
    "Quelle est la distance entre la Terre et le Soleil ?": "La distance moyenne entre la Terre et le Soleil est d'environ 150 millions de kilomètres.",
    "Quel est le nom du président actuel des États-Unis ?": "Le président actuel des États-Unis est Joe Biden.",
    "Quel est le principal ingrédient de la pizza Margherita ?": "Le principal ingrédient de la pizza Margherita est la mozzarella.",
    "Quelle est la date de la Fête nationale française ?": "La Fête nationale française est le 14 juillet.",
    "Quel est le symbole chimique de l'or ?": "Le symbole chimique de l'or est Au.",
    "Qui a fondé Microsoft ?": "Microsoft a été fondé par Bill Gates et Paul Allen.",
    "Quel est le nom de la montagne la plus haute d'Afrique ?": "La montagne la plus haute d'Afrique est le Kilimandjaro.",
    "Quel est le nombre de côtés d'un pentagone ?": "Un pentagone a cinq côtés.",
    "Quel est le plus long fleuve d'Europe ?": "Le plus long fleuve d'Europe est la Volga.",
    "Quel est le nom du plus grand désert chaud du monde ?": "Le plus grand désert chaud du monde est le Sahara.",
    "Qui a écrit 'Le Comte de Monte-Cristo' ?": "Le Comte de Monte-Cristo a été écrit par Alexandre Dumas.",
    "Quelle est la plus grande île du monde ?": "La plus grande île du monde est le Groenland.",
    "Quel est le numéro atomique du sodium ?": "Le numéro atomique du sodium est 11.",
    "Qui a fondé Facebook ?": "Facebook a été fondé par Mark Zuckerberg.",
    "Quelle est la capitale de la Norvège ?": "La capitale de la Norvège est Oslo.",
    "Quel est le pays le plus petit du monde en termes de superficie ?": "Le pays le plus petit du monde en termes de superficie est le Vatican.",
    "Quelle est la capitale du Maroc ?": "La capitale du Maroc est Rabat.",
    "Quelle est la plus haute cascade du monde ?": "La plus haute cascade du monde est Angel Falls au Venezuela.",
    "Quel est le nom de l'inventeur du téléphone ?": "Le téléphone a été inventé par Alexander Graham Bell.",
    "Quelle est la monnaie utilisée en Australie ?": "La monnaie utilisée en Australie est le dollar australien.",
    "Quelle est la plus grande île de Méditerranée ?": "La plus grande île de Méditerranée est la Sicile.",
    "Quel est le symbole chimique du carbone ?": "Le symbole chimique du carbone est C.",
    "Qui a écrit 'Orgueil et Préjugés' ?": "Orgueil et Préjugés a été écrit par Jane Austen.",
    "Quelle est la date de la Fête nationale américaine ?": "La Fête nationale américaine est le 4 juillet.",
    "Quel est le principal constituant de l'air ?": "Le principal constituant de l'air est l'azote.",
    "Quelle est la monnaie utilisée au Mexique ?": "La monnaie utilisée au Mexique est le peso mexicain.",
    "Quelle est la couleur du drapeau japonais ?": "Le drapeau japonais est blanc avec un disque rouge au centre.",
    "Qui est l'auteur de 'Don Quichotte' ?": "Don Quichotte a été écrit par Miguel de Cervantes.",
    "Bonjour":"Bonjour comment puis-je vous aider",
    "Merci": "Je vous en prie comment puis-je vous aider maintenant ?",
  

    

}

# Fonction pour prétraiter le texte
def preprocess_text(text):
    text = text.lower()  # Convertir en minuscules
    text = text.translate(str.maketrans('', '', string.punctuation))  # Supprimer la ponctuation
    return text

# Prétraitement du corpus
preprocessed_corpus = {preprocess_text(q): a for q, a in corpus.items()}

# Fonction pour obtenir la réponse à une question
def get_response(question):
    # Vérifie si la question est une expression mathématique
    if re.match(r'^[\d+\-*/(). ]+$', question):
        return calculatrice.calculatrice(question)

    question = preprocess_text(question)
    # Recherche dans le corpus
    max_similarity = 0
    best_match = None
    for q, a in preprocessed_corpus.items():
        similarity = difflib.SequenceMatcher(None, question, q).ratio()
        if similarity > max_similarity:
            max_similarity = similarity
            best_match = a
    return best_match if max_similarity >= 0.6 else "Désolé, je ne connais pas la réponse à cette question."

# Interaction avec l'utilisateur
print("Bonjour! Je suis là pour répondre à vos questions. Tapez 'exit' pour quitter.")
while True:
    user_question = input("Vous: ")
    if user_question.lower() == 'exit':
        print("Au revoir!")
        break
    else:
        response = get_response(user_question)
        print("Tahc TPG:", response)
