from decimal import *

def calculo_da_qtdd_tinta():

    print('Esse software determina quantas latas de tinta voc� precisar� usar para pintar a sua parede e qual ser� o custo final**')

    tamanho_parede = int(input('Informe qual � a area da parede a ser pintada, em m2: '))

    def qtdd_tinta():
        qttd_tinta = round(tamanho_parede / 3, 1)
        return qttd_tinta

    def qtdd_latas():
        qtdd_latas = round(qtdd_tinta() / 18 + 1)
        return qtdd_latas

    def plural_latas():
        if qtdd_latas() > 1:
            return 'latas'
        else: return 'lata'

    def plural_galoes():
        if qtdd_galoes() > 1:
            return 'gal�es'
        else: return 'gal�o'        

    def qtdd_galoes():
        qtdd_galoes = round(qtdd_tinta() / 3.6 + 0.5)
        return qtdd_galoes

    def orcamento():
        custo = qtdd_latas() * 80
        return custo

    def retorno_user():
        print (f'A sua parede de tamanho {tamanho_parede}m2 necessitar� de {qtdd_tinta()} litros de tinta. Voc� precisa, portanto, adquirir {qtdd_latas()} {plural_latas()} de tinta ou, se preferir, {qtdd_galoes()}{plural_galoes()}. Voc� ir� gastar R$ {orcamento()} reais, em nossa loja')

    retorno_user()
        
calculo_da_qtdd_tinta()