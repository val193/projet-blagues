import pyjokes

def tell_joke(lang="en"):
    print(pyjokes.get_joke(language=lang))

if __name__ == "__main__":
    langue = input("Choisissez une langue (en, de, es, it, gr): ")
    tell_joke(lang)