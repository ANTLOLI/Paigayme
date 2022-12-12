#!/usr/bin/python3
from buttons import Button

# Constantes

w, h = pygame.display.get_surface().get_size()

# Criando botões
button1=Button(w-50,)


# Definindo as variaveis da grid do mapa 1

X = 3
Y = 0
A1 = [1, 2, 3, 4, 5]
B2 = [1, 2, 3, 4, 5]
C2 = [1, 2, 3, 4, 5]
D3 = [1, 2, 3, 4, 5]
E4 = [1, 2, 3, 4, 5]
posY = ["E", "D", "C", "B", "A"]

# Definindo as variaveis de itens, locais, eventos...

r=0
lp = 100
gameover = "false"
doorswitch = 0
doorkey = 0
axe = "false"
brknswitch = "true"
ind_action = 0
beentohouse = "false"
beentoroses = "false"
rosehint = "false"
beentoswitch1 = "false"
beentoswitch2 = "false"
beentochest = "false"
esfinge = "false"
total_energy = 10
end_battle = 'false'
final_boss = 'false'
battle_decision = "false"
repeat_index2 = 0
repeat_index = 0

# life points decay
def lp_decay(lpd, gameover, lp):
    lp -= lpd
    if lp == 0:
        gameover = 'true'
    else:
        gameover = 'false'
    return lpd, gameover, lp


