colors = {'blue':'\x1b[34m', 'green':'\x1b[32m', 'red':'\x1b[31m', 'cyan':'\x1b[36m', 'normal':'\x1b[97m'}

def colored(text: str, color: str) -> str:
    return colors[color] + text