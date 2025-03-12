import pyjokes

def tell_joke(lang="en", category="neutral"):
    print(pyjokes.get_joke(language=lang, category=category))

if __name__ == "__main__":
    langue = input("Choisissez une langue (en, de, es, it, fr) : ")
    categorie = input("Choisissez une catégorie de blague (neutral, chuck, all): ")
    tell_joke(langue, categorie)