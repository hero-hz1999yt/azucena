#!/bin/bash
# -- CONSTANTES --
USUARIO=$USER
DIRECTORIO="/home/$USUARIO/.azucena"
COLOR_TERMINAL_ROJO='\033[0;31m'
RESETEAR_COLOR='\033[0m'

# -- COMENTARIO: validamos si el directorio se encuentra en la sesion(esto para evitar que se ejecute si no esta instalado) END --
if [ -d "$DIRECTORIO" ]; then
    python3 /home/$USUARIO/.azucena/source/azucena.py
else 
    echo -e "${COLOR_TERMINAL_ROJO}EL DIRECTORIO '.azucena' NO ESTA EN TU SISTEMA, VERIFICA QUE EL PROGRAMA ESTE INSTALADO${RESETEAR_COLOR}"
fi
