"""
ISBN : xxx-xxxxxxxxxx
"""

"""
Structure du donnée 1 :
    > Importance de la clé dans chaque isbn (authors, pages, year) : sinon on doit se rappeller de l'index
      de chaque élément
"""
books = {
    '456-7433679863': {
        'authors': ['Thomas Blanchy', 'Jean Luc'],
        'pages': 345,
        'year': 2008
    },
    '723-0987654823': {
        'authors': ['Michel Berger'],
        'pages': 23,
        'year': 1679
    },
    '654-5753579126': {
        'authors': ['Thomas Blanchy'],
        'pages': 567,
        'year': 2017
    }
}

"""

Structure de donnée 2 :
    > Dictionnaire composé de listes : tous les mêmes éléments (isbn)

"""
authors = {
    'Thomas Blanchy': [
        '456-7433679863',
        '654-5753579126'
    ],
    'Jean Luc': [
        '456-7433679863'
    ],
    'Michel Berger': [
        '723-0987654823'
    ]
}