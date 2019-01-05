# https://www.myefrei.fr/moodle/pluginfile.php/100234/mod_resource/content/1/Labyrinth%20project.pdf

def generate():
#   Tout notre cycle de génération de la matrice se situe ici.
    width = int(input("How many cells in width? "))
    height = int(input("How many cells in height? "))
    n = 0
    liste = [i for i in range(n)]

    print([-1 for i in range (height + 1)])

    x = 0

    while x < width:
        x += 1
        print([-1 for i in range (height + 1)])

generate()
