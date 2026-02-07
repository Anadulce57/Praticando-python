def formular_p(o_text):
    if o_text ==  " ":
        return 0
    o_text = o_text.lower()

    new_string = "".join(o_text.split())[::-1]

    return new_string

text = input("Digite o seu texto: ")
c_text = text.lower()
c_text = "".join(c_text.split())

if c_text == formular_p(c_text):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")