# battle
def battle_nanone(n1, elp, n2, battle_decision, repeat_index2, repeat_index, total_energy, gameover,lp):
    while battle_decision == 'false':
        import random
        enemy_action_indice = random.getrandbits(1)
        eai = enemy_action_indice % 2
        if elp < 0:
            battle_decision = 'true'
        else:
            if eai == 0:
                repeat_index2 = 0
                repeat_index += 1
                if repeat_index == 1:
                    enemy_damage = n1
                elif repeat_index == 2:
                    enemy_damage = round(n1 * 0.7, 0)
                elif repeat_index == 3:
                    enemy_damage = round(n1 * 0.5, 0)
                elif repeat_index >= 4:
                    enemy_damage = round(n1 * 0.2, 0)
                print(f'O inimigo causará {enemy_damage} de dano no proximo turno.')
                print('(Deseja atacar, correr ou perdoar?)')
                dec = input('')
                if dec == 'atacar':
                    while end_battle == 'false':
                        print('(Atacar, defender ou repousar?')
                        battle_action = input('')
                        if battle_action == 'atacar':
                            print(f'(deseja consumir qantos pontos de energia?), você possui {total_energy}')
                            eng = int(input(''))
                            total_energy -= eng
                            dmg = eng * 10
                            elp -= dmg
                            lp_decay(enemy_damage, gameover, lp)
                            lpd, gameover, lp = lp_decay(enemy_damage, gameover, lp)
                            print(f"Ainda lhe sobram {lp} pontos de vida")
                            break
                        elif battle_action == 'defender':
                            print(f'(deseja consumir qantos pontos de energia?), você possui {total_energy}')
                            eng = int(input(''))
                            total_energy -= eng
                            dfc = eng * 8
                            fedmg = enemy_damage - dfc
                            if fedmg >= 1:
                                lp_decay(fedmg, gameover, lp)
                                lpd, gameover, lp = lp_decay(enemy_damage, gameover, lp)
                                print(f"Ainda lhe sobram {lp} pontos de vida")
                                break
                            else:
                                break
                        elif battle_action == 'repousar':
                            total_energy = 10
                            lp_decay(enemy_damage, gameover, lp)
                            lpd, gameover, lp = lp_decay(enemy_damage, gameover, lp)
                            print(f"Ainda lhe sobram {lp} pontos de vida")
                            break
                elif dec == 'correr':
                    agility = elp / lp
                    if agility >= 2:
                        print('(você foge do inimigo, reconhecendo-o como um igual)')
                        battle_decision = 'true'
                    elif manto_do_covarde == "true":
                        if final_boss == 'false':
                            print('(você foge do inimigo, reconhecendo-o como um igual)')
                            battle_decision = 'true'
                        elif final_boss == 'true':
                            print('(você foge como um covarde, enquanto o inimigo ri de você)')
                    else:
                        print('(Você falha em fugir e acredita que não possui outra opção senão lutar)')
                elif dec == 'perdoar':
                    if final_boss == 'false':
                        print('(Você não conheceu nenhuma flor, portanto esta ação não será útil)')
                    else:
                        print('(Você sente um conforto na criatura, como se presenciasse uma memoria feliz)')
                        print('(Após um longo tempo adimirando-a, você percebe o seu dever e se curva perante seu mestre)')
                        print('Real ending')
                        exit()
            else:
                repeat_index = 0
                repeat_index2 += 1
                if repeat_index2 == 1 or repeat_index2 == 2:
                    enemy_defense = n2
                elif repeat_index2 == 3:
                    enemy_defense = round(n2 * 0.76, 0)
                elif repeat_index2 == 4:
                    enemy_defense = round(n2 * 0.6, 0)
                elif repeat_index2 >= 5:
                    enemy_defense = round(n2 * 0.36, 0)
                print(f'O inimigo defenderá {enemy_defense} de dano no proximo turno.')
                print('(Deseja atacar, correr ou perdoar?)')
                dec = input('')
                if dec == 'atacar':
                    while end_battle == 'false':
                        print('(Atacar, defender ou repousar?')
                        battle_action = input('')
                        if battle_action == 'atacar':
                            print(f'(deseja consumir qantos pontos de energia?), você possui {total_energy}')
                            eng = int(input(''))
                            total_energy -= eng
                            dmg = eng * 10
                            fdmg = dmg - enemy_defense
                            if fdmg >= 1:
                                elp -= fdmg
                                break
                            else:
                                break
                        elif battle_action == 'defender':
                            print(f'(deseja consumir qantos pontos de energia?), você possui {total_energy}')
                            eng = int(input(''))
                            total_energy -= eng
                            dfc = eng * 8
                            break
                        elif battle_action == 'repousar':
                            total_energy = 10
                            break
                elif dec == 'correr':
                    agility = elp / lp
                    if agility >= 2:
                        print('(você foge do inimigo, reconhecendo-o como um igual)')
                        battle_decision = 'true'
                    elif manto_do_covarde == "true":
                        if final_boss == 'false':
                            print('(você foge do inimigo, reconhecendo-o como um igual)')
                            battle_decision = 'true'
                        elif final_boss == 'true':
                            print('(você foge como um covarde, enquanto o inimigo ri de você)')
                    else:
                        print('(Você falha em fugir e acredita que não possui outra opção senão lutar)')
                elif dec == 'perdoar':
                    if final_boss == 'false':
                        print('(Você não conheceu nenhuma flor, portanto esta ação não será útil)')
                    else:
                        print('(Você sente um conforto na criatura, como se presenciasse uma memoria feliz)')
                        print('(Após um longo tempo adimirando-a, você percebe o seu dever e se curva perante seu mestre)')
                        print('Real ending')
                        exit()

# Setar as funções

