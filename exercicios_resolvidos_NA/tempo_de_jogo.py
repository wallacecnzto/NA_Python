hora_inicial = int(input("Hora inicial: "))
hora_final = int(input("Hora final: "))

if hora_inicial < hora_final:
    duracao = hora_final - hora_inicial
    print(f"O JOGO DUROU {duracao} HORAS(S)")
else:
    duracao = 24 - (hora_inicial - hora_final)
    print(f"O JOGO DUROU {duracao} HORAS(S)")
