import argparse
from datetime import datetime, timedelta

def calcular_saida(hora_entrada_str, duracao_almoco_str):
    # Converte strings em objetos datetime e timedelta
    hora_entrada = datetime.strptime(hora_entrada_str, "%H:%M")
    duracao_almoco = timedelta(
        hours=int(duracao_almoco_str.split(":")[0]),
        minutes=int(duracao_almoco_str.split(":")[1])
    )

    jornada = timedelta(hours=8)  # Jornada CLT padrão
    hora_saida = hora_entrada + jornada + duracao_almoco
    return hora_saida.strftime("%H:%M")

def main():
    parser = argparse.ArgumentParser(description="Calcula o horário de saída para cumprir 8h de jornada CLT.")
    parser.add_argument("entrada", help="Horário de entrada no formato HH:MM (ex: 08:30)")
    parser.add_argument("almoco", help="Duração do almoço no formato HH:MM (ex: 01:00)")

    args = parser.parse_args()
    saida = calcular_saida(args.entrada, args.almoco)
    print(f"Você deve sair às {saida} para completar 8h de trabalho.")

if __name__ == "__main__":
    main()
