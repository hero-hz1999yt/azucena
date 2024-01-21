#!/usr/bin/python3
#
# +---------------------------------------------------------------+
# |   █████╗ ███████╗██╗   ██╗ ██████╗███████╗███╗   ██╗ █████╗   |
# |  ██╔══██╗╚══███╔╝██║   ██║██╔════╝██╔════╝████╗  ██║██╔══██╗  |
# |  ███████║  ███╔╝ ██║   ██║██║     █████╗  ██╔██╗ ██║███████║  |
# |  ██╔══██║ ███╔╝  ██║   ██║██║     ██╔══╝  ██║╚██╗██║██╔══██║  |
# |  ██║  ██║███████╗╚██████╔╝╚██████╗███████╗██║ ╚████║██║  ██║  |
# |  ╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝  |
# +-------------------AUTHOR BY: HERO_HZ1999YT--------------------+
#
# -- IMPORTS --
import gi
gi.require_version('Notify', '0.7')    
gi.require_version('Gtk', '3.0')       

from gi.repository import Notify    
from gi.repository import Gtk       
from tkinter import messagebox      
from io import open                 
from git import Repo                
from os import path, environ, listdir, mkdir       
from datetime import datetime       
from time import sleep              
from re import sub, match           
from random import randrange        
from shutil import rmtree           
from sys import exit                
from subprocess import check_output 
from subprocess import Popen

# -- CONSTANTES --
DIRECTORIO_RAIZ = "/home/" + environ.get('USER') + "/.azucena"
DIRECTORIO_DE_SONIDOS = "/home/" + environ.get('USER') + "/.azucena/sonidos"
PARAMETROS_DE_CONFIGURACION = ["AZUCENA","APARIENCIA", "URGENCIA", "MOSTRAR", "OCULTAR", "APODO", "MMENSAJE", "TMENSAJE", "NMENSAJE", "MAMENSAJE", "TIMBRE"]
ARCHIVO_DE_CONFIGURACION = "/home/" + environ.get('USER') + "/.azucena/azucena.azc"
NOMBRE_DE_AZUCENA = "Azucena"
APODO_DE_AZUCENA = "Azucena"
MOSTRAR_NOTIFICACION = 0
OCULTAR_NOTIFICACION = 10
URGENCIA_NOTIFICACION = 1
MENSAJE_NOTIFICACION = "no deberias de ver este mensaje xd" 
TITULO_NOTIFICACION = "no deberias de ver este titulo xd"
ICONO_NOTIFICACION = "dialog-information"
HORA_DEL_DIA = datetime.now().hour
APARIENCIA_NOTIFICACION = "EMOTICONES"
LISTA_DE_APODOS = [environ.get('USER')]
LISTA_DE_MENSAJES = ["Que tengas un increible dia, tu puedes !!!!"] 
LISTA_DE_ESTADOS = ["ENAMORADA"] 
NUMERO_RANDOM = 0 
COLOR_TERMINAL_VERDE = "\033[92m" 
COLOR_TERMINAL_AMARILLO = "\033[93m"
COLOR_TERMINAL_ROJO = "\033[91m"
RESET_COLOR_TERMINAL = "\033[0m"
TIPOS_DE_APARIENCIAS = ["POR_DEFECTO", "MI_AZUCENA", "EMOTICONES", "ZOMBIE", "AZUCENA"]
TIPOS_DE_URGENCIAS = ["BAJA", "NORMAL", "CRITICA"]
TIPOS_DE_ESTADOS = ["FELIZ", "ENOJADA", "SOÑOLIENTA", "CELOSA", "RISUEÑA", "TRISTE", "ENAMORADA", "CALIENTE", "ASUSTADA"] 
ESTADO_MENSAJE = "ENAMORADA"
CANTIDAD_DE_EMOTICONES = 0
DIRECTORIO_DE_ICONOS = "/home/" + environ.get('USER') + "/.azucena/iconos"
DIRECTORIO_DE_EMOTICONES = "/home/" + environ.get('USER') + "/.azucena/emoticones"
TIMBRE_NOTIFICACION = "TRUE"
DICCIONARIO = [ 
                "Hola",                                                                                                         # 0                                                                                                                                                                                         
                "Ups, demasiadas notificaciones en pantalla espera un poco....",                                                # 1
                "Hola baby, tengo una noticia!",                                                                                # 2
                "Ups, este boton sigue en construccion, pero pronto estara listo 7w7",                                          # 3
                "Configuración",                                                                                                # 4
                "Cerrar",                                                                                                       # 5
                "Cerraron a azucena :(",                                                                                        # 6
                "Me pongo súper roja cuando me dices Chaparra",                                                                 # 7
                "A mi me encanta el color morado",                                                                              # 8
                "No me gusta que me digan Guadalupe",                                                                           # 9
                "Falta la carpeta principal para que el programa pueda trabajar\nRuta: /home/nombre_usuario/.azucena",          # 10
                "Hola baby, hubo un error en el programa!",                                                                     # 11
                "Falta el archivo que contiene los creditos de este programa\nRuta: /home/nombre_usuario/.azucena/creditos.azc" # 12                                                                                                 
        ]
