# ATIVIDADE PRÁTICA SUPERVISIONADAS (APS)

# Funções por tipos de materiais

# Plasticos
def MaterialEscolhidoPlastico(z):
    x = z
    if x >= -291 and x <= -150:
        print('', ['sacola de supermercado, saco de lixo, embalagem de leite', 'Tipo de plastico: PEBD (Polietileno de Baixa Densidade)',
        ' Ponto de coleta: Rua Serra Dourada 165, Campinas, SP, 13100-312'], '\n',
        ['Garrafa de alvejante, Garrafa detergente, frascos shampoo,', 'Tipo: plasticos: PEAD (Polietileno de Alta Densidade)',
         'ponto de coleta:  Rua Celso soares Couto s/n°, Pq. Itajaí'])
        return x
    elif x >= -149 and x <= -100:
        print('',['Garrafas Pet', 'embalagem de cosméticos', 'Tipo de plastico: PET (Tereftalato de Polietileno)', 'Local de coleta: Av. São José dos campos s/ n°, Vl Campos Sales' ], '\n',
        ['pote de sorvete, partes internas de geladeira, brinquedo lego', 'Tipo plastico: PS (Poliestireno)',
        'Local de coleta: Rua josé martins lourenço, esq. com Rua Geraldo Bretas, jd. São Gabriel'])
        return x

    elif x > -100 and x <= 0:
        print('',['Pote de sorvete', 'Tipo plastico: PP (Polipropileno)', 'Av. Marechal Rondon, esq. com Rua José Manuel Veiga, Jd. Eulina'], '\n',
        ['PVC', 'Tipo de platico: PVC (Policloreto de Vinila)', 'Ponto de coleta: Rua Manoel Gomes Ferreira, esq. com Rua José Ramos Catarino'])
        return x
    elif x > 0 and x <= 90:
        print('',['pote de sorvete, partes internas de geladeira, brinquedo lego', 'Tipo plastico: PS (Poliestireno)',
        'Local de coleta: Rua josé martins lourenço, esq. com Rua Geraldo Bretas, jd. São Gabriel'], '\n',
        ['Garrafas Pet', 'embalagem de cosméticos', 'Tipo de plastico: PET (Tereftalato de Polietileno)', 'Local de coleta: Av. São José dos campos s/ n°, Vl Campos Sales' ])
        return x
    elif x > 90 and x <= 149:
        print('',['pote de sorvete, partes internas de geladeira, brinquedo lego', 'Tipo plastico: PS (Poliestireno)',
        'Local de coleta: Rua josé martins lourenço, esq. com Rua Geraldo Bretas, jd. São Gabriel'], '\n',
        ['PVC', 'Tipo de platico: PVC (Policloreto de Vinila)',
       'Ponto de coleta: Rua Manoel Gomes Ferreira, esq. com Rua José Ramos Catarino'] )
        return x
    elif x > 149 and x <= 210:
        print(['sacola de supermercado, saco de lixo, embalagem de leite', 'Tipo de plastico: PEBD (Polietileno de Baixa Densidade)',
                   ' Ponto de coleta: Rua Serra Dourada 165, Campinas, SP, 13100-312'], '\n',
              ['PVC', 'Tipo de platico: PVC (Policloreto de Vinila)', 'Ponto de coleta: Rua Manoel Gomes Ferreira, esq. com Rua José Ramos Catarino'], '\n',
              ['Garrafas Pet', 'embalagem de cosméticos', 'Tipo de plastico: PET (Tereftalato de Polietileno)', 'Local de coleta: Av. São José dos campos s/ n°, Vl Campos Sales' ])
        return x
    elif x > 210 and x <= 280:
        print('',['Garrafa de alvejante, Garrafa detergente, frascos shampoo,', 'Tipo: plasticos: PEAD (Polietileno de Alta Densidade)',
         'ponto de coleta:  Rua Celso soares Couto s/n°, Pq. Itajaí'], '\n',
        ['sacola de supermercado, saco de lixo, embalagem de leite', 'Tipo de plastico: PEBD (Polietileno de Baixa Densidade)',
        ' Ponto de coleta: Rua Serra Dourada 165, Campinas, SP, 13100-312'])

