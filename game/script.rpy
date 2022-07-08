# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define mc = Character('MC', color="#c8ffc8")


# Le jeu commence ici
label start:
    scene landscape01
    show girl normal
    mc "Vous venez de créer un nouveau jeu Ren'Py."
    show girl happy at right
    mc "Après avoir ajouté une histoire, des images et de la musique, vous pourrez le présenter au monde entier !"
    scene underthesea01 with dissolve
    show girl inquiete at left
    "test push 2"
    "test Atma"
    "test 2"
    "test dragons"

    return