DIRECTORIO_BIN_LOCAL="/home/" + environ.get('USER') + "/.local/bin"

# -- FUNCIONES --
def existeElDirectorioRaiz():
    if not path.exists(DIRECTORIO_RAIZ):
        messagebox.showerror(DICCIONARIO[11], DICCIONARIO[10])
        exit()

def existeElArchivoCreditos():
    if not path.exists(DIRECTORIO_RAIZ + "/creditos.azc"):
        messagebox.showerror(DICCIONARIO[11], DICCIONARIO[12])
        exit()

def existeElArchivoDeConfiguracion(): 
    if not path.exists(ARCHIVO_DE_CONFIGURACION): 
        file = open (ARCHIVO_DE_CONFIGURACION, "w") 
        file.write("#\n" 
                + "#  █████╗ ███████╗██╗   ██╗ ██████╗███████╗███╗   ██╗ █████╗ \n"         
                + "# ██╔══██╗╚══███╔╝██║   ██║██╔════╝██╔════╝████╗  ██║██╔══██╗\n"         
                + "# ███████║  ███╔╝ ██║   ██║██║     █████╗  ██╔██╗ ██║███████║\n"         
                + "# ██╔══██║ ███╔╝  ██║   ██║██║     ██╔══╝  ██║╚██╗██║██╔══██║\n"         
                + "# ██║  ██║███████╗╚██████╔╝╚██████╗███████╗██║ ╚████║██║  ██║\n"         
                + "# ╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝\n"         
                + "# -----------------AUTHOR BY: HERO_HZ1999YT------------------\n"         
                + "# %%%%%%%%%%%%[ARCHIVO DE CONFIGURACION AZUCENA]%%%%%%%%%%%%%\n"         
                + "#\n"
                + "# ======================== MIS AJUSTES GENERALES ========================\n"
                + ""+PARAMETROS_DE_CONFIGURACION[0]+"=\"Azucena\";\n"                                               # AÑADIMOS UN APODO AL PROGRAMA                                    
                + ""+PARAMETROS_DE_CONFIGURACION[1]+"="+TIPOS_DE_APARIENCIAS[0]+";\n"                               # AÑADIMOS UNA APARIENCIA A LA NOTIFICACION
                + ""+PARAMETROS_DE_CONFIGURACION[2]+"="+TIPOS_DE_URGENCIAS[0]+";\n"                                 # AÑADIMOS LA URGENCIA DE LA NOTIFICACION
                + ""+PARAMETROS_DE_CONFIGURACION[3]+"=0;\n"                                                         # AÑADIMOS EL TIEMPO EN MOSTRAR LA NOTIFICACION
                + ""+PARAMETROS_DE_CONFIGURACION[4]+"=20;\n"                                                        # AÑADIMOS EL TIEMPO EN OCULTAR LA NOTIFICACION
                + ""+PARAMETROS_DE_CONFIGURACION[10]+"=TRUE;\n"                                                     # HABILITAMOS EL TIMBRE DE LA NOTIFICACION
                + "\n"
                + "# ============================== MIS APODOS =============================\n"
                + ""+PARAMETROS_DE_CONFIGURACION[5]+"=\""+environ.get('USER')+"\";\n"                               # AÑADIMOS UN APODO AL USUARIO (EL NOMBRE DE USUARIO)
                + "\n"
                + "# ======================= MENSAJES PARA LA MAÑANA =======================\n"
                + ""+PARAMETROS_DE_CONFIGURACION[6]+"-"+TIPOS_DE_ESTADOS[0]+"=\"Que tengas un bonito dia\";\n"      # AÑADIMOS UN MENSAJE PARA LA MAÑANA
                + "\n"
                + "# ======================== MENSAJES PARA LA TARDE =======================\n"
                + ""+PARAMETROS_DE_CONFIGURACION[7]+"-"+TIPOS_DE_ESTADOS[0]+"=\"Que tengas una bonita tarde\";\n"   # AÑADIMOS UN MENSAJE PARA LA TARDE
                + "\n"
                + "# ======================== MENSAJES PARA LA NOCHE =======================\n"
                + ""+PARAMETROS_DE_CONFIGURACION[8]+"-"+TIPOS_DE_ESTADOS[0]+"=\"Que tengas una bonita noche\";\n"   # AÑADIMOS UN MENSAJE PARA LA NOCHE
                + "\n"
                + "# ====================== MENSAJES PARA LA MADRUGADA ======================\n"
                + ""+PARAMETROS_DE_CONFIGURACION[9]+"-"+TIPOS_DE_ESTADOS[0]+"=\"Que tengas dulces sueños\";\n"      # AÑADIMOS UN MENSAJE PARA LA MADRUGADA
        )
        file.close() 