# Vidro
def MaterialEscolhidoVidro(z):
    x = z
    if x >= -291 and x <= -120:
        print('', ['temperado, laminado, duplo', 'Ponto de coleta proximo: Ponto verde - Vila Costa e Silva Rua Saldanha da Gama, 77 Ecoponto'], '\n',
    ['Termoendurecido, Lacado, Controle Acústico, Controle Solar', 'Pontos de coleta proximo: Ponto verde - Vila Costa e Silva Rua Saldanha da Gama, 77 Ecoponto']),
        return x
    elif x > -120 and x <= -90:
        print('',['Vidros especiais: Corta fogo, Auto limpeza, Anti-Bala / Blindado','Ponto de coleta proximo: ',
               ' Ponto Verde Av. Santa Isabel, 2300, Ecoponto Jardim EulinaAv. Mal. Rondon'])
        return x
    elif x > -90 and x <= -20:
        print('',['temperado, laminado, duplo', 'Ponto de coleta proximo: Ponto verde - Vila Costa e Silva Rua Saldanha da Gama, 77 Ecoponto'], '\n' ,
        ['Vidros especiais: Vidro para Pavimentos, Decorativo / Vidro Texturado, espelho',
         'Ponto de coleta proximo: Ponto-Verde Av. Santa Isabel, 2300 Ecoponto Jardim Eulina Av. Mal. Rondon'])
        return x
    elif x > -20 and x <= 50:
        print('',['temperado, laminado, duplo', 'Ponto de coleta proximo: Ponto verde - Vila Costa e Silva Rua Saldanha da Gama, 77 Ecoponto'])
        return x
    elif x > 50 and x <= 100:
        print('',['Termoendurecido, Lacado, Controle Acústico, Controle Solar', 'Pontos de coleta proximo: Ponto verde - Vila Costa e Silva Rua Saldanha da Gama, 77 Ecoponto'], '\n',
        ['Vidros especiais: Vidro para Pavimentos, Decorativo / Vidro Texturado, espelho'
         'Ponto de coleta proximo: Ponto-Verde Av. Santa Isabel, 2300 Ecoponto Jardim Eulina Av. Mal. Rondon'])
        return x
    elif x > 100 and x <= 150:
        print('',['Vidros especiais: Corta fogo, Auto limpeza, Anti-Bala / Blindado','Ponto de coleta proximo: ',
               ' Ponto Verde Av. Santa Isabel, 2300, Ecoponto Jardim EulinaAv. Mal. Rondon'])
        return x
    elif x > 151 and x <= 219:
        print('', ['Vidros especiais: Corta fogo, Auto limpeza, Anti-Bala / Blindado','Ponto de coleta proximo: ',
        ' Ponto Verde Av. Santa Isabel, 2300, Ecoponto Jardim EulinaAv. Mal. Rondon'], '\n',
        ['Termoendurecido, Lacado, Controle Acústico, Controle Solar',
       'Pontos de coleta proximo: Ponto verde - Vila Costa e Silva Rua Saldanha da Gama, 77 Ecoponto'])
        return x
    elif x > 219 and x <= 280:
        print('',['Vidros especiais: Corta fogo, Auto limpeza, Anti-Bala / Blindado','Ponto de coleta proximo: ',
        ' Ponto Verde Av. Santa Isabel, 2300, Ecoponto Jardim EulinaAv. Mal. Rondon'], '\n',
        ['temperado, laminado, duplo', 'Ponto de coleta proximo: Ponto verde - Vila Costa e Silva Rua Saldanha da Gama, 77 Ecoponto'])
        return x

#Papel
def MaterialEscolhidoPapel(z):
    x = z
    if  x >= -291 and x <= -120:
        print('', ['lista telefonica, jornal, revista', 'tipo: papel imprensa',
        'Ponto de coleta: (Papeis zambelli)R Leonor Ponessi Cappelli, 210, Parque Rural Fazenda Santa Cândida - Campinas, SP'], '\n',
        ['A4, A3, A2, A1', 'Tipo: papel para imprimir',
        'Ponto de coleta: (comercio de sucatas rodrigues) R Itacuruçá, 480 - Jardim Aeroporto de Viracopos - Campinas, SP - CEP: 13056-094'])
    elif x > -120 and x <= -90:
        print('',['Papelão', 'Tipo: papel ondulado',
            'Ponto de coleta: (Marapara maravalhas aparas de papel papelão e sucatas) R São José do Rio Preto, 1101 - Jardim Nova Europa - Campinas, SP - CEP: 13040-060'], ' \n',
        ['embalagens de alimentos e remedios', 'tipo: papel cartão', 'Ponto de coleta: (Latem) Av. Orozimbo Maia, 2062 - Cambuí - Campinas, SP - CEP: 13024-045'], '\n',
        ['pepel higienico, papel toalha, guarda napos', 'Tipo: papel sanitário', 'Ponto de coleta: ops: esse tipo de papel não pode ser reciclado ;-)'])
        return x
    elif x > -90 and x <= 0:
        print('',['A4, A3, A2, A1', 'Tipo: papel para imprimir',
        'Ponto de coleta: (comercio de sucatas rodrigues) R Itacuruçá, 480 - Jardim Aeroporto de Viracopos - Campinas, SP - CEP: 13056-094'], '\n',
        ['embalagens de alimentos e remedios', 'tipo: papel cartão', 'Ponto de coleta: (Latem) Av. Orozimbo Maia, 2062 - Cambuí - Campinas, SP - CEP: 13024-045'])
        return x
    elif x > 0 and x <= 60:
        print('',['Papelão', 'Tipo: papel ondulado',
        'Ponto de coleta: (Marapara maravalhas aparas de papel papelão e sucatas) R São José do Rio Preto, 1101 - Jardim Nova Europa - Campinas, SP - CEP: 13040-060'], '\n',
        ['lista telefonica, jornal, revista', 'tipo: papel imprensa',
        'Ponto de coleta: (Papeis zambelli)R Leonor Ponessi Cappelli, 210, Parque Rural Fazenda Santa Cândida - Campinas, SP'])
        return x

    elif x > 60 and x <= 110:
        print('',['Papelão', 'Tipo: papel ondulado',
            'Ponto de coleta: (Marapara maravalhas aparas de papel papelão e sucatas) R São José do Rio Preto, 1101 - Jardim Nova Europa - Campinas, SP - CEP: 13040-060'], '\n',
            ['lista telefonica, jornal, revista', 'tipo: papel imprensa',
            'Ponto de coleta: (Papeis zambelli)R Leonor Ponessi Cappelli, 210, Parque Rural Fazenda Santa Cândida - Campinas, SP'], '\n',
            ['A4, A3, A2, A1', 'Tipo: papel para imprimir',
            'Ponto de coleta: (comercio de sucatas rodrigues) R Itacuruçá, 480 - Jardim Aeroporto de Viracopos - Campinas, SP - CEP: 13056-094'])
        return x
    elif x > 110 and x <= 170:
        print('',['lista telefonica, jornal, revista', 'tipo: papel imprensa',
            'Ponto de coleta: (Papeis zambelli)R Leonor Ponessi Cappelli, 210, Parque Rural Fazenda Santa Cândida - Campinas, SP'], '\n',
            ['embalagens de alimentos e remedios', 'tipo: papel cartão', 'Ponto de coleta: (Latem) Av. Orozimbo Maia, 2062 - Cambuí - Campinas, SP - CEP: 13024-045'])
        return x
    elif x > 170 and x <= 220:
        print('',['embalagens de alimentos e remedios', 'tipo: papel cartão', 'Ponto de coleta: (Latem) Av. Orozimbo Maia, 2062 - Cambuí - Campinas, SP - CEP: 13024-045'], '\n',
            ['A4, A3, A2, A1', 'Tipo: papel para imprimir',
            'Ponto de coleta: (comercio de sucatas rodrigues) R Itacuruçá, 480 - Jardim Aeroporto de Viracopos - Campinas, SP - CEP: 13056-094'])
        return x
    elif x > 220 and x <= 280:
        print('',['lista telefonica, jornal, revista', 'tipo: papel imprensa',
            'Ponto de coleta: (Papeis zambelli)R Leonor Ponessi Cappelli, 210, Parque Rural Fazenda Santa Cândida - Campinas, SP'], '\n',
            ['embalagens de alimentos e remedios', 'tipo: papel cartão', 'Ponto de coleta: (Latem) Av. Orozimbo Maia, 2062 - Cambuí - Campinas, SP - CEP: 13024-045'], '\n',
            ['Papelão', 'Tipo: papel ondulado',
            'Ponto de coleta: (Marapara maravalhas aparas de papel papelão e sucatas) R São José do Rio Preto, 1101 - Jardim Nova Europa - Campinas, SP - CEP: 13040-060'])
        return x

