import time

def main():
    """funcion que comprueba la hora del sistema
    con una hora especifica."""

    specificHour=19
    localTime=time.localtime()
    hour=localTime[3]
    minute=localTime[4]
    if hour>=specificHour:
        print("Es hora de irse.")
    else:
        print(f"Faltan {specificHour-hour-1} horas y {60-minute} minutos.")

if __name__=="__main__":
    main()