#!/bin/bash 
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
# -- CONSTANTES --
USUARIO=$USER
DIRECTORIO="/home/$USUARIO/.azucena"
COLOR_TERMINAL_ROJO='\033[0;31m'
COLOR_TERMINAL_NEGRO='\033[0;30m'
COLOR_TERMINAL_VERDE='\033[0;32m'
COLOR_TERMINAL_AMARILLO='\033[0;33m'
COLOR_TERMINAL_AZUL='\033[0;34m'
COLOR_TERMINAL_PURPURA='\033[0;35m'
COLOR_TERMINAL_CYAN='\033[0;36m'
COLOR_TERMINAL_BLANCO='\033[0;37m'
RESETEAR_COLOR='\033[0m'
ARCHIVO_DESKTOP="/home/$USUARIO/.config/autostart/azucena.desktop"
EJECUTABLE_TERMINAL="/home/$USUARIO/.local/bin/azucena"
DIRECTORIO_CLONADO_GIT="/home/$USUARIO/azucena"
DIRECTORIO_GITHUB="/home/$USUARIO/.azucena/.git"
DIRECTORIO_AUTOSTART="/home/$USUARIO/.config/autostart"
DIRECTORIO_BIN="/home/$USUARIO/.local/bin"

clear

echo -e "${COLOR_TERMINAL_AMARILLO}+---------------------------------------------------------------------------------+${RESETEAR_COLOR}"
echo -e "${COLOR_TERMINAL_AMARILLO}|                                                                                 |${RESETEAR_COLOR}"
echo -e "${COLOR_TERMINAL_AMARILLO}|           █████╗ ███████╗██╗   ██╗ ██████╗███████╗███╗   ██╗ █████╗             |${RESETEAR_COLOR}"
echo -e "${COLOR_TERMINAL_AMARILLO}|          ██╔══██╗╚══███╔╝██║   ██║██╔════╝██╔════╝████╗  ██║██╔══██╗            |${RESETEAR_COLOR}"
echo -e "${COLOR_TERMINAL_AMARILLO}|          ███████║  ███╔╝ ██║   ██║██║     █████╗  ██╔██╗ ██║███████║            |${RESETEAR_COLOR}"
echo -e "${COLOR_TERMINAL_AMARILLO}|          ██╔══██║ ███╔╝  ██║   ██║██║     ██╔══╝  ██║╚██╗██║██╔══██║            |${RESETEAR_COLOR}"
echo -e "${COLOR_TERMINAL_AMARILLO}|          ██║  ██║███████╗╚██████╔╝╚██████╗███████╗██║ ╚████║██║  ██║            |${RESETEAR_COLOR}"
echo -e "${COLOR_TERMINAL_AMARILLO}|          ╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝            |${RESETEAR_COLOR}"
echo -e "${COLOR_TERMINAL_AMARILLO}|                                                                                 |${RESETEAR_COLOR}"
echo -e "${COLOR_TERMINAL_AMARILLO}+-----------------------------AUTHOR BY: HERO_HZ1999YT----------------------------+${RESETEAR_COLOR}"
echo -e "${COLOR_TERMINAL_CYAN}============================>> INICIANDO INSTALACION <<============================${RESETEAR_COLOR}"

# VERIFICAMOS SI HAY UNA INSTALACION EXISTENTE DE AZUCENA Y LA REMOVEMOS
echo -e "${COLOR_TERMINAL_AZUL}BUSCANDO INTALACION DEL PROGRAMA YA EXISTENTES PARA REMOVERLA${RESETEAR_COLOR}"
# DIRECTORIO
if [ -d "$DIRECTORIO" ]; then
    rm -r -d -f $DIRECTORIO
    echo -e "${COLOR_TERMINAL_AMARILLO}DIRECTORIO RAIZ[REMOVIDO]${RESETEAR_COLOR}"
fi

# ARCHIVO DESKTOP
if [ -f "$ARCHIVO_DESKTOP" ]; then
    rm -f $ARCHIVO_DESKTOP
    echo -e "${COLOR_TERMINAL_AMARILLO}ARCHIVO DESKTOP[REMOVIDO]${RESETEAR_COLOR}"