#Metal
def MaterialEscolhidoMetal(z):
    x = z
    if x > -291 and x <= -200:
        print('', ['ferro, aço', 'Tipo: ferroso. Ponto de coleta: Ferro Velho Roberto, Compra E Venda De Sucatas: R. Marquês de Abrantes, 600 - Jardim Santa Genebra, Campinas - SP, 13080-220'], '\n',
        ['alumínio, cobre', 'tipo: não ferroso. Ponto de coleta: FERRO VELHO CLEBER: R. Pref. Celso Daniel, 161 - Vila San Martin, Campinas - SP, 13069-079 '], '\n',
        ['chumbo, níquel, mercúrio',
         'tipo: metal pesado. Ponto de coleta: Sucatas e Metais 2 Irmãos | Ferro Velho em Campinas | Sucatas em Campinas: R. Guaiçara, 354 - Jardim Itatinga, Campinas - SP, 13052-442 '])
        return x
    elif x > -200 and x <= -160:
        print('não tem metal reciclável proximo')
        return x
    elif x > -160 and x <= -110:
        print('',['alumínio, cobre', 'tipo: não ferroso. Ponto de coleta: FERRO VELHO CLEBER: R. Pref. Celso Daniel, 161 - Vila San Martin, Campinas - SP, 13069-079 '])
        return x
    elif x > -110 and x <= -60:
        print('',['chumbo, níquel, mercúrio',
        'tipo: metal pesado. Ponto de coleta: Sucatas e Metais 2 Irmãos | Ferro Velho em Campinas | Sucatas em Campinas: R. Guaiçara, 354 - Jardim Itatinga, Campinas - SP, 13052-442 '], '\n',
        ['ferro, aço',
        'Tipo: ferroso. Ponto de coleta: Ferro Velho Roberto, Compra E Venda De Sucatas: R. Marquês de Abrantes, 600 - Jardim Santa Genebra, Campinas - SP, 13080-220'])
        return x
    elif x > -60 and x <= 0:
        print('',['chumbo, níquel, mercúrio',
        'tipo: metal pesado. Ponto de coleta: Sucatas e Metais 2 Irmãos | Ferro Velho em Campinas | Sucatas em Campinas: R. Guaiçara, 354 - Jardim Itatinga, Campinas - SP, 13052-442 '])
        return x
    elif x > 0 and x <= 60:
        print('',['ferro, aço',
        'Tipo: ferroso. Ponto de coleta: Ferro Velho Roberto, Compra E Venda De Sucatas: R. Marquês de Abrantes, 600 - Jardim Santa Genebra, Campinas - SP, 13080-220'], '\n',
        ['chumbo, níquel, mercúrio',
        'tipo: metal pesado. Ponto de coleta: Sucatas e Metais 2 Irmãos | Ferro Velho em Campinas | Sucatas em Campinas: R. Guaiçara, 354 - Jardim Itatinga, Campinas - SP, 13052-442 '])
        return x
    elif x > 60 and x <= 110:
        print('',['ferro, aço',
        'Tipo: ferroso. Ponto de coleta: Ferro Velho Roberto, Compra E Venda De Sucatas: R. Marquês de Abrantes, 600 - Jardim Santa Genebra, Campinas - SP, 13080-220'])
        return x
    elif x > 110 and x <= 170:
        print('',['alumínio, cobre', 'tipo: não ferroso. Ponto de coleta: FERRO VELHO CLEBER: R. Pref. Celso Daniel, 161 - Vila San Martin, Campinas - SP, 13069-079 '],'\n',
        ['ferro, aço',
        'Tipo: ferroso. Ponto de coleta: Ferro Velho Roberto, Compra E Venda De Sucatas: R. Marquês de Abrantes, 600 - Jardim Santa Genebra, Campinas - SP, 13080-220'])
    elif x > 170 and x <= 220:
        print('',['alumínio, cobre', 'tipo: não ferroso. Ponto de coleta: FERRO VELHO CLEBER: R. Pref. Celso Daniel, 161 - Vila San Martin, Campinas - SP, 13069-079 '], '\n',
        ['ferro, aço',
        'Tipo: ferroso. Ponto de coleta: Ferro Velho Roberto, Compra E Venda De Sucatas: R. Marquês de Abrantes, 600 - Jardim Santa Genebra, Campinas - SP, 13080-220'])
    elif x > 220 and x <= 280:
        print('não tem metal reciclável proximo')
        return x