def leerArchivoDeConfiguracion(): 
    global APODO_DE_AZUCENA 
    global APARIENCIA_NOTIFICACION 
    global URGENCIA_NOTIFICACION 
    global MOSTRAR_NOTIFICACION 
    global OCULTAR_NOTIFICACION 
    global LISTA_DE_APODOS 
    global LISTA_DE_MENSAJES 
    global LISTA_DE_ESTADOS 
    global TIMBRE_NOTIFICACION

    with open (ARCHIVO_DE_CONFIGURACION) as archivo: 
        for linea in archivo: 
            if not linea.startswith("#"):
                # APODO DEL PROGRAMA
                if match("^"+PARAMETROS_DE_CONFIGURACION[0]+"=\"[!-ÿ\\s]+\";\\s+$", linea): 
                    linea = sub("^"+PARAMETROS_DE_CONFIGURACION[0]+"=\"", "", linea)  
                    linea = sub("\";\\s+$", "", linea)               
                    linea = sub("\n", "", linea)                    
                    APODO_DE_AZUCENA = linea 

                # APARIENCIA DE LA NOTIFICACION
                if match("^"+PARAMETROS_DE_CONFIGURACION[1]+"=("+TIPOS_DE_APARIENCIAS[0]+"|"+TIPOS_DE_APARIENCIAS[1]+"|"+TIPOS_DE_APARIENCIAS[2]+"|"+TIPOS_DE_APARIENCIAS[3]+"|"+TIPOS_DE_APARIENCIAS[4]+");\\s+$", linea): 
                    linea = sub("^"+PARAMETROS_DE_CONFIGURACION[1]+"=", "", linea)    
                    linea = sub(";\\s+$", "", linea)                 
                    linea = sub("\n", "", linea)                
                    APARIENCIA_NOTIFICACION = linea 

                # URGENCIA DE LA NOTIFICACION
                if match("^"+PARAMETROS_DE_CONFIGURACION[2]+"=("+TIPOS_DE_URGENCIAS[0]+"|"+TIPOS_DE_URGENCIAS[1]+"|"+TIPOS_DE_URGENCIAS[2]+");\\s+$", linea): 
                    linea = sub("^"+PARAMETROS_DE_CONFIGURACION[2]+"=", "", linea)    
                    linea = sub(";\\s+$", "", linea)                 
                    linea = sub("\n", "", linea)                     
                    if   linea == TIPOS_DE_URGENCIAS[0]: # URGENCIA BAJA
                        URGENCIA_NOTIFICACION = 0
                    elif linea == TIPOS_DE_URGENCIAS[1]: # URGENCIA NORMAL
                        URGENCIA_NOTIFICACION = 1
                    elif linea == TIPOS_DE_URGENCIAS[2]: # URGENCIA CRITICA
                        URGENCIA_NOTIFICACION = 2

                # TIEMPO EN MOSTRAR LA NOTIFICACION
                if match("^"+PARAMETROS_DE_CONFIGURACION[3]+"=[0-9]+;\\s+$", linea): 
                    linea = sub("^"+PARAMETROS_DE_CONFIGURACION[3]+"=", "", linea)    
                    linea = sub(";\\s+$", "", linea)                 
                    linea = sub("\n", "", linea)                     
                    MOSTRAR_NOTIFICACION = linea 

                # TIEMPO EN OCULTAR LA NOTIFICACION
                if match("^"+PARAMETROS_DE_CONFIGURACION[4]+"=[0-9]+;\\s+$", linea): 
                    linea = sub("^"+PARAMETROS_DE_CONFIGURACION[4]+"=", "", linea)    
                    linea = sub(";\\s+$", "", linea)                 
                    linea = sub("\n", "", linea)                     
                    OCULTAR_NOTIFICACION = linea 

                # TIMBRE DE LA NOTIFICACION
                if match("^"+PARAMETROS_DE_CONFIGURACION[10]+"=(TRUE|FALSE);\\s+$", linea): 
                    linea = sub("^"+PARAMETROS_DE_CONFIGURACION[10]+"=", "", linea)    
                    linea = sub(";\\s+$", "", linea)                 
                    linea = sub("\n", "", linea)                     
                    TIMBRE_NOTIFICACION = linea 

                # MIS APODOS CONFIGURADOS
                if match("^"+PARAMETROS_DE_CONFIGURACION[5]+"=\"[!-ÿ\\s]+\";\\s+$", linea):
                    linea = sub("^"+PARAMETROS_DE_CONFIGURACION[5]+"=\"", "", linea) 
                    linea = sub("\";\\s+$", "", linea)               
                    linea = sub("\n", "", linea)                     
                    LISTA_DE_APODOS.append(linea) 

                # OBTENEMOS LOS MENSAJES DE LA MAÑANA
                if HORA_DEL_DIA >= 7 and HORA_DEL_DIA <= 11: 
                    if match("^"+PARAMETROS_DE_CONFIGURACION[6]+"-("+TIPOS_DE_ESTADOS[0]+"|"+TIPOS_DE_ESTADOS[1]+"|"+TIPOS_DE_ESTADOS[2]+"|"+TIPOS_DE_ESTADOS[3]+"|"+TIPOS_DE_ESTADOS[4]+"|"+TIPOS_DE_ESTADOS[5]+"|"+TIPOS_DE_ESTADOS[6]+"|"+TIPOS_DE_ESTADOS[7]+"|"+TIPOS_DE_ESTADOS[8]+")=\"[!-ÿ\\s]+\";\\s+$", linea): 
                        
                        mensaje = linea 
                        mensaje = sub("^"+PARAMETROS_DE_CONFIGURACION[6]+"-("+TIPOS_DE_ESTADOS[0]+"|"+TIPOS_DE_ESTADOS[1]+"|"+TIPOS_DE_ESTADOS[2]+"|"+TIPOS_DE_ESTADOS[3]+"|"+TIPOS_DE_ESTADOS[4]+"|"+TIPOS_DE_ESTADOS[5]+"|"+TIPOS_DE_ESTADOS[6]+"|"+TIPOS_DE_ESTADOS[7]+"|"+TIPOS_DE_ESTADOS[8]+")=\"", "", mensaje) 
                        mensaje = sub("\";\\s+$", "", mensaje) 
                        mensaje = sub("\n", "", mensaje) 
                        
                        estado = linea 
                        estado = sub("^"+PARAMETROS_DE_CONFIGURACION[6]+"-", "", estado)  
                        estado = sub("=\"[!-ÿ\\s]+\";\\s+$", "", estado) 
                        estado = sub("\n", "", estado)                   
                        LISTA_DE_MENSAJES.append(mensaje) 
                        LISTA_DE_ESTADOS.append(estado) 
                
                # OBTENEMOS LOS MENSAJES DE LA TARDE
                if HORA_DEL_DIA >= 12 and HORA_DEL_DIA <= 18: 
                    if match("^"+PARAMETROS_DE_CONFIGURACION[7]+"-("+TIPOS_DE_ESTADOS[0]+"|"+TIPOS_DE_ESTADOS[1]+"|"+TIPOS_DE_ESTADOS[2]+"|"+TIPOS_DE_ESTADOS[3]+"|"+TIPOS_DE_ESTADOS[4]+"|"+TIPOS_DE_ESTADOS[5]+"|"+TIPOS_DE_ESTADOS[6]+"|"+TIPOS_DE_ESTADOS[7]+"|"+TIPOS_DE_ESTADOS[8]+")=\"[!-ÿ\\s]+\";\\s+$", linea): 
                        
                        mensaje = linea 
                        mensaje = sub("^"+PARAMETROS_DE_CONFIGURACION[7]+"-("+TIPOS_DE_ESTADOS[0]+"|"+TIPOS_DE_ESTADOS[1]+"|"+TIPOS_DE_ESTADOS[2]+"|"+TIPOS_DE_ESTADOS[3]+"|"+TIPOS_DE_ESTADOS[4]+"|"+TIPOS_DE_ESTADOS[5]+"|"+TIPOS_DE_ESTADOS[6]+"|"+TIPOS_DE_ESTADOS[7]+"|"+TIPOS_DE_ESTADOS[8]+")=\"", "", mensaje) 
                        mensaje = sub("\";\\s+$", "", mensaje) 
                        mensaje = sub("\n", "", mensaje) 
                        
                        estado = linea 
                        estado = sub("^"+PARAMETROS_DE_CONFIGURACION[7]+"-", "", estado)  
                        estado = sub("=\"[!-ÿ\\s]+\";\\s+$", "", estado) 
                        estado = sub("\n", "", estado)                   
                        LISTA_DE_MENSAJES.append(mensaje) 
                        LISTA_DE_ESTADOS.append(estado)

                # OBTENEMOS LOS MENSAJES DE LA NOCHE
                if HORA_DEL_DIA >= 19 and HORA_DEL_DIA <= 23: 
                    if match("^"+PARAMETROS_DE_CONFIGURACION[8]+"-("+TIPOS_DE_ESTADOS[0]+"|"+TIPOS_DE_ESTADOS[1]+"|"+TIPOS_DE_ESTADOS[2]+"|"+TIPOS_DE_ESTADOS[3]+"|"+TIPOS_DE_ESTADOS[4]+"|"+TIPOS_DE_ESTADOS[5]+"|"+TIPOS_DE_ESTADOS[6]+"|"+TIPOS_DE_ESTADOS[7]+"|"+TIPOS_DE_ESTADOS[8]+")=\"[!-ÿ\\s]+\";\\s+$", linea): 
                        
                        mensaje = linea 
                        mensaje = sub("^"+PARAMETROS_DE_CONFIGURACION[8]+"-("+TIPOS_DE_ESTADOS[0]+"|"+TIPOS_DE_ESTADOS[1]+"|"+TIPOS_DE_ESTADOS[2]+"|"+TIPOS_DE_ESTADOS[3]+"|"+TIPOS_DE_ESTADOS[4]+"|"+TIPOS_DE_ESTADOS[5]+"|"+TIPOS_DE_ESTADOS[6]+"|"+TIPOS_DE_ESTADOS[7]+"|"+TIPOS_DE_ESTADOS[8]+")=\"", "", mensaje) 
                        mensaje = sub("\";\\s+$", "", mensaje) 
                        mensaje = sub("\n", "", mensaje) 
                        
                        estado = linea 
                        estado = sub("^"+PARAMETROS_DE_CONFIGURACION[8]+"-", "", estado) 
                        estado = sub("=\"[!-ÿ\\s]+\";\\s+$", "", estado) 
                        estado = sub("\n", "", estado)                   
                        LISTA_DE_MENSAJES.append(mensaje) 
                        LISTA_DE_ESTADOS.append(estado) 

                # OBTENEMOS LOS MENSAJES DE LA MADRUGADA
                if HORA_DEL_DIA >= 0 and HORA_DEL_DIA <= 6: 
                    if match("^"+PARAMETROS_DE_CONFIGURACION[9]+"-("+TIPOS_DE_ESTADOS[0]+"|"+TIPOS_DE_ESTADOS[1]+"|"+TIPOS_DE_ESTADOS[2]+"|"+TIPOS_DE_ESTADOS[3]+"|"+TIPOS_DE_ESTADOS[4]+"|"+TIPOS_DE_ESTADOS[5]+"|"+TIPOS_DE_ESTADOS[6]+"|"+TIPOS_DE_ESTADOS[7]+"|"+TIPOS_DE_ESTADOS[8]+")=\"[!-ÿ\\s]+\";\\s+$", linea): 
                        
                        mensaje = linea 
                        mensaje = sub("^"+PARAMETROS_DE_CONFIGURACION[9]+"-("+TIPOS_DE_ESTADOS[0]+"|"+TIPOS_DE_ESTADOS[1]+"|"+TIPOS_DE_ESTADOS[2]+"|"+TIPOS_DE_ESTADOS[3]+"|"+TIPOS_DE_ESTADOS[4]+"|"+TIPOS_DE_ESTADOS[5]+"|"+TIPOS_DE_ESTADOS[6]+"|"+TIPOS_DE_ESTADOS[7]+"|"+TIPOS_DE_ESTADOS[8]+")=\"", "", mensaje) 
                        mensaje = sub("\";\\s+$", "", mensaje) 
                        mensaje = sub("\n", "", mensaje) 
                        
                        estado = linea 
                        estado = sub("^"+PARAMETROS_DE_CONFIGURACION[9]+"-", "", estado)  
                        estado = sub("=\"[!-ÿ\\s]+\";\\s+$", "", estado) 
                        estado = sub("\n", "", estado)                  
                        LISTA_DE_MENSAJES.append(mensaje) 
                        LISTA_DE_ESTADOS.append(estado)
        