def move(X, Y):
    if X == 1 and Y != 0 and Y != 4:
        # Movimento do lado esquerdo da grid (tirando os cantos)
        print("Seguir a diante, para direita ou para trás?")
        walk = input("")
        if walk == "diante":
            Y += 1
        elif walk == "direita":
            X += 1
        elif walk == "trás":
            Y -= 1
        else:
            print("Comando inválido")
    elif X == 5 and Y != 0 and Y != 4:
        # Movimento do lado direito da grid (Tirando os cantos)
        print("Seguir a diante, para esquerda ou para trás?")
        walk = input("")
        if walk == "diante":
            Y += 1
        elif walk == "esquerda":
            X -= 1
        elif walk == "trás":
            Y -= 1
        else:
            print("Comando inválido")
    elif Y == 0 and X != 1 and X != 5:
        # Movimento da parte inferior extrema da grid (tirando os cantos)
        print("Seguir a diante, para esquerda ou para direita?")
        walk = input("")
        if walk == "diante":
            Y += 1
        elif walk == "esquerda":
            X -= 1
        elif walk == "direita":
            X += 1
        else:
            print("Comando inválido")
    elif Y == 4 and X != 1 and X != 5:
        # Movimento do lado superior extremo da grid (Tirando os cantos)
        print("Seguir a trás, para esquerda ou para direita?")
        walk = input("")
        if walk == "trás":
            Y -= 1
        elif walk == "esquerda":
            X -= 1
        elif walk == "direita":
            X += 1
        else:
            print("Comando inválido")
    elif X != 1 and X != 5 and Y != 0 and Y != 4:
        # Movimento do centro da grid
        print("Seguir a diante, para trás, para esquerda ou para direita?")
        walk = input("")
        if walk == "diante":
            Y += 1
        elif walk == "esquerda":
            X -= 1
        elif walk == "direita":
            X += 1
        elif walk == "trás":
            Y -= 1
        else:
            print("Comando inválido")
    elif X == 1 and Y == 0:
        # Movimento do canto inferior esquerdo
        print("Seguir a diante ou para direita?")
        walk = input("")
        if walk == "diante":
            Y += 1
        elif walk == "direita":
            X += 1
        else:
            print("He was here")
    elif X == 1 and Y == 4:
        # Movimento do canto superior esquerdo
        print("Seguir para trás ou para direita?")
        walk = input("")
        if walk == "trás":
            Y -= 1
        elif walk == "direita":
            X += 1
        else:
            print("Comando inválido")
    elif X == 5 and Y == 0:
        # Movimento do canto inferior direito
        print("Seguir a diante ou para esquerda?")
        walk = input("")
        if walk == "diante":
            Y += 1
        elif walk == "esquerda":
            X -= 1
        else:
            print("Comando inválido")
    elif X == 5 and Y == 4:
        # Movimento do canto superior direita
        print("Seguir para trás ou para a esquerda?")
        walk = input("")
        if walk == "trás":
            Y -= 1
        elif walk == "esquerda":
            X -= 1
        else:
            print("You can't save them")
    return X, Y
    print("")


# Gameplay