#Eletrônicos
def MaterialEscolhidoEletro(z):
    x = z
    if x > -291 and x <= -200:
        print('',['Computador, televisor, monitor, notebook, celular, tablet',
        'Ponto de coleta: (Reversis - Reciclagem de Eletrônicos e Informática) fica na R. da Abolição, 1900 - Pte. Preta, Campinas - SP, 13041-445'], '\n',
        ['telefones, impressora, vídeo, cassete, aparelho DVD', '(Ecoponto / Ponto Verde) fica na Av. Santa Isabel, 2300 - Barão Geraldo, Campinas -SP, 13084-012'])
        return x
    elif x > -200 and x <= -130:
        print('',['microondas, modem, caixa de som',
        'Ponto de coleta: (Reversis - Reciclagem de Eletrônicos e Informática) fica na R. da Abolição, 1900 - Pte. Preta, Campinas - SP, 13041-445'], '\n',
        ['no Break, estabilizador, cabos de energia', 'Ponto de coleta: (GMV Recycle) fica na Rod. Lix da Cunha, 911 - Jardim do Lago II, Campinas - SP, 13051-051'])
        return x
    elif x > -130 and x <= -85:
        print(['telefones, impressora, vídeo, cassete, aparelho DVD', '(Ecoponto / Ponto Verde) fica na Av. Santa Isabel, 2300 - Barão Geraldo, Campinas -SP, 13084-012'], '\n',
        ['microondas, modem, caixa de som',
        'Ponto de coleta: (Reversis - Reciclagem de Eletrônicos e Informática) fica na R. da Abolição, 1900 - Pte. Preta, Campinas - SP, 13041-445'])
        return x
    elif x > -85 and x <= -20:
        print(['telefones, impressora, vídeo, cassete, aparelho DVD', '(Ecoponto / Ponto Verde) fica na Av. Santa Isabel, 2300 - Barão Geraldo, Campinas -SP, 13084-012'], '\n',
        ['no Break, estabilizador, cabos de energia', 'Ponto de coleta: (GMV Recycle) fica na Rod. Lix da Cunha, 911 - Jardim do Lago II, Campinas - SP, 13051-051'])
    elif x > -20 and x <= 20:
        print('não tem lixo eletrônico ao redor')
        return x
    elif x > 20 and x <= 80:
        print(['microondas, modem, caixa de som',
        'Ponto de coleta: (Reversis - Reciclagem de Eletrônicos e Informática) fica na R. da Abolição, 1900 - Pte. Preta, Campinas - SP, 13041-445'], '\n',
        ['Computador, televisor, monitor, notebook, celular, tablet',
        'Ponto de coleta: (Reversis - Reciclagem de Eletrônicos e Informática) fica na R. da Abolição, 1900 - Pte. Preta, Campinas - SP, 13041-445'])
        return x
    elif x > 80 and x <= 130:
        print(['Computador, televisor, monitor, notebook, celular, tablet',
        'Ponto de coleta: (Reversis - Reciclagem de Eletrônicos e Informática) fica na R. da Abolição, 1900 - Pte. Preta, Campinas - SP, 13041-445'], '\n',
        ['telefones, impressora, vídeo, cassete, aparelho DVD', '(Ecoponto / Ponto Verde) fica na Av. Santa Isabel, 2300 - Barão Geraldo, Campinas -SP, 13084-012'], '\n',
        ['microondas, modem, caixa de som',
        'Ponto de coleta: (Reversis - Reciclagem de Eletrônicos e Informática) fica na R. da Abolição, 1900 - Pte. Preta, Campinas - SP, 13041-445'])
        return x
    elif x > 130 and x <= 180:
        print(['telefones, impressora, vídeo, cassete, aparelho DVD', '(Ecoponto / Ponto Verde) fica na Av. Santa Isabel, 2300 - Barão Geraldo, Campinas -SP, 13084-012'])
        return x
    elif x > 180 and x <= 230:
        print(['Computador, televisor, monitor, notebook, celular, tablet',
        'Ponto de coleta: (Reversis - Reciclagem de Eletrônicos e Informática) fica na R. da Abolição, 1900 - Pte. Preta, Campinas - SP, 13041-445'], '\n',
        ['no Break, estabilizador, cabos de energia', 'Ponto de coleta: (GMV Recycle) fica na Rod. Lix da Cunha, 911 - Jardim do Lago II, Campinas - SP, 13051-051'])
        return x
    elif x > 230 and x <= 280:
        print(['Computador, televisor, monitor, notebook, celular, tablet',
        'Ponto de coleta: (Reversis - Reciclagem de Eletrônicos e Informática) fica na R. da Abolição, 1900 - Pte. Preta, Campinas - SP, 13041-445'])
        return x

