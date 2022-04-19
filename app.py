import tweepy
import time
import secrets
from random import randint

# TODO Habría que separar todo por funciones
# TODO Se guarda todo en el programa (RAM) habría que guardarlo en un fichero o una base de datos
# TODO En vez de guardar el último movimiento para comparar si ha tirado o no, guardar los mensajes que tenía la última vez, y si ahora tiene más significa que ha vuelto a "tirar"
# TODO Hacer cuando no me sigan manda el tweet, pero cuando empiezan a seguirme no hace nada
# TODO Entrada incorrecta, no se envia un mensaje diciendo que vuelva a enviar su mov

def comprobarPosibleTresEnRaya(tablero, i, x, turnoHumano):
    
    # Está en el medio
    if x == 1 and i == 1:
        # Comprobar arriba-izquierda y abajo-derecha
        if tablero[i-1][x-1] == turnoHumano and tablero[i+1][x+1] == ' ':
            return i+1, x+1
        # Comprobar arriba y abajo
        elif tablero[i][x-1] == turnoHumano and tablero[i][x+1] == ' ':
            return i, x+1
        # Comprobar arriba-derecha y abajo-izquierda
        elif tablero[i+1][x-1] == turnoHumano and tablero[i-1][x+1] == ' ':
            return i-1, x+1
        # Comprobar derecha e izquierda
        elif tablero[i+1][x] == turnoHumano and tablero[i-1][x] == ' ':
            return i+1, x
        # Comprobar abajo-derecha y arrxba-xzquxerda
        elif tablero[i+1][x+1] == turnoHumano and tablero[i-1][x-1] == ' ':
            return i-1, x-1
        # Comprobar abajo y arrxba
        elif tablero[i][x+1] == turnoHumano and tablero[i][x-1] == ' ':
            return i, x-1
        # Comprobar abajo-xzquxerda y arrxba-derecha
        elif tablero[i-1][x+1] == turnoHumano and tablero[i+1][x-1] == ' ':
            return i+1, x-1
        # Comprobar xzquxerda y derecha
        elif tablero[i-1][x] == turnoHumano and tablero[i+1][x] == ' ':
            return i+1, x
        # Devolvemos el mismo valor para decir que no hay ninguna posibilidad de hacer tres en raya
        else:
            return i, x
    else:
        # Comprobar arriba-izquierda y arriba-centro
        if tablero[0][0] == turnoHumano and tablero[0][1] == turnoHumano and tablero[0][2] == ' ':
            return 0, 2
        # Comprobar izquierda y centro
        elif tablero[1][0] == turnoHumano and tablero[1][1] == turnoHumano and tablero[1][2] == ' ':
            return 1, 2
        # Comprobar abajo-izquierda y abajo-centro
        elif tablero[2][0] == turnoHumano and tablero[2][1] == turnoHumano and tablero[2][2] == ' ':
            return 2, 2
        # Comprobar arriba-derecha y arriba-centro
        elif tablero[0][2] == turnoHumano and tablero[0][1] == turnoHumano and tablero[0][0] == ' ':
            return 0, 0
        # Comprobar derecha y centro
        elif tablero[1][2] == turnoHumano and tablero[1][1] == turnoHumano and tablero[1][0] == ' ':
            return 1, 0
        # Comprobar abajo-derecha y abajo-centro
        elif tablero[2][2] == turnoHumano and tablero[2][1] == turnoHumano and tablero[2][0] == ' ':
            return 2, 0
        # Comprobar arriba-izquierda y izquierda
        elif tablero[0][0] == turnoHumano and tablero[1][0] == turnoHumano and tablero[2][0] == ' ':
            return 2, 0
        # Comprobar arriba-centro y centro
        elif tablero[0][1] == turnoHumano and tablero[1][1] == turnoHumano and tablero[2][1] == ' ':
            return 2, 1
        # Comprobar arriba-derecha y izquierda-centro
        elif tablero[0][2] == turnoHumano and tablero[1][2] == turnoHumano and tablero[2][2] == ' ':
            return 2, 2
        # Comprobar abajo-izquierda y izquierda-centro
        elif tablero[2][0] == turnoHumano and tablero[1][0] == turnoHumano and tablero[0][0] == ' ':
            return 0, 0
        # Comprobar abajo-centro y centro
        elif tablero[2][1] == turnoHumano and tablero[1][1] == turnoHumano and tablero[0][1] == ' ':
            return 0, 1
        # Comprobar abajo-derecha y derecha-centro
        elif tablero[2][2] == turnoHumano and tablero[1][2] == turnoHumano and tablero[0][2] == ' ':
            return 0, 2
        # Comprobar arriba-izquierda y arriba-derecha
        elif tablero[0][0] == turnoHumano and tablero[0][2] == turnoHumano and tablero[0][1] == ' ':
            return 0, 1
        # Comprobar izquierda-centro y derecha-centro
        elif tablero[1][0] == turnoHumano and tablero[1][2] == turnoHumano and tablero[1][1] == ' ':
            return 1, 1
        # Comprobar abajo-izquierda y abajo-derecha
        elif tablero[2][0] == turnoHumano and tablero[2][2] == turnoHumano and tablero[2][1] == ' ':
            return 2, 1
        # Comprobar arriba-izquierda y abajo-izquierda
        elif tablero[0][0] == turnoHumano and tablero[2][0] == turnoHumano and tablero[1][0] == ' ':
            return 1, 0
        # Comprobar arriba-centro y abajo-centro
        elif tablero[0][1] == turnoHumano and tablero[2][1] == turnoHumano and tablero[1][1] == ' ':
            return 1, 1
        # Comprobar arriba-derecha y abajo-derecha
        elif tablero[0][2] == turnoHumano and tablero[2][2] == turnoHumano and tablero[1][2] == ' ':
            return 1, 2
        else:
            return x, i


