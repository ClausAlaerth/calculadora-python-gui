import re

# Verificar se é número ou ponto
NUM_OR_DOT_REGEX = re.compile(r"^[0-9.]$")


# Verificar se é número ou ponto usando o REGEX acima
def isNumOrDot(string: str) -> bool:
    return bool(NUM_OR_DOT_REGEX.search(string))


# Verifica se o número inserido é válido,
# ignorando o input se não for
def isValidNumber(string: str):
    valid = False

    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid


# Converte os números flutuantes para inteiros, se possível.
def convertToInteger(string: str):
    number = float(string)

    if number.is_integer():
        number = int(number)

    return number

# OBS.: Não usado
# Invalida os espaços vazios na grid de botões


def isEmpty(string: str):
    return len(string) == 0