#Converte uma opção d0 menu (1, 2, 3, etc.)
def MaterialSelecionado(latitude, longitude, opcao):
    if latitude < -90 or latitude > 90 or longitude < -180 or longitude > 180:
        return 'coordenadas invalidas'

    elif (-90 <= latitude <= 90) and (-180 <= longitude <= 180):
        float(latitude)
        float(longitude)

        z = latitude + longitude
        if opcao == 1:
            return MaterialEscolhidoPlastico(z)
        elif opcao == 2:
            return MaterialEscolhidoMetal(z)
        elif opcao == 3:
            return MaterialEscolhidoVidro(z)
        elif opcao == 4:
            return MaterialEscolhidoPapel(z)
        elif opcao == 5:
            return MaterialEscolhidoEletro(z)


# teste condicional coordenadas para material reciclável proximo,
def coordenada_la(latitude, longitude):
    if latitude < -90 or latitude > 90 or longitude < -180 or longitude > 180:
        return 'coordenadas invalidas'

    elif -90 <= latitude <= 90 and -180 <= longitude <= 180:
        float(latitude)
        float(longitude)
        # metodo simples para converter coordenadas em defimal
        x = latitude + longitude
        if -291 >= x <= -230:
            x = ['no Break', 'cobre', 'níquel', 'Pote de sorvete', 'Garrafas Pet', 'embalagem de cosméticos']
            return x

        elif -229 >= x <= -200:
            x = ['embalagens de alimentos ', 'guarda napos', 'Papelão']
            return x

        elif -199 >= x <= -152:
            x = ['aparelho DVD, telefones, frascos shampoo, embalagem de leite']
            return x

        elif -151 >= x <= -116:
            x = ['televisor, revista, Garrafa de alvejante, mercúrio']
            return x

        elif -115 >= x <= -94:
            x = ['PVC, embalagem de cosméticos, embalagem de leite, Garrafa detergente ']
            return x

        elif -93 >= x <= -79:
            x = ['cabos de energia, embalagens de alimentos,  notebook ']
            return x

        elif -78 >= x <= -50:
            x = ['caixa de som, impressora, monitor, tablet, mercúrio ']
            return x

        elif -49 >= x <= -1:
            x = ['Vidro para Pavimentos, vidro temperado, brinquedo lego']
            return x

        elif -0 >= x <= 30:
            x = ['impressora, cabos de energia, frascos shampoo, alumínio']
            return x

        elif 31 >= x <= 51:
            x = ['estabilizador, revista, partes internas de geladeira']
            return x

        elif 52 >= x <= 92:
            x = ['Computador, ferro, cobre, brinquedo lego']
            return x

        elif 93 >= x <= 110:
            x = ['brinquedo lego, remedios, tablet, lista telefonica']
            return x

        elif 111 >= x <= 135:
            x = ['sacola de supermercado, microondas, papel para imprimir, televisor']
            return x

        elif 136 >= x <= 157:
            x = ['brinquedos de plastico, garrafa de vidro, telefones, aparelho DVD']
            return x

        elif 158 >= x <= 178:
            x = ['painel de vidro, baterias, peças de carro, notebook']
            return x

        elif 179 >= x <= 200:
            x = ['vidro termoendurecido, vidro acústico, janela, vidro temperado']
            return x

        elif 201 >= x <= 220:
            x = ['sacola plastica, garrafa pet, pote de alimento, caixa de remedio']
            return x

        elif 221 >= x <= 240:
            x = ['vidro termoendurecido, vidro lacado, vidro controle Acústico, vidro controle Solar, '
                 'pepel higienico, papel toalha, guarda napos']
            return x

        elif 241 >= x <= 251:
            x = ['sacola plastica, garrafa pet, pote de alimento, caixa de remedio, caixa de som, impressora']
            return x

        elif 252 >= x <= 260:
            x = ['Computador, ferro, baterias, peças de carro']
            return x


        elif 261 >= x <= 265:
            x = ['embalagens de alimentos e remedios, lista telefonica, jornal']
            return x

        elif 230 >= x <= 280:
            x = ['baterias, celulares e telefones']
            return x

        else:
            x = ['painel de vidro, baterias, peças de carro, notebook, caixa de som, impressora, monitor, tablet, mercúrio']
            return x