def movRandom(tablero):

    listaX = []
    listaI = []

    for x in range(len(tablero)):
        for i in range(len(tablero)):
            if tablero[x][i] == ' ':
                listaX.append(x)
                listaI.append(i)

    numRandom = randint(0, len(listaX))
    numRandom -= 1
    num1 = listaI[numRandom]
    num2 = listaX[numRandom]

    return num1, num2


def mostrarTablero(tablero):
    string = ""
    string += '   1  2  3'
    for x in range(len(tablero)):
        string += '\n'
        string += str(x+1) + ' '
        for y in range(len(tablero)):
            if tablero[x][y] == ' ':
                cosa = ' _'
            else:
                cosa = tablero[x][y]
            string += cosa + ' '
    string += '\n'
    return string

# Devuelve True si inserta el movimiento, en caso contrario devuelve False


def insertarMovimiento(tablero, columna, fila, turno):
    if (tablero[fila][columna] == ' '):
        tablero[fila][columna] = turno
        return True, tablero
    else:
        return False


def pedirNum(frase=''):
    columna = -1
    while(columna < 1 or columna > 3):
        if (frase != ''):
            print(frase, end='')
        columna = int(input())
    return columna


def comprobarTresEnRaya(tablero):
    if (tablero[0][0] == tablero[0][1] and tablero[0][0] == tablero[0][2] and tablero[0][0] != ' '):
        return True
    elif (tablero[1][0] == tablero[1][1] and tablero[1][0] == tablero[1][2] and tablero[1][0] != ' '):
        return True
    elif (tablero[2][0] == tablero[2][1] and tablero[2][0] == tablero[2][2] and tablero[2][0] != ' '):
        return True
    elif (tablero[0][0] == tablero[1][0] and tablero[0][0] == tablero[2][0] and tablero[0][0] != ' '):
        return True
    elif (tablero[0][1] == tablero[1][1] and tablero[0][1] == tablero[2][1] and tablero[0][1] != ' '):
        return True
    elif (tablero[0][2] == tablero[1][2] and tablero[0][2] == tablero[2][2] and tablero[0][2] != ' '):
        return True
    elif (tablero[0][0] == tablero[1][1] and tablero[0][0] == tablero[2][2] and tablero[0][0] != ' '):
        return True
    elif (tablero[2][0] == tablero[1][1] and tablero[2][0] == tablero[0][2] and tablero[2][0] != ' '):
        return True
    else:
        return False