def configuracion(*args): 
    check_output("xdg-open /home/"+environ.get('USER')+"/.azucena/azucena.azc", shell=True)

def cerrar(*args):
    Notify.uninit() 
    Gtk.main_quit() 

# -- INVOCAMOS LAS FUNCIONES --
existeElDirectorioRaiz()   
existeElArchivoDeConfiguracion()      
leerArchivoDeConfiguracion()
existeElArchivoCreditos()

# SI LAS LISTAS TIENEN MAS DE UN VALOR, REMOVEMOS EL CONFIGURADO POR EL PROGRAMA
if LISTA_DE_APODOS.__len__() > 1: 
    LISTA_DE_APODOS.__delitem__(0) 

if LISTA_DE_MENSAJES.__len__() > 1: 
    LISTA_DE_MENSAJES.__delitem__(0) 

if LISTA_DE_ESTADOS.__len__() > 1: 
    LISTA_DE_ESTADOS.__delitem__(0)

NUMERO_RANDOM = randrange(0, LISTA_DE_APODOS.__len__())
TITULO_NOTIFICACION = DICCIONARIO[0] + " " + LISTA_DE_APODOS[NUMERO_RANDOM]
# -- ESTE APARTADO CONTIENE ALGUNOS HUEVOS DE PASCUA --
if "erik" in TITULO_NOTIFICACION.lower():
    TITULO_NOTIFICACION = DICCIONARIO[0] + " Mi Eriksin <3"