#Pontos de coleta
def PontosColeta(latitude,longitude):
    if latitude < -91 or latitude > 90 or longitude < -181 or longitude > 180:
        return 'coordenadas invalidas, tente novamente'

    elif -90 <= latitude <= 90 and -180 <= longitude <= 180:
        float(latitude)
        float(longitude)
        # metodo simples de calcular lugares proximos
        x = latitude + longitude
        if -291 >= x <= -240:
            print('', ['(GMV Recycle) fica na Rod. Lix da Cunha, 911 - Jardim do Lago II, Campinas - SP, 13051-051'],
                  '\n',
                  ['(FERRO VELHO CLEBER) R. Pref. Celso Daniel, 161 - Vila San Martin, Campinas - SP, 13069-079'])
            return latitude, longitude
        elif -239 >= x <= -215:
            print('', ['(GMV Recycle) fica na Rod. Lix da Cunha, 911 - Jardim do Lago II, Campinas - SP, 13051-051'],'\n',
                  ['Rua Manoel Gomes Ferreira, esq. com Rua José Ramos Catarino'], '\n',
                  ['Sucatas e Metais 2 Irmãos | Ferro Velho em Campinas | Sucatas em Campinas: R. Guaiçara, 354 - Jardim Itatinga, Campinas - SP, 13052-442'])
            return latitude, longitude
        elif -239 >= x <= -215:
            print('', ['(Latem) Av. Orozimbo Maia, 2062 - Cambuí - Campinas, SP - CEP: 13024-045'], '\n',
                  ['Av. São José dos campos s/ n°, Vl Campos Sales'], '\n',
                  ['(Reversis - Reciclagem de Eletrônicos e Informática) fica na R. da Abolição, 1900 - Pte. Preta, Campinas - SP, 13041-445'])
            return latitude, longitude
        elif -239 >= x <= -215:
            print('', ['Rua josé martins lourenço, esq. com Rua Geraldo Bretas, jd. São Gabriel'], '\n',
                  ['Ponto verde - Vila Costa e Silva Rua Saldanha da Gama, 77 Ecoponto'], '\n',
                  ['(Papeis zambelli)R Leonor Ponessi Cappelli, 210, Parque Rural Fazenda Santa Cândida - Campinas, SP'], '\n',
                  ['FERRO VELHO CLEBER: R. Pref. Celso Daniel, 161 - Vila San Martin, Campinas - SP, 13069-079'])
            return latitude, longitude
        elif -214 >= x <= -190:
            print('', ['Rua Serra Dourada 165, Campinas, SP, 13100-312'], '\n',
                  ['Rua Celso soares Couto s/n°, Pq. Itajaí'], '\n',
                  ['Ferro Velho Roberto, Compra E Venda De Sucatas: R. Marquês de Abrantes, 600 - Jardim Santa Genebra, Campinas - SP, 13080-220'], '\n',
                  ['Ponto Verde Av. Santa Isabel, 2300, Ecoponto Jardim EulinaAv. Mal. Rondon'])
            return latitude, longitude
        elif -189 >= x <= -169:
            print('', ['(Papeis zambelli)R Leonor Ponessi Cappelli, 210, Parque Rural Fazenda Santa Cândida - Campinas, SP'], '\n',
                  ['Ponto verde - Vila Costa e Silva Rua Saldanha da Gama, 77 Ecoponto'], '\n',
                  ['(Ecoponto / Ponto Verde) fica na Av. Santa Isabel, 2300 - Barão Geraldo, Campinas -SP, 13084-012'], '\n',
                  ['R São José do Rio Preto, 1101 - Jardim Nova Europa - Campinas, SP - CEP: 13040-060'])
            return latitude, longitude
        elif -168 >= x <= -148:
            print('', ['Ponto de coleta: Rua Serra Dourada 165, Campinas, SP, 13100-312'], '\n',
                  ['Ponto-Verde Av. Santa Isabel, 2300 Ecoponto Jardim Eulina Av. Mal. Rondon'], '\n',
                  ['(Reversis - Reciclagem de Eletrônicos e Informática) fica na R. da Abolição, 1900 - Pte. Preta, Campinas - SP, 13041-445'], '\n',
                  ['(Latem) Av. Orozimbo Maia, 2062 - Cambuí - Campinas, SP - CEP: 13024-045'])
            return latitude, longitude
        elif -147 >= x <= -120:
            print('', ['Ferro Velho Roberto, Compra E Venda De Sucatas: R. Marquês de Abrantes, 600 - Jardim Santa Genebra, Campinas - SP, 13080-220'], '\n',
                  ['Av. Marechal Rondon, esq. com Rua josé Manuel Veiga, jd. Eulina'], '\n',
                  ['(Ecoponto / Ponto Verde) fica na Av. Santa Isabel, 2300 - Barão Geraldo, Campinas -SP, 13084-012'], '\n',
                  ['Rua Manoel Gomes Ferreira, esq. com Rua José Ramos Catarino'])
            return latitude, longitude
        elif -119 >= x <= -100:
            print('', ['(Papeis zambelli)R Leonor Ponessi Cappelli, 210, Parque Rural Fazenda Santa Cândida - Campinas, SP'], '\n',
                  ['(Latem) Av. Orozimbo Maia, 2062 - Cambuí - Campinas, SP - CEP: 13024-045'], '\n',
                  ['(GMV Recycle) fica na Rod. Lix da Cunha, 911 - Jardim do Lago II, Campinas - SP, 13051-051'], '\n',
                  ['Ponto verde - Vila Costa e Silva Rua Saldanha da Gama, 77 Ecoponto'])
            return latitude, longitude
        elif -99 >= x <= -84:
            print('', ['Rua Celso soares Couto s/n°, Pq. Itajaí'], '\n',
                  ['Ponto verde - Vila Costa e Silva Rua Saldanha da Gama, 77 Ecoponto'], '\n',
                  ['Rua josé martins lourenço, esq. com Rua Geraldo Bretas, jd. São Gabriel'])
            return latitude, longitude
        elif -83 >= x <= -64:
            print('', ['(Papeis zambelli)R Leonor Ponessi Cappelli, 210, Parque Rural Fazenda Santa Cândida -- Campinas, SP'], '\n',
                  ['(comercio de sucatas rodrigues) R Itacuruçá, 480 - Jardim Aeroporto de Viracopos - Campinas, SP - CEP: 13056-094'], '\n',
                  ['R São José do Rio Preto, 1101 - Jardim Nova Europa - Campinas, SP - CEP: 13040-060'], '\n',
                  ['Ferro Velho Roberto, Compra E Venda De Sucatas: R. Marquês de Abrantes, 600 - Jardim Santa Genebra, Campinas - SP, 13080-220'])
            return latitude, longitude
        elif -63 >= x <= -20:
            print('', ['(Marapara maravalhas aparas de papel papelão e sucatas) R São José do Rio Preto, 1101 - Jardim Nova Europa - Campinas, SP - CEP: 13040-060'], '\n',
                  ['Ponto verde - Vila Costa e Silva Rua Saldanha da Gama, 77 Ecoponto'], '\n',
                  ['FERRO VELHO CLEBER: R. Pref. Celso Daniel, 161 - Vila San Martin, Campinas - SP, 13069-079'], '\n',
                  ['Rua josé martins lourenço, esq. com Rua Geraldo Bretas, jd. São Gabriel'])
            return latitude, longitude
        elif -19 >= x <= 2:
            print('', ['R São José do Rio Preto, 1101 - Jardim Nova Europa - Campinas, SP - CEP: 13040-060'], '\n',
                  ['Ponto-Verde Av. Santa Isabel, 2300 Ecoponto Jardim Eulina Av. Mal. Rondon'], '\n',
                  ['(Ecoponto / Ponto Verde) fica na Av. Santa Isabel, 2300 - Barão Geraldo, Campinas -SP, 13084-012'], '\n',
                  ['FERRO VELHO CLEBER: R. Pref. Celso Daniel, 161 - Vila San Martin, Campinas - SP, 13069-079'])
            return latitude, longitude
        elif 3 >= x <= 26:
            print('', ['(Latem) Av. Orozimbo Maia, 2062 - Cambuí - Campinas, SP - CEP: 13024-045'], '\n',
                  ['Rua Serra Dourada 165, Campinas, SP, 13100-312'], '\n',
                  ['FERRO VELHO CLEBER: R. Pref. Celso Daniel, 161 - Vila San Martin, Campinas - SP, 13069-079'], '\n',
                  ['Ponto-Verde Av. Santa Isabel, 2300 Ecoponto Jardim Eulina Av. Mal. Rondon'])
            return latitude, longitude
        elif 27 >= x <= 57:
            print('', ['Rua Manoel Gomes Ferreira, esq. com Rua José Ramos Catarino'], '\n',
                  ['(Ecoponto / Ponto Verde) fica na Av. Santa Isabel, 2300 - Barão Geraldo, Campinas -SP, 13084-012'], '\n',
                  ['(Reversis - Reciclagem de Eletrônicos e Informática) fica na R. da Abolição, 1900 - Pte. Preta, Campinas - SP, 13041-445'])
            return latitude, longitude
        elif 58 >= x <= 90:
            print('', ['(Marapara maravalhas aparas de papel papelão e sucatas) R São José do Rio Preto, 1101 - Jardim Nova Europa - Campinas, SP - CEP: 13040-060'], '\n',
                  ['Ferro Velho Roberto, Compra E Venda De Sucatas: R. Marquês de Abrantes, 600 - Jardim Santa Genebra, Campinas - SP, 13080-220'])
            return latitude, longitude
        elif 91 >= x <= 130:
            print('', ['Ponto verde - Vila Costa e Silva Rua Saldanha da Gama, 77 Ecoponto'], '\n',
                  ['Ferro Velho Roberto, Compra E Venda De Sucatas: R. Marquês de Abrantes, 600 - Jardim Santa Genebra,'
                   + ' Campinas - SP, 13080-220'], '\n',
                  ['(GMV Recycle) fica na Rod. Lix da Cunha, 911 - Jardim do Lago II, Campinas - SP, 13051-051'], '\n',
                  ['(Reversis - Reciclagem de Eletrônicos e Informática) fica na R. da Abolição, 1900 - Pte. Preta, '
                   + 'Campinas - SP, 13041-445'])
            return latitude, longitude
        elif 131 >= x <= 163:
            print('', ['Ponto verde - Vila Costa e Silva Rua Saldanha da Gama, 77 Ecoponto'], '\n',
                  ['(Papeis zambelli)R Leonor Ponessi Cappelli, 210, Parque Rural Fazenda Santa Cândida - Campinas, SP']
                  , '\n',
                  ['(comercio de sucatas rodrigues) R Itacuruçá, 480 - Jardim Aeroporto de Viracopos - Campinas, '
                   + 'SP - CEP: 13056-094'], '\n',)
            return latitude, longitude
        elif 164 >= x <= 200:
            print('', ['Av. São José dos campos s/ n°, Vl Campos Sales'], '\n',
                  ['Ponto-Verde Av. Santa Isabel, 2300 Ecoponto Jardim Eulina Av. Mal. Rondon'], '\n',
                  ['Av. Orozimbo Maia, 2062 - Cambuí - Campinas, SP - CEP: 13024-045'], '\n',
                  ['R São José do Rio Preto, 1101 - Jardim Nova Europa - Campinas, SP - CEP: 13040-060'])
            return latitude, longitude
        elif 201 >= x <= 231:
            print('', ['Av. Santa Isabel, 2300 - Barão Geraldo, Campinas -SP, 13084-012'], '\n',
                  ['(Reversis - Reciclagem de Eletrônicos e Informática) fica na R. da Abolição, 1900 - Pte. Preta, Campinas - SP, 13041-445'], '\n',
                  ['Ponto-Verde Av. Santa Isabel, 2300 Ecoponto Jardim Eulina Av. Mal. Rondon'])
            return latitude, longitude
        elif 232 >= x <= 260:
            print('', ['Rua josé martins lourenço, esq. com Rua Geraldo Bretas, jd. São Gabriel'], '\n',
                  ['Sucatas em Campinas: R. Guaiçara, 354 - Jardim Itatinga, Campinas - SP, 13052-442'])
            return latitude, longitude
        elif 261 >= x <= 300:
            print('', ['(Reversis - Reciclagem de Eletrônicos e Informática) fica na R. da Abolição, 1900 - Pte. Preta, Campinas - SP, 13041-445'], '\n',
                  ['Av. Marechal Rondon, esq. com Rua josé Manuel Veiga, jd. Eulina'], '\n',
                  ['Ponto verde - Vila Costa e Silva Rua Saldanha da Gama, 77 Ecoponto'], '\n',
                  ['Rua josé martins lourenço, esq. com Rua Geraldo Bretas, jd. São Gabriel'])
            return latitude, longitude
        elif x <= 270:
            print('', [
                '(Reversis - Reciclagem de Eletrônicos e Informática) fica na R. da Abolição, 1900 - Pte. Preta, Campinas - SP, 13041-445'],
                  '\n',
                  ['Av. Marechal Rondon, esq. com Rua josé Manuel Veiga, jd. Eulina'], '\n',
                  ['Av. Orozimbo Maia, 2062 - Cambuí - Campinas, SP - CEP: 13024-045'])
            return latitude, longitude
        else:
            return 'Coordenadas inválidas'


