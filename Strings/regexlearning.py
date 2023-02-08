import re  # Regular Expression -- RegEx

endereco = "Rua das Flores 72, apartamento 1002, laranjeiras, Rio de Janeiro, RJ, 23440-120"

padrao = re.compile("[0-9]{5}-?[0-9]{3}")
busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)
