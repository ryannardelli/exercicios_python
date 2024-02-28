import sys
def notas(*notas, sit=False):
    """
    notas(*notas, sit=False) 
    -> Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dicionario = {}
    lista_notas = []
    maior = media = 0
    menor = sys.maxsize
    for nota in notas:
        lista_notas.append(nota)
    dicionario['total'] = len(lista_notas)
    for nota in lista_notas:
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota
    dicionario['maior'] = maior
    dicionario['menor'] = menor
    media = sum(lista_notas) / len(lista_notas)
    dicionario['média'] = media
    if sit is True:
        if media >= 7:
            dicionario['situação'] = 'BOA'
        elif media >= 5:
            dicionario['situação'] = 'RAZOÁVEL'
        else:
            dicionario['situação'] = 'RUIM'
    return dicionario
print('-=' * 30)
resp = notas(3.5, 2, 6.5, 2, 7, 4)
help(notas)