elif "hero-hz1999yt" in TITULO_NOTIFICACION.lower() or "alberto" in TITULO_NOTIFICACION.lower():
    TITULO_NOTIFICACION = DICCIONARIO[0] + " Mi Alberto <3"

NUMERO_RANDOM = randrange(0, LISTA_DE_MENSAJES.__len__()) 
MENSAJE_NOTIFICACION = LISTA_DE_MENSAJES[NUMERO_RANDOM] 
ESTADO_MENSAJE = LISTA_DE_ESTADOS[NUMERO_RANDOM] 

# APARIENCIA POR DEFECTO
if APARIENCIA_NOTIFICACION == TIPOS_DE_APARIENCIAS[0]: 
    if path.exists(DIRECTORIO_DE_ICONOS) and path.exists(DIRECTORIO_DE_ICONOS + "/por_defecto.png"): 
        ICONO_NOTIFICACION = DIRECTORIO_DE_ICONOS + "/por_defecto.png" 
    else: 
        if path.exists(DIRECTORIO_DE_ICONOS):   
            rmtree(DIRECTORIO_DE_ICONOS)    
        try: 
            repo = Repo.clone_from("https://github.com/hero-hz1999yt/iconos.git", DIRECTORIO_RAIZ + "/iconos") 
            ICONO_NOTIFICACION = DIRECTORIO_DE_ICONOS + "/por_defecto.png" 
        except: 
            ICONO_NOTIFICACION = "dialog-information" 