fi

# ARCHIVO DESKTOP
if [ -f "$EJECUTABLE_TERMINAL" ]; then
    rm  -f $EJECUTABLE_TERMINAL
    echo -e "${COLOR_TERMINAL_AMARILLO}ARCHIVO EJECUTABLE[REMOVIDO]${RESETEAR_COLOR}"
fi

# INSTALACION
echo -e "${COLOR_TERMINAL_AZUL}ARCHIVOS EXISTENTES REMOVIDOS, INICIANDO INSTALACION 7W7${RESETEAR_COLOR}"
echo -e "${COLOR_TERMINAL_AZUL}BUSCANDO DIRECTORIO CLONADO DE GIT EN TU DIRECTORIO HOME${RESETEAR_COLOR}"
if [ -d "$DIRECTORIO_CLONADO_GIT" ]; then
    echo -e "${COLOR_TERMINAL_VERDE}DIRECTORIO[EXISTENTE]${RESETEAR_COLOR}"
    
    # RENOMBRAMOS EL REPOSITORIO CLONADO DE GITHUB
    mv $DIRECTORIO_CLONADO_GIT $DIRECTORIO
    echo -e "${COLOR_TERMINAL_VERDE}DIRECTORIO RAIZ[CREADO]${RESETEAR_COLOR}"
    
    # REMOVEMOS EL DIRECTORIO QUE GITHUB CREA POR DEFECTO
    rm -r -f $DIRECTORIO_GITHUB
    echo -e "${COLOR_TERMINAL_VERDE}DIRECTORIO .git[REMOVIDO]${RESETEAR_COLOR}"

    # ARCHIVO .DESKTOP QUE EJECUTA A AZUCENA AL ARRANCAR LA SESION
    echo -e "${COLOR_TERMINAL_VERDE}MOVIENDO ARCHIVO .desktop A SU RUTA${RESETEAR_COLOR}"
    if [ -d "$DIRECTORIO_AUTOSTART" ]; then
        mv "$DIRECTORIO/azucena.desktop" $DIRECTORIO_AUTOSTART
        echo -e "${COLOR_TERMINAL_VERDE}ARCHIVO DESKTOP[MOVIDO]${RESETEAR_COLOR}"
    else
        mkdir $DIRECTORIO_AUTOSTART
        mv "$DIRECTORIO/azucena.desktop" $DIRECTORIO_AUTOSTART
        echo -e "${COLOR_TERMINAL_VERDE}ARCHIVO DESKTOP[MOVIDO]${RESETEAR_COLOR}"
    fi
    echo "Exec=/home/$USER/.azucena/azucena" >> /home/$USER/.config/autostart/azucena.desktop

    # ARCHIVO EJECUTABLE POR TERMINAL
    echo -e "${COLOR_TERMINAL_VERDE}MOVIENDO ARCHIVO EJECUTABLE A SU RUTA${RESETEAR_COLOR}"
    if [ -d "$DIRECTORIO_BIN" ]; then
        cp "$DIRECTORIO/azucena" $DIRECTORIO_BIN
        echo -e "${COLOR_TERMINAL_VERDE}ARCHIVO EJECUTABLE[COPIADO]${RESETEAR_COLOR}"
    else
        mkdir $DIRECTORIO_BIN
        cp "$DIRECTORIO/azucena" $DIRECTORIO_BIN
        echo -e "${COLOR_TERMINAL_VERDE}ARCHIVO EJECUTABLE[COPIADO]${RESETEAR_COLOR}"
    fi

else 
    echo -e "${COLOR_TERMINAL_AMARILLO}DIRECTORIO[NO EXISTENTE]${RESETEAR_COLOR}"
    echo -e "${COLOR_TERMINAL_ROJO}DEBES DE CLONAR EL REPOSITORIO GIT EN TU HOME\nRUTA:'/home/nombre_usuario/'${RESETEAR_COLOR}"
    exit 1
fi