print('Seja bem-vindo!')
print("""Este programa tem como finalidade localizar tipos de materiais e os pontos de coleta
para a reciclagem próximos de você.
Observação: coordenada latitude começa de -90 até 90 e longitude de -180 até 180, cuidado com as informações que for digitar
""")
opcao = 1

#Menu de opções
while opcao != 9:
    print(""" 
Menu de opções:
[1] - Plastico
[2] - Metal
[3] - Vidro
[4] - Papel
[5] - Eletrônicos
[6] - Materiais proximos para coletar
[7] - Pontos para coleta proximos
[9] - Encerrar programa""")

    opcao = float(input('Digite a opção desejada: '))
    z = opcao
    if z == 1:
        print('Você selecionou "Plastico" \nlocalizando pontos de coleta proximos')
        latitude = float(input('latitude: '))
        longitude = float(input('longitude: '))
        MaterialSelecionado(latitude, longitude, opcao)
        print("""Sobre: São formados por polímeros(Tereftalato de Polietileno, Polietileno de Alta Densidade
Poli cloreto de Vinila, Polietileno de Baixa Densidade, Polipropileno e Poliestireno), 
divididos em grupos de termoplásticos(podem ser reciclado) e termorrígidos (não são recicláveis).
Reutilização:
* vaso para plantas utilizando PETS
* Porta lápis 
* Fazer decoração para casa
* casa de pássaros 
* brinquedos """)

    elif z == 2:
        print('Você selecionou "Metal" \nlocalizando pontos de coleta proximos')
        latitude = float(input('latitude: '))
        longitude = float(input('longitude: '))
        MaterialSelecionado(latitude, longitude, opcao)
        print("""Sobre: Separados por ferrosos e não ferrosos. Ferrosos possuem propriedades magnéticas, 
já os não ferrosos não possuem quantia grande de ferro.
Reutilização:
São derretidos para recriar outros tipos de materiais. 
Os metais mais utilizados são alumínio, ferro, aço e cobre.""")

    elif z == 3:
        print('Você selecionou "Vidro" \nlocalizando pontos de coleta proximos')
        latitude = float(input('latitude: '))
        longitude = float(input('longitude: '))
        MaterialSelecionado(latitude, longitude, opcao)
        print("""Sobre: é uma misturara de produtos inorgânicos: dióxido de silício, 
barrilha ou soda (carbonato de sódio - Na2CO3) e calcário (carbonato de cálcio – CaCO3). 
a mistura dos três podem criar o vidro.
Reutilização:
O vidro no seu processo quando reaproveitado, é utilizado para criar outros tipos de materiais feito de vidro """)

    elif z == 4:
        print('Você selecionou "Papel" \nlocalizando pontos de coleta proximos')
        latitude = float(input('latitude: '))
        longitude = float(input('longitude: '))
        MaterialSelecionado(latitude, longitude, opcao)
        print("""Sobre: O papel comum tem como matéria prima, fibras de celulose extraídas de
arvores, como o pinheiro e o eucalipto.
Reutilização: 
* fazer embrulho para presentes;
* fatiado serve para forro de gaiola;
* possível fazer fogueira, para acender churrasqueira;
* recortes serve para fazer artesanato;
* papeis velhos é possível criar uma folha nova reciclada""")

    elif z == 5:
        print('Você selecionou "Eletrônicos" \nlocalizando pontos de coleta proximos')
        latitude = float(input('latitude: '))
        longitude = float(input('longitude: '))
        MaterialSelecionado(latitude, longitude, opcao)
        print("""
Sobre: são componentes que controlados por circuitos elétricos, esse circuito 
pode se manifestar de diversas maneiras, como visual, sonora, mecânica, emitir ondas de rádio e muito mais.  
Reutilização:
* recriar novos equipamentos;
* vidro pode ser vendido para empresas que usam matéria prima; """)

    elif z == 6:
        print('localizando materiais reciclaveis proximos')
        la = float(input('latitude: '))
        lon = float(input('longitude: '))
        print(coordenada_la(la, lon))

    elif z == 7:
        print('localizando pontos de coleta proximos')
        latitude = float(input('latitude: '))
        longitude = float(input('longitude: '))
        print(PontosColeta(latitude, longitude))

    elif z == 9:
        print("""Autores:
Lucas Alves de Souza Marques Timoteo - N555696
Leonardo Slonzo Alvares Portes – F3079A9
Nathan Duarte da Silva – N6188C2
Rafael Mascarenhas – F19DAD3
Vinicius de Campos da Silva – F206BA7
        """)
        print('Encerrando programa!!')
        exit()

    else:
        print('valor invalido, tente novamente')