# APARIENCIA MI AZUCENA
elif APARIENCIA_NOTIFICACION == TIPOS_DE_APARIENCIAS[1]: 
    if path.exists(DIRECTORIO_RAIZ + "/mi-azucena.png"): 
        ICONO_NOTIFICACION = DIRECTORIO_RAIZ + "/mi-azucena.png" 
    elif path.exists(DIRECTORIO_RAIZ + "/mi-azucena.jpg"): 
        ICONO_NOTIFICACION = DIRECTORIO_RAIZ + "/mi-azucena.jpg" 
    elif path.exists(DIRECTORIO_RAIZ + "/mi-azucena.png") and path.exists(DIRECTORIO_RAIZ + "/mi-azucena.jpg"): 
        ICONO_NOTIFICACION = DIRECTORIO_RAIZ + "/mi-azucena.png" 
    else: 
        ICONO_NOTIFICACION = "dialog-information" 

# APARIENCIA EMOTICONES
elif APARIENCIA_NOTIFICACION == TIPOS_DE_APARIENCIAS[2]:  
        archivos = listdir(DIRECTORIO_DE_EMOTICONES)
        for archivo in archivos:
            if match("^"+ESTADO_MENSAJE+"[0-9]+.png$", archivo):
                CANTIDAD_DE_EMOTICONES += 1

        NUMERO_RANDOM = randrange(1, CANTIDAD_DE_EMOTICONES + 1) 
        if path.exists(DIRECTORIO_DE_EMOTICONES) and path.exists(DIRECTORIO_DE_EMOTICONES + "/" + ESTADO_MENSAJE + str(NUMERO_RANDOM) + ".png"): 
            ICONO_NOTIFICACION = DIRECTORIO_DE_EMOTICONES + "/" + ESTADO_MENSAJE + str(NUMERO_RANDOM) + ".png" 
        else: 
            if path.exists(DIRECTORIO_DE_EMOTICONES):   
                rmtree(DIRECTORIO_DE_EMOTICONES)    
            try: 
                repo = Repo.clone_from("https://github.com/hero-hz1999yt/emoticones.git", DIRECTORIO_RAIZ + "/emoticones") 
                ICONO_NOTIFICACION = DIRECTORIO_DE_EMOTICONES + "/" + ESTADO_MENSAJE + str(NUMERO_RANDOM) + ".png" 
            except: 
                ICONO_NOTIFICACION = "dialog-information"

