# Fairfe une fonction qui supprime un caractère dans un fichier

def del_charactere(path, char):

    with open(path, 'r') as file:
        content = file.read()

    updated_content = content.replace(char, '')

    with open(path, 'w') as file:
        file.write(updated_content)

    print(f"Le caractère {char} a été supprimé du fichier: {path} .")

    return updated_content

print(del_charactere(r'C:\Users\kurdtkobane\Desktop\hello_world.txt', 'z'))