def comprobarEmpate(tablero):
    if (tablero[0][0] != ' ' and tablero[0][1] != ' ' and tablero[0][2] != ' ' and tablero[1][0] != ' ' and tablero[1][1] != ' ' and tablero[1][2] != ' ' and tablero[2][0] != ' ' and tablero[2][1] != ' ' and tablero[2][2] != ' '):
        return True
    else:
        return False


def cambiarTurno(turno):
    if (turno == 'O'):
        return 'X'
    else:
        return 'O'


def hacerMovimiento(tablero, turno):
    movimientoValido = False

    while not movimientoValido:
        columna = pedirNum('Columna: ')
        fila = pedirNum('Fila: ')
        movimientoValido = insertarMovimiento(
            tablero, columna-1, fila-1, turno)
        if (not movimientoValido):
            print('movimiento ilegal')


def movMaquina(tablero, turnoMaquina):

    if turnoMaquina == 'X':
        turnoHumano = 'O'
    else:
        turnoHumano = 'X'

    movRealizado = False

    # Comprobación si puede ganar
    for x in range(len(tablero)):
        for i in range(len(tablero)):
            if tablero[x][i] == turnoMaquina:
                movimientos = comprobarPosibleTresEnRaya(tablero, i, x, turnoMaquina)

    # Si puede ganar hará el movimiento y marcara movRealizado para ni siquiere buscar la posible derrota
    try:
        fila = movimientos[0]
        columna = movimientos[1]
        if tablero[fila][columna] == ' ':
            insertarMovimiento(tablero, columna, fila, turnoMaquina)
            movRealizado = True
    except:
        pass

    movRealizado2 = False

    if not movRealizado:
        for x in range(len(tablero)):
            for i in range(len(tablero)):
                if tablero[x][i] == turnoHumano:
                    movimientos = comprobarPosibleTresEnRaya(tablero, i, x, turnoHumano)
                    if x == 1 and i == 1 and movimientos[0] != 1 and movimientos[1] != 1:
                        insertarMovimiento(tablero, movimientos[1], movimientos[0], turnoMaquina)
                        movRealizado2 = True

        # Si hay una en el centro esa mandará
        if not movRealizado2:

            try:
                fila = movimientos[0]
                columna = movimientos[1]

                if tablero[fila][columna] == ' ':
                    insertarMovimiento(tablero, columna, fila, turnoMaquina)
                elif tablero[1][1] == ' ':
                    insertarMovimiento(tablero, 1, 1, turnoMaquina)
                elif tablero[0][0] == ' ' and tablero[2][0] == ' ' and tablero[0][2] == ' ' and tablero[2][2] == ' ':
                    numRandom = randint(0, 3)
                    if numRandom == 0:
                        insertarMovimiento(tablero, 0, 0, turnoMaquina)
                    elif numRandom == 1:
                        insertarMovimiento(tablero, 2, 0, turnoMaquina)
                    elif numRandom == 2:
                        insertarMovimiento(tablero, 0, 2, turnoMaquina)
                    else:
                        insertarMovimiento(tablero, 2, 2, turnoMaquina)
                else:
                    print('mov random')
                    movRandoms = movRandom(tablero)
                    insertarMovimiento(tablero, movRandoms[0], movRandoms[1], turnoMaquina)
                    
            except:
                movRandoms = movRandom(tablero)
                insertarMovimiento(tablero, movRandoms[0], movRandoms[1], turnoMaquina)
    
    return tablero

def contNumMensajes(mensajes, userId):
    cont = 0
    for mensaje in mensajes:
        if str(userId) == mensaje.message_create['sender_id']:
            cont += 1
    return cont

################################################################################### TRES EN RAYA METODOS #######################################################################

def comprobarUsuario(id):
    for usuario in USUARIOS_CON_PARTIDA:
        if usuario == id:
            return True

    return False

