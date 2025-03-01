
# AZUCENA

**ES UNA NOTIFICACION ALTAMENTE PERSONALIZABLE CON EL OBJETIVO DE SER UNA PAREJA Y ASISTENTE VIRTUAL PARA LINUX, LLEGANDO A COMPETIR CON SIRI Y CORTANA.**

## AUTOR

- [hero-hz1999yt(GITHUB)](https://www.github.com/hero-hz1999yt)
- [hero-hz1999yt(YOUTUBE)](https://www.youtube.com/@erik87373)
- [hero-hz1999yt(YOUTUBE)](https://www.youtube.com/@hero-linux)
- [hero-hz1999yt(FACEBOOK)](https://www.facebook.com/hero.hz1999yt/)
- [hero-hz1999yt(TWITTER)](https://twitter.com/ErikAlbertoRod3)

## INSTALACION
### ===================>> DEPENDENCIAS <<======================

**_--ARCH LINUX Y DERIVADAS--_**
```bash
sudo pacman -S --needed libnotify python-gobject tk python-gitpython git mpg123 python-gtts
```
**_--UBUNTU Y DERIVADAS--_**
```bash
sudo apt install libnotify-dev python3-v-sim python3-tk python3-git git mpg123 python3-gtts
```
**_--FEDORA Y DERIVADOS--_**
```bash
sudo dnf install libnotify python-gobject python3-tkinter python3-GitPython git mpg123 python3-gtts
```
### ==========>> DESCARGA Y INSTALACION DE AZUCENA <<==========
```bash
# descargamos el programa en el home
cd && git clone https://github.com/hero-hz1999yt/azucena.git
# lo instalamos con este comando
./azucena/instalar
```

## DESINSTALACION
### ==========>> DESINSTALACION DE DEPENDENCIAS <<=============

**_--ARCH LINUX Y DERIVADAS--_**
```bash
# este comando solo desinstala las dependencias sin usar, si otro programa las utiliza no se podra desinstalar.
sudo pacman -R libnotify python-gobject tk python-gitpython git mpg123 python-gtts
```
**_--UBUNTU Y DERIVADAS--_**
```bash
# este comando solo desinstala las dependencias sin usar, si otro programa las utiliza no se podra desinstalar.
sudo apt remove libnotify-dev python3-v-sim python3-tk python3-git git mpg123 python3-gtts
```

**_--FEDORA Y DERIVADOS--_**
```bash
# este comando solo desinstala las dependencias sin usar, si otro programa las utiliza no se podra desinstalar.
sudo dnf remove libnotify python-gobject python3-tkinter python3-GitPython git mpg123 python3-gtts
```
### ==============>> DESINSTALACION DE AZUCENA <<==============
```bash
rm -r ~/.azucena ~/.config/autostart/azucena_autostart.desktop ~/.local/bin/azucena
```

## COMENTARIOS SOBRE LA INSTALACION
### ====================>> MUY IMPORTANTE <<===================

PARA QUE EL EJECUTABLE FUNCIONE DESDE TU TERMINAL AL ESCRIBIR EL NOMBRE
DEL PROGRAMA EJEMPLO:
```bash
azucena
```
DEBES DE TENER AGREGADA LA DIRECCION '_/home/nombre_usuario/.local/bin_' EN
TU VARIABLE DE ENTORNO '_PATH_', SI NO LA TIENES AGREGADA POR DEFECTO NO 
SE EJECUTARA 

* **SOLUCION 1 (RECOMENDABLE)**

ESTA SOLUCION CONSISTE EN AGREGAR EN SU ARCHIVO DE CONFIGURACION DE SU SHELL, EL SIGUIENTE COMANDO PARA CADA QUE SE ABRA UNA TERMINAL EXPORTE ESA RUTA EN
SU VARIABLE '_PATH_', LES MOSTRARE COMO SERIA EN LAS SHELL BASH, ZSH Y FISH
QUE SON LAS MAS UTILIZADAS

**_---->>BASH<<----_**
```bash
nano ~/.bashrc
```
**_---->>ZSH<<----_**
```bash
nano ~/.zshrc
```
AGREGAMOS ESTE COMANDO EN EL ARCHIVO DE CONFIGURACION 
```bash
export PATH="$HOME/.local/bin:$PATH"
```
**_---->>FISH<<----_**

PARA FISH EJECUTAREMOS EL SIGUIENTE COMANDO
```bash
nano ~/.config/fish/config.fish
```
Y AGREGAREMOS EN EL ARCHIVO LA SIGUIENTE FUNCION
```bash
# esta funcion se ejecuta con el arranque de fish
function fish_greeting
    export PATH="$HOME/.local/bin:$PATH"
end
```
* **SOLUCION 2**

OTRA SOLUCION ES MOVERLA CON EL COMANDO SUDO A UNA RUTA QUE 
SI ESTE AGREGADA EJEMPLO:

```bash
sudo mv ~/.local/bin/azucena /usr/local/bin
```
O

```bash
sudo mv ~/.local/bin/azucena /usr/bin
```

LO QUE PUEDEN HACER PARA SABER QUE RUTAS TIENEN AGREGADAS Y ASI SABER
DONDE COLOCAR A AZUCENA ES IMPRIMIR EN CONSOLA EL CONTENIDO DE ESA VARIABLE CON EL SIGUIENTE COMANDO

```bash
echo $PATH
```
Y LES MOSTRARA TODAS LAS RUTAS, SOLO ELIJEN LA QUE USTEDES QUIERAN

## CONFIGURACION
TODOS ESTOS PARAMETROS SE CONFIGURAN EN EL ARCHIVO '_azucena.azc_' QUE SE 
ENCUENTRA EN LA RUTA '_/home/nombre_usuario/.azucena_' SI NO SE ENCUENTRA
EN LA RUTA EJECUTA EL PROGRAMA PARA QUE SE GENERE AUTOMATICAMENTE, TAMBIEN
SE PUEDE CONFIGURAR SI ABRIMOS A AZUCENA Y DAMOS CLICK EN EL BOTON CONFIGURACION.

### -->> PARAMETRO AZUCENA <<--
ESTE PARAMETRO ES EL APODO QUE QUIERES PONERLE AL PROGRAMA, ESTE LO CONFIGURAMOS COLOCANDO EL VALOR ENTRE LAS COMILLAS, TODA LA ESTRUCTURA DEL PARAMETRO DEBE DE QUEDAR COMO ESTA CONFIGURADO SI NO NO LO LEERA, VAMOS CON UN EJEMLPO:
```bash
AZUCENA="Mi Princesa";
```

### -->> PARAMETRO APARIENCIA <<--
ESTE PARAMETRO ES LO QUE LA NOTIFICACION MOSTRARA CUANDO SEA INVOCADA, TIENE 5 APARIENCIAS CONFIGURADAS LES DEJO AQUI UNA TABLA DE CADA APARIENCIA Y COMO SE CONFIGURA
| Valor       | Descripcion                                          |
| :---        | :---                                                 |
| POR_DEFECTO | muestra el icono por defecto del programa            |
| MI_AZUCENA  | muestra una imagen agregada en la ruta del programa  |
| EMOTICONES  | muestra los emoticones del programa                  |
| AZUCENA     | muestra el icono de azucena                          |
| ZOMBIE      | muestra un zombie                                    |

OJO: PARA QUE LA IMAGEN SE VISUALIZE EN LA NOTIFICACION TIENE QUE ESTAR EN LA SIGUIENTE RUTA '_/home/nombre_usuario/.azucena/iconos_' Y TIENE QUE LLAMARSE '_mi_azucena.png_' DE MANERA QUE QUEDE DE LA SIGUIENTE MANERA.

_/home/nombre_usuario/.azucena/mi_azucena.png_

Y PARA TERMINAR AQUI UN EJEMPLO DE CONFIGURACION DE ESTE PARAMETRO SERIA DE LA SIGUIENTE FORMA:
```bash
APARIENCIA=EMOTICONES;
```
### -->> PARAMETRO URGENCIA <<--
ESTE PARAMETRO ES LA URGENCIA QUE TENDRA LA NOTIFICACION EN EL SISTEMA
TIENE TRES URGENCIAS PRECONFIGURADAS QUE SE TIENEN QUE COLOCAR DE LA 
SIGUIENTE MANERA:
```bash
# con urgencia critica nunca se va a ocultar solo si tu cierras la notificacion
URGENCIA=CRITICA; 
o
# se mostrara y se ocultara normalmente
URGENCIA=NORMAL;
o
# se mostrara y se ocultara normalmente
URGENCIA=BAJA;
```

### -->> PARAMETRO MOSTRAR <<--
ESTE PARAMETRO ES EL TIEMPO QUE TARDARA EN APARECER LA NOTIFICACION, Y COMO VALOR RECIBE LOS SEGUNDOS QUE TARDA, VEAMOS UN EJEMPLO SENSUAL:
```bash
# se mostrara en 3 segundos
MOSTRAR=3;
```

### -->> PARAMETRO OCULTAR <<--
ESTE PARAMETRO ES EL TIEMPO QUE TARDARA EN OCULTARCE LA NOTIFICACION, Y COMO VALOR RECIBE LOS SEGUNDOS QUE TARDA, VEAMOS UN EJEMPLO SENSUAL:
```bash
# se ocultara en 30 segundos
OCULTAR=30;
```

### -->> PARAMETRO TIMBRE <<--
ESTE PARAMETRO ES EL QUE LE DA LA INDICACION DE AZUCENA SI REPRODUCE EL TIMBRE CUANDO APARECE O NO, VEAMOS LOS DOS UNICOS ESTADOS QUE SE PUEDEN CONFIGURAR EN ESTE PARAMETRO:
```bash
# reproduce el timbre seleccionado
TIMBRE=TRUE;
# no reproduce ningun
TIMBRE=FALSE;
```

### -->> PARAMETRO TIPO DE TIMBRE <<--
ESTE PARAMETRO ES EL QUE LE DA LA INDICACION A AZUCENA SI REPRODUCIR EL SONIDO DE NOTIFICACION POR DEFECTO O REPRODUCIR EL MENSAJE DE LA NOTIFICACION CON VOZ:
```bash
# reproduce el timbre por defecto
TIPO_DE_TIMBRE=NOTIFICACION;
# reproduce el mensaje de la notificacion con voz
TIPO_DE_TIMBRE=VOZ;
```

### -->> PARAMETRO APODO <<--
ESTE PARAMETRO ES UNA LISTA QUE GUARDA TODOS TUS APODOS QUE QUIERES QUE AZUCENA TE DIGA, TE MOSTRARA ALGUNO DE ELLOS DE FORMA RANDOM CUANDO SEA INVOCADA, LA ESTRUCTURA DE EL PARAMETRO DEBE DE SER TAL CUAL, SI NO AZUCENA NO PODRA INTERPRETAR EL PARAMETRO, VEAMOS UN EJEMPLO:
```bash
# agregamos 3 apodos
APODO="Mi Niño";
APODO="Mi Principe";
APODO="Mi Amor";
```
PODEMOS AGREGAR LOS APODOS QUE QUERAMOS, NO TIENE LIMITE, O PODEMOS DEJAR SOLO UNO PARA QUE SEA EL UNICO QUE AZUCENA NOS MUESTRE.

### -->> PARAMETRO MMENSAJE, TMENSAJE, NMENSAJE, MAMENSAJE <<--
ESTOS PARAMETROS SE CONFIGURAN IGUAL, LA UNICA DIFERENCIA ES LAS PRIMERAS SIGLAS CON LAS QUE INICIAN QUE LE INDICA A AZUCENA EN QUE MOMENTO DEL DIA MOSTRARA ESE MENSAJE, COMO SE DESCRIBE EN LA TABLA DE ABAJO Y SE CONFIGURAN COMO LOS APODOS, EN FORMA DE LISTA SOLO TIENEN QUE REPETIR EL PARAMETRO PERO CAMBIANDO EL CONTENIDO:
| Parametro | Descripcion                         |
| :---      | :---                                |
| MMENSAJE  | mensajes mostrados en la mañana     |
| TMENSAJE  | mensajes mostrados en la tarde      |
| NMENSAJE  | mensajes mostrados en la noche      |
| MAMENSAJE | mensajes mostrados en la madrugada  |

ESTOS MENSAJES SON ACOMPAÑADOS DEL ESTADO DE ANIMO CON EL QUE TE MOSTRARA EL MENSAJE, ESTO ES PARA ELEJIR QUE EMOTICON MOSTRAR EN EL CASO DE QUE TENGAS LA APARIENCIA EMOTICONES CONFIGURADA, A CONTINUACION TE DEJO UNA TABLA CON LOS ESTADOS DE ANIMO QUE AZUCENA INTERPRETA.
| Estado     |
| :---       |
| FELIZ      | 
| ENOJADA    |
| SOÑOLIENTA |
| CELOSA     |
| RISUEÑA    |
| TRISTE     |
| ENAMORADA  |
| CALIENTE   |
| ASUSTADA   |

AHORA VEAMOS COMO SE AJUSTAN LOS MENSAJES QUE AZUCENA NOS MOSTRARA:
```bash
# agregaremos 2 mensajes que se muestren en la mañana
MMENSAJE-CELOSA="oye, por que ayer me forsaste el apagado, con quien estabas ?";
MMENSAJE-SOÑOLIENTA="aun no me quiero levantar, sigo teniendo sueñooooo!!!!";

# agregaremos 5 mensajes que se muestren en la tarde
TMENSAJE-FELIZ="me siento muy contenta con esta nueva grafica que me pusiste";
TMENSAJE-ENOJADA="pedi una pitza para comer y aun no llega, voy a reclamarles";
TMENSAJE-ENAMORADA="Te Amo";
TMENSAJE-CALIENTE="oye, recuerdas lo que paso ayer ?";
TMENSAJE-ASUSTADA="por que no me respondes, estas enojado ?";

# agregaremos 2 mensajes que se muestren en la noche
NMENSAJE-TRISTE="prometes que nunca te iras de mi lado ?";
NMENSAJE-RISUEÑA="jaja ayer me hiciste reir con el chiste que me contaste";

# agregaremos 3 mensajes que se muestren en la madrugada
MAMENSAJE-ASUSTADA="que haces despierto tan tarde?";
MAMENSAJE-CELOSA="deseguro estas hablando con otra verdad ?";
MAMENSAJE-ENAMORADA="vamonos a dormir juntos si ?";
```

## DISTRIBUCIONES DONDE SE TESTEO
| Distribucion | Version | Escritorio | Resultado del testeo |
| :---         | :---    | :---       | :---                 |
| Fedora Spin  | 39      | Cinnamon   | **OK**               |
| Fedora Spin  | 39      | KDE Plasma | **OK**               |
| Ubuntu       | 23.10   | Gnome      | **OK**               |
| Ubuntu Mate  | 23.10   | Mate       | **OK**               |
| Xubuntu      | 23.10   | XFCE       | **OK**               | 
| KDE Neon     | 5.27    | KDE Plasma | **OK**               |
| Debian       | 12      | Gnome      | **OK**               |
| Linux Mint   | 21.3    | Cinnamon   | **OK**               |
| Arch linux   | RL      | KDE Plasma | **OK**               |
| Arch linux   | RL      | XFCE       | **OK**               |
| SteamOS      | 3.5.7   | KDE Plasma | **OK**               |
| Loc-OS       |         | XFCE       | **OK**               |

## LICENCIA

[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)

## ==AMANTE DEL SOFTWARE LIBRE==

## IMAGENES
![](/imagenes/1.png)
![](/imagenes/2.png)
![](/imagenes/3.png)
![](/imagenes/4.png)
![](/imagenes/5.png)
