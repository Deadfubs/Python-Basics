from collections import Counter

texto1 = 'Uma boneca que ganhou vida por magia, Gwen empunha as mesmas ferramentas que um dia a criaram. ' \
         'Valorizando todo instante, ' \
         'ela carrega a força do amor de sua criadora a cada passo e comanda a Névoa Sagrada,' \
         ' uma magia protetora ancestral que abençoou a tesoura, as agulhas e a linha de costura que ela usa. ' \
         'Tudo é novidade para Gwen, ' \
         'mas ela continua alegre e determinada a lutar pelo bem que ainda resta nesse mundo abatido.'

texto2 = 'Incomparável tanto por suas habilidades com armamentos incomuns quanto pelo seu sarcasmo mordaz, ' \
         'Jax é o último mestre de armas de Icathia conhecido. ' \
         'Depois de sua terra natal ter sido derrotada por sua própria arrogância ao libertar o Vazio, ' \
         'Jax e seu povo juraram proteger o pouco que restou.' \
         'Com a magia se espalhando pelo mundo, ' \
         'essa ameaça dormente acordou novamente e agora Jax vaga por Valoran carregando a última chama de Icathia ' \
         'e testando todo guerreiro encontrar para descobrir' \
         ' se algum deles é forte o suficiente para lutar ao seu lado...'

aparicoes = Counter(texto1.lower())
print(aparicoes)
print()

total = sum(aparicoes.values())
print(total)
print()

lista_frequencia = [(letra, round(frequencia/total*100, 2)) for letra, frequencia in aparicoes.items()]
proporcoes = dict(lista_frequencia)
print(proporcoes)
print()

proporcoes = Counter(proporcoes)

mais_comuns = proporcoes.most_common(10)

print('\n\n\n\Aplicando tudo:\n')
def analisa_frequencia_das_letras(texto):
    aparicoes = Counter(texto.lower())
    total = sum(aparicoes.values())
    proporcoes = [(letra, round(frequencia / total * 100, 2)) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print(f'{caractere} => {proporcao}%')

analisa_frequencia_das_letras(texto1)
print()

analisa_frequencia_das_letras(texto2)
print()