def comprobarUsuarioMensaje(id):
    for usuario in USUARIOS_MENSAJES_ENVIADOS:
        if usuario == id:
            return True

    return False

USUARIOS_MENSAJES_ENVIADOS = []

USUARIOS_CON_PARTIDA = []
USUARIOS_TABLEROS = {}
USUARIOS_TURNO = {}
USUARIOS_ULTIMO_MOV = {}
USUARIOS_EMPEZAR_ENVIADO = {}

auth = tweepy.OAuthHandler(secrets.API_KEY, secrets.API_SECRET_KEY)
auth.set_access_token(secrets.ACCES_TOKEN, secrets.ACCES_SECRET_TOKEN)

while True:
    # Hay que mirar cada 60 segundos porque sino la API te deniega el acceso (aún así lo hace)
    time.sleep(60)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    # Recojemos las menciones hacia el bot
    menciones = api.mentions_timeline()
    # Recojemos los mensajes directos
    mensajes = api.list_direct_messages()

    # Por cada mención que tengamos se envía un mensaje para jugar la partida o para seguirla
    for mencion in menciones:
        userId = mencion.user.id
        ultimoMensaje = '_'
        if not comprobarUsuario(userId):
            print('mensaje enviado a: ', userId)
            # Intentamos enviar un mensaje directo
            try:
                api.send_direct_message(userId, 'Bienvenido al Tic Tac Toe de Carlos\n\nPara empezar una partida sigue los siguiente pasos:\n\nSi quieres empezar tú escribe: \'empiezo yo\'\n\nSi quieres que empiece yo escribe: \'empieza tu\'\n\nSin comillas, muchas gracias y suerte :)\n\nComo sabes no funciono muy bien, si te equivocas moriré y mi creador tendrá que volver a ponerme en funcionamiento, intenta no equivocarte gracias <3')
            # Si no funciona el mensaje directo porque no me sigue le enviamos una mención
            except:
                if not comprobarUsuarioMensaje(userId):
                    api.update_status('@' + api.get_user(userId).screen_name + ' si no me sigues no te puedo enviar mensajes directos :(', mencion.id)
                    USUARIOS_MENSAJES_ENVIADOS.append(userId)
            USUARIOS_CON_PARTIDA.append(userId)
            USUARIOS_TABLEROS[userId] = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
            USUARIOS_TURNO[userId] = 'X'
            USUARIOS_EMPEZAR_ENVIADO[userId] = False
        else:
            for mensaje in mensajes:
                if str(userId) == mensaje.message_create['sender_id']:
                    ultimoMensaje = mensaje.message_create['message_data']['text']
                    break
        
            stringDeComp = 'empiezo yo | empieza tu'

            if ultimoMensaje in stringDeComp or ('columna' in ultimoMensaje and 'fila' in ultimoMensaje):
                
                if ultimoMensaje == 'empiezo yo' or ultimoMensaje == 'empieza tu':
                    print('crear partida')
                    print(ultimoMensaje)
                    if ultimoMensaje == 'empiezo yo':
                        print('empieza el usuario')
                        enviado = USUARIOS_EMPEZAR_ENVIADO.get(userId)
                        if not enviado:
                            tablero = USUARIOS_TABLEROS.get(userId)
                            strMostrarTablero = mostrarTablero(tablero)
                            # Recupero el turno de la partida
                            turno = USUARIOS_TURNO.get(userId)
                            api.send_direct_message(userId, '¿Entonces empiezas tú?\nPerfecto, ahora me tendrás que escribir donde quieres hacer el movimiento de la siguiente manera:\n\ncolumna: X\nfila: X\n\nEscribiendo en la X el número que quieres poner tu movimiento\n\n' + strMostrarTablero)
                            USUARIOS_EMPEZAR_ENVIADO[userId] = True
                    else:
                        print('empieza el bot')
                        # Recupero el turno de la partida
                        turno = USUARIOS_TURNO.get(userId)
                        if turno == 'X':
                            # Recupero el tablero del usuario
                            tablero = USUARIOS_TABLEROS.get(userId)
                            # Hace mov la máquina
                            tablero = movMaquina(tablero, turno)
                            # Guardo el tablero para guardar la partida
                            USUARIOS_TABLEROS[userId] = tablero
                            strMostrarTablero = mostrarTablero(tablero)
                            api.send_direct_message(userId, '¿Entonces empiezo yo?\nPerfecto, ahora me tendrás que escribir donde quieres hacer el movimiento de la siguiente manera:\n\ncolumna: X\nfila: X\n\nEscribiendo en la X el número que quieres poner tu movimiento\n\nMi movimiento es el siguiente:\n\n' + strMostrarTablero + '\n\nAhora te toca hacer un movimiento a ti.')
                            turno = cambiarTurno(turno)
                            USUARIOS_TURNO[userId] = turno
                        else:
                            print('el turno no ha cambiado, esperando respuesta')
                else:
                    ultMov = USUARIOS_ULTIMO_MOV.get(userId)
                    if ultMov != ultimoMensaje:
                        print('seguir partida')
                        print(ultimoMensaje)
                        USUARIOS_ULTIMO_MOV[userId] = ultimoMensaje
                        entradaSep = ultimoMensaje.split("\n")
                        print('entradaSeparada: ', entradaSep)
                        # TODO Comprobar si son numeros
                        columna = entradaSep[0][-1:]
                        fila = entradaSep[1][-1:]
                        # Recupero el turno de la partida
                        turno = USUARIOS_TURNO.get(userId)
                        # Recupero el turno de la partida
                        print('movCol: ', columna)
                        print('movFila: ', fila)
                        turno = USUARIOS_TURNO.get(userId)
                        # Recupero el tablero del usuario
                        tablero = USUARIOS_TABLEROS.get(userId)
                        respuesta = insertarMovimiento(tablero, int(columna)-1, int(fila)-1, turno)
                        if respuesta == False:
                            print('movimiento inválido')
                            api.send_direct_message(userId, 'Movimiento inválido, vuelve a introducir tu movimiento')
                        else:
                            print('mov válido')
                            tablero = respuesta[1]
                            turno = cambiarTurno(turno)
                            USUARIOS_TURNO[userId] = turno
                            USUARIOS_TABLEROS[userId] = tablero
                            comprobacion = comprobarTresEnRaya(tablero)
                            empate = comprobarEmpate(tablero)
                            if comprobacion:
                                print('partida acabada')
                                api.send_direct_message(userId, '¡Felicidades, has ganado!')
                            elif empate:
                                print('partida empatada')
                                api.send_direct_message(userId, 'Vaya...\nHemos quedado empate :/')
                            else:
                                print('partida sigue')
                                strMostrarTablero = mostrarTablero(tablero)
                                api.send_direct_message(userId, 'Buen movimiento\n\n' + strMostrarTablero)
                                # El bot tiene que hacer el movimiento
                                print('movMaquina después del suyo')
                                turno = USUARIOS_TURNO.get(userId)
                                tablero = movMaquina(tablero, turno)
                                strMostrarTablero = mostrarTablero(tablero)
                                USUARIOS_TABLEROS[userId] = tablero
                                turno = cambiarTurno(turno)
                                USUARIOS_TURNO[userId] = turno
                                api.send_direct_message(userId, 'Mi movimiento es el siguiente:\n\n' + strMostrarTablero)
                                comprobacion = comprobarTresEnRaya(tablero)
                                empate = comprobarEmpate(tablero)
                                if comprobacion:
                                    print('partida acabada')
                                    api.send_direct_message(userId, 'Vaya...\nParece que te he ganado xD')
                                elif empate:
                                    print('partida empate')
                                    api.send_direct_message(userId, 'Vaya...\nHemos quedado empate :/')
                    else:
                        print('esperando respuesta')
                        print(ultimoMensaje)
                    
            else:
                if ultimoMensaje == '_':
                    print('no hay respuesta')
                else:
                    print(ultimoMensaje)
                    print('Entrada incorrecta, vuelve a introducir tu opción')