print("(Você se encontra em uma enorme e densa floresta)")
print("(Você nunca teve uma boa memória, então não se lembra de muitas coisas)")
print("(Mas você sabe exatamente o que precisa fazer)\n")
print("(É dificil de enxergar os seus arredores, mas é fácil distinguir os caminhos que você pode seguir)\n")
def game_execute():
    X, Y = move(X, Y)
    # Patches
    if X == 3 and Y == 3:
        print('(Você se depara com uma sala vazia e escura, com um suspeito buraco no centro)')
        print('(Ao se aproximar do buraco, você é confrontado por um homem careca e mal vestido)')
        print('(O homem diz "Ali, aquele buraco, olhe mais de perto")')
        print('(Desejas olhar?)')
        bald = input("")
        if bald == 'sim':
            print('(Você é empurrado e morre, nunca confie em um careca)')
            gameover = 'true'
    #Bandcoot
    elif X==4 and Y == 1:
        if r == 0:
            print("Você encontra uma ogro estranho, seu nome aparenta ser Kresh")
            battle_nanone(20, 200, 30, battle_decision, repeat_index2, repeat_index, total_energy,gameover,lp)
            r +=1
        else:
            print("Você já derrotou a criatura que residia aqui")
    # posição da catacumba A3
    if X == 3 and Y == 4:
        print("(Você se encontra no que parece ser a entrada de uma grande catacumba)\n")
        print("(Tentar abrir o grande portão?)")
        opengr8door = input("")
        if opengr8door == "sim":
            if doorswitch == 0 and doorkey == 0:
                print("(Não abre, parece estar trancada)")
                print(
                    "(Há um espaço para uma chave grande e duas grandes travas que impedem o portão de ser aberto)\n")
                print("(Tentar arrombar o grande portão?)")
                breakin = input("")
                if breakin == "sim":
                    if axe == "false":
                        print("(O portão é muito resistente, você não seria capaz de fazer um arranhão)\n")
                        print("(Você se afasta da grande catacumba)\n")
                    elif axe == "true":
                        print("(Ao tentar arrombar a catacumba, seu machado rompe em dois)")
                        print("(O cabo pode vir a calhar)\n")
                        print("(Você se afasta da grande catacumba)\n")
                        axe = "false"
                        brknswitch = "false"
                elif breakin == "não":
                    print("(Você percebe que isso definitivamente não seria uma boa ideia)\n")
                    print("(Você se afasta da grande catacumba)\n")
                else:
                    print("Comando inválido")
            elif doorswitch == 1 and doorkey == 0:
                print("(Há um espaço para uma chave grande e uma grande trava que impedem o portão de ser aberto)")
                print("Tentar arrombar o grande portão?)")
                breakin = input("")
                if breakin == "sim":
                    if axe == "false":
                        print("(O portão é muito resistente, você não seria capaz de fazer um arranhão)\n")
                        print("(Você se afasta da grande catacumba)\n")
                    elif axe == "true":
                        print("(Ao tentar arrombar a catacumba, seu machado rompe em dois)")
                        print("(O cabo pode vir a calhar)\n")
                        print("(Você se afasta da grande catacumba)\n")
                        axe = "false"
                        brknswitch = "false"
                elif breakin == "não":
                    print("(Você percebe que isso definitivamente não seria uma boa ideia)\n")
                    print("(Você se afasta da grande catacumba)\n")
                else:
                    print("Comando inválido")
            elif doorswitch == 2 and doorkey == 0:
                print("(Há um espaço para uma chave grande e uma grande trava que impedem o portão de ser aberto)")
                print("Tentar arrombar o grande portão?)")
                breakin = input("")
                if breakin == "sim":
                    if axe == "false":
                        print("(O portão é muito resistente, você não seria capaz de fazer um arranhão)\n")
                    elif axe == "true":
                        print("(Ao tentar arrombar a catacumba, seu machado rompe em dois)")
                        print("(O cabo pode vir a calhar)\n")
                        print("(Você se afasta da grande catacumba)\n")
                        axe = "false"
                        brknswitch = "false"
                elif breakin == "não":
                    print("(Você percebe que isso definitivamente não seria uma boa ideia)\n")
                    print("(Você se afasta da grande catacumba)\n")
                else:
                    print("Comando inválido")
                    print("")
                    print("(Você se afasta da grande catacumba)\n")
            elif doorswitch == 2 and doorkey == 1:
                print("(Não há nada entre você e seu objetivo agora)")
                print("(Se prosseguir, não terá mais volta)\n")
                print("(Deseja prosseguir?)\n")
                proceed = input("")
                if proceed == "sim":
                    print("(Certeza?)")
                    proceed = input("")
                    if proceed == "sim":
                        final_boss = "true"
                        print("Você se encontra com algo que aparenta ser um rei segurando uma bela flor")
                        battle_nanone(32,300,24,battle_decision,repeat_index2,repeat_index,total_energy,gameover,lp)
                        print("(Você segue em direção à uma vasta escuridão)\n")
                        gameover == "true"
                    elif proceed == "não":
                        print("(Você decide se preparar antes de seguir com sua missão)\n")
                        print("(Você se afasta da grande catacumba)\n")
                    else:
                        print(
                            "(Você não consegue pensar direito sobre o que quer, então decide se preparar antes de seguir com sua missão)")
                        print("(Você se afasta da grande catacumba)\n")
                elif proceed == "não":
                    print("(Você decide se preparar antes de seguir com sua missão)\n")
                    print("(Você se afasta da grande catacumba)\n")
                else:
                    print(
                        "(Você não consegue pensar direito sobre o que quer, então decide se preparar antes de seguir com sua missão)")
                    print("(Você se afasta da grande catacumba)\n")

    # posição da alavanca 1 B2 (NEW)

    if X == 2 and Y == 3:
        if beentoswitch1 == "true":
            print("Aqui há apenas uma alavanca já ativada")
        if beentoswitch1 == "false":
            print("(Você encontra uma alavanca)")
            print("(Ativar a alavaca?)")
            ans = input("")
            if ans == "sim":
                print("Você escuta um estrondo na distância")
                doorswitch = doorswitch + 1
                beentoswitch1 = "true"
            if ans == "não":
                print("Você decide não tocar na alavanca")

    # posição da alavanca 2 A1 (NEW)

    if X == 1 and Y == 4:
        if beentoswitch2 == "true":
            print("Aqui há apenas uma alavanca já ativada")
        if beentoswitch2 == "false":
            print("(Você encontra uma alavanca)")
            print("(Ativar a alavaca?)")
            ans = input("")
            if ans == "sim":
                print("Você escuta um estrondo na distância")
                doorswitch = doorswitch + 1
                beentoswitch2 = "true"
            if ans == "não":
                print("Você decide não tocar na alavanca")

    # posição báu chave D2 (NEW)

    if X == 2 and Y == 1:
        if beentochest == "true":
            print("(Você avista o báu aberto e vázio)")
        if beentochest == "false":
            if esfinge == "false":
                print(
                    "(A diante você se encontra com um báu. Não parece ser um báu comum, sua trava possui entrada para uma resposta)")
                print("(Ao lado, uma nota diz: ")
                print("(O que é que de manhã tem quatro patas, de tarde possui apenas duas e de noite tem três?)")
                print("(Inserir algo no cadeado?)")
                ans = input("")
                if ans == "sim":
                    esfingeans = input("A resposta é: ")
                    if esfingeans != "ser humano":
                        print("(Nada acontece)")
                        esfinge = "true"
                    elif esfingeans == "ser humano":
                        print("(O báu se abre, dentro há uma chave de metal enferrujada)")
                        print("(Você o pega sem pensar duas vezes)")
                        beentochest = "true"
                        doorkey = 1
                if ans == "não":
                    print("(Você se afasta do báu)")
                    esfinge = "true"
            if esfinge == "true":
                print("(O báu continua aqui, digitar algo no cadeado?)")
                ans = input("")
                if ans == "sim":
                    esfingeans = input("A resposta é: ")
                    if esfingeans != "ser humano":
                        print("(Nada acontece)")
                        esfinge = "true"
                    elif esfingeans == "ser humano":
                        print("(O báu se abre, dentro há uma chave de metal enferrujada)")
                        print("(Você o pega sem pensar duas vezes)")
                        beentochest = "true"
                        doorkey = 1
                if ans == "não":
                    print("(Você se afasta do báu)")

    # posição da cabana E5

    if X == 5 and Y == 0:
        if beentohouse == "false":
            print("(Uma cabana decrepíta é visível de longe, pode ter algo de útil para sua missão)")
            print("(Saquear a cabana abandonada?)")
            saquear = input("")
            if saquear == "sim":
                print(
                    "(Você encontra diversas latas de sopa vencida, mas você não parece estar com tanta fome assim)")
                print(
                    "(Voltando para a porta de entrada, você percebe um machado velho e enferrujado apoiado logo ao lado)\n")
                print("(Pegar o machado?)")
                saquear = input("")
                if saquear == "sim":
                    print("(Você pega o machado)")
                    axe = "true"
                    axelock = "true"
                elif saquear == "não":
                    print("(Você decide não furtar o machado)")
                beentohouse = "true"
            elif saquear == "não":
                print("(Você decide não se aproximar da casa de aura ameaçadora)")
        elif beentohouse == "true" and axe == "false":
            print("(Você se encontra frente a frente novamente com a velha cabana)\n")
            print("(Entrar e pegar o machado?)")
            saquear = input("")
            if saquear == "sim":
                print("(Você pega o machado)")
                axe = "true"
                axelock = "true"
            elif saquear == "não":
                print("(Você decide não furtar o machado)")
        elif beentohouse == "true" and axelock == "true":
            print("(Na distância você avista a cabana decrepíta novamente)")
            print("(Já não há mais nada de útil lá)\n")

    # posição C3 fonte dica da rosa uau

    if X == 3 and Y == 2:
        print("(Você uma fonte jorrando água cristalina, há escrituras cravadas nas bordas)")
        print("(Elas dizem:)")
        print("(Através da mais profunda dor, sente-se o perfume dos ares)")
        rosehint = "true"

    # secret1

    # Não esquece de colocar as botas de hermes aqui (não sei porque)

    if X == 5 and Y == 4:
        print("(A floresta fica cada vez mais densa)")
        if rosehint == "true":
            if axe == "false":
                print("(Tem um arbusto de rosas e vinhas espinhosas)\n")
                print("(...)")
                print("(Algo parece ressoar atrás dos espinhos)")
                print("(Checar?)")
                ans = input("")
                if ans == "sim":
                    print("(Você espeta seu dedo nos espinhos, mas percebe que há algo através das vinhas)")
                    print("(Você se afasta)")
                if ans == "não":
                    print("(Você se afasta)")
            if axe == "true":
                print("(Tem um arbusto de rosas e vinhas espinhosas)\n")
                print("(...)")
                print("(Algo parece ressoar atrás dos espinhos)")
                print("(Checar?)")
                ans = input("")
                if ans == "sim":
                    print("você encontra um manto velho e rasgado")
                    manto_do_covarde = "true"
                if ans == "não":
                    print("(Você se afasta)")
        elif beentoroses == "false" and rosehint == "false":
            print("(Tem um arbusto de rosas e vinhas espinhosas)\n")
            print("(Sentir o aroma das rosas?)")
            check = input()
            if check == "sim":
                print("(Você assume que seja bom)\n")
                print("(Você se afasta)")
                beentoroses = "true"
            if check == "não":
                print("(Você prefere não perder seu tempo)\n")
                print("(Você se afasta)")
                beentoroses = "true"
    # switch 1
    elif X == 1 and Y == 3:
        if ind_action == 0:
            print('(Ao adentrar a sala você se depara com uma mesa simples.')
            print('(Esta mesa possui apenas um item similar a uma alavanca perfeitamente centralizada, como se já '
                  'soubessem que você estaria ali)')
            print('(Pegar alavanca?)')
            action = input("")
            if action == 'sim':
                print('(Você pega a alavanca e sente como se nada pudesse dar errado)')
                doorswitch += 1
                ind_action = 1
            elif action == 'não':
                print('(Embora a tentação seja grande, você decide voltar mais tarde)')
                ind_action = 2
        elif ind_action == 2:
            print('(você volta para a sala e continua sendo tentado pelo item)')
            print('(Ceder a tentação?)')
            action = input("")
            if action == 'sim':
                print('(Você pega a alavanca e sente como se nada pudesse dar errado)')
                doorswitch += 1
                ind_action = 1
            elif action == 'não':
                print('(Embora a tentação seja grande, você decide voltar mais tarde)')
                ind_action = 2
        else:
            print('(Agora esta sala transmite uma sensação de vazio)')
while gameover == 'true':
    print('De volta ao planejamento')
    exit()