# APARIENCIA ZOMBIE
elif APARIENCIA_NOTIFICACION == TIPOS_DE_APARIENCIAS[3]: 
    if path.exists(DIRECTORIO_DE_ICONOS) and path.exists(DIRECTORIO_DE_ICONOS + "/zombie.png"): 
        ICONO_NOTIFICACION = DIRECTORIO_DE_ICONOS + "/zombie.png" 
    else: 
        if path.exists(DIRECTORIO_DE_ICONOS):   
            rmtree(DIRECTORIO_DE_ICONOS)    
        try: 
            repo = Repo.clone_from("https://github.com/hero-hz1999yt/iconos.git", DIRECTORIO_RAIZ + "/iconos") 
            ICONO_NOTIFICACION = DIRECTORIO_DE_ICONOS + "/zombie.png" 
        except: 
            ICONO_NOTIFICACION = "dialog-information" 

# APARIENCIA AZUCENA
elif APARIENCIA_NOTIFICACION == TIPOS_DE_APARIENCIAS[4]: 
    if path.exists(DIRECTORIO_DE_ICONOS) and path.exists(DIRECTORIO_DE_ICONOS + "/azucena.png"): 
        ICONO_NOTIFICACION = DIRECTORIO_DE_ICONOS + "/azucena.png" 
    else: 
        if path.exists(DIRECTORIO_DE_ICONOS):   
            rmtree(DIRECTORIO_DE_ICONOS)   
        try:
            repo = Repo.clone_from("https://github.com/hero-hz1999yt/iconos.git", DIRECTORIO_RAIZ + "/iconos")
            ICONO_NOTIFICACION = DIRECTORIO_DE_ICONOS + "/azucena.png" 
        except: 
            ICONO_NOTIFICACION = "dialog-information" 

