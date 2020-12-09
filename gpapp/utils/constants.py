from stop_words import get_stop_words

STOP_WORDS = get_stop_words('french')
ADDITIONAL_STOP_WORDS = ["la", "dis", "", "ok", "quoi", "bonjour", "grandpy", "salut", "peux",
                         "dire", "où", "salut,", "salut",
                         "grandpy", "grandpy,",
                         "trouve"]
PUNCTUATION = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
               "[", "]", "{", "}", ";", ":", ",", ".", "/", "<",
               ">", "?", "|", "`", "~", "-", "=", "_", "+", "§"]

GRANDPY_FIRST_ANSWER = [
    "Bien sûr mon poussin ! Voici l'adresse :",
    "Avec plaisir ! Ca se trouve ici :",
    "Il me semble que l'adresse est celle-ci :"
]

GRANDPY_SECOND_ANSWER = [
    "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ?",
    "Le savais-tu ?",
    "Hmm.. Cela me rappelle quelque chose... Ah oui !"
]

GRANPY_WRONG_QUESTION = [
    "Désolé jeune homme, il semblerait que les mots que tu utilises "
    "ne me permettent pas de trouver de résultat. "
    "Peux-tu reformuler ta question ?",
    "Je ne suis un plus tout jeune tu sais, peux-tu reformuler "
    "ta question avec des mots plus clairs ?"
]