# -- PARAMETROS DE LA NOTIFICIACION --
Notify.init(NOMBRE_DE_AZUCENA) 
notificacion = Notify.Notification.new(TITULO_NOTIFICACION, MENSAJE_NOTIFICACION, ICONO_NOTIFICACION) 
notificacion.set_urgency(URGENCIA_NOTIFICACION) 
notificacion.set_timeout(int(OCULTAR_NOTIFICACION) * 1000) 
notificacion.set_app_name(APODO_DE_AZUCENA) 
notificacion.set_category("email.arrived") 
notificacion.connect("closed", cerrar) 
notificacion.add_action("action_click", DICCIONARIO[4], configuracion, None)
notificacion.add_action("action_click1", DICCIONARIO[5], cerrar, None)

# -- ESTE APARTADO CONTIENE ALGUNOS HUEVOS DE PASCUA --
if APARIENCIA_NOTIFICACION == TIPOS_DE_APARIENCIAS[2]:
    if "chaparra" in APODO_DE_AZUCENA.lower(): 
        ICONO_NOTIFICACION = DIRECTORIO_DE_EMOTICONES + "/ENAMORADA6.png" 
        notificacion.update(TITULO_NOTIFICACION, DICCIONARIO[7], ICONO_NOTIFICACION) 

    if "guadalupe" in APODO_DE_AZUCENA.lower() or "lupita" in APODO_DE_AZUCENA.lower() or "lupe" in APODO_DE_AZUCENA.lower(): 
        ICONO_NOTIFICACION = DIRECTORIO_DE_EMOTICONES + "/ENOJADA1.png" 
        notificacion.update(TITULO_NOTIFICACION, DICCIONARIO[9], ICONO_NOTIFICACION) 

    if "morado" in MENSAJE_NOTIFICACION.lower(): 
        ICONO_NOTIFICACION = DIRECTORIO_DE_EMOTICONES + "/ENAMORADA6.png" 
        notificacion.update(TITULO_NOTIFICACION, DICCIONARIO[8], ICONO_NOTIFICACION)

sleep(int(MOSTRAR_NOTIFICACION))
try:
    notificacion.show()
except Exception as error: 
    messagebox.showerror(DICCIONARIO[11], str(error))
    exit()

if TIMBRE_NOTIFICACION== "TRUE" and path.exists(DIRECTORIO_DE_SONIDOS + "/notificacion.mp3"):
    audio = Popen("mpg123 "+DIRECTORIO_DE_SONIDOS + "/notificacion.mp3", shell=True)

# -- MAIN LOOP --
try: 
    Gtk.main()
except: 
    print(COLOR_TERMINAL_VERDE + "\n" + DICCIONARIO[6] + RESET_COLOR_TERMINAL) 