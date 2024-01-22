
# AZUCENA

Es una notificacion que se muestra en el arranque de tu sesion, altamente configurable, te muestra mensajes motivadores que tu mismo puedes modificar, se tiene planeado que azucena sera la mejor asistente virtual de linux, mejor que cortana y siri.




## AUTOR

- [hero-hz1999yt(GITHUB)](https://www.github.com/hero-hz1999yt)
- [hero-hz1999yt(YOUTUBE)](https://www.youtube.com/@erik87373)
- [hero-hz1999yt(YOUTUBE)](https://www.youtube.com/@hero-linux)
- [hero-hz1999yt(FACEBOOK)](https://www.facebook.com/hero.hz1999yt/)
- [hero-hz1999yt(TWITTER)](https://twitter.com/ErikAlbertoRod3)

## AUTORES DE LOS ICONOS

- [vectors-market](https://www.flaticon.es/autores/vectors-market)
- [Smashicons](https://www.flaticon.es/autores/Smashicons)
- [Freepik](https://www.flaticon.es/autores/Freepik)
- [justicon](https://www.flaticon.es/autores/justicon)
## INSTALACION
### ===================>> DEPENDENCIAS <<======================

**_--ARCH LINUX Y DERIVADAS--_**
```bash
$ sudo pacman -S libnotify python-gobject tk python-gitpython git mpg123
```
**_--UBUNTU Y DERIVADAS--_**
```bash
$ sudo apt install libnotify-dev python3-v-sim python3-tk python3-git git mpg123
```
**_--FEDORA Y DERIVADOS--_**
```bash
$ sudo dnf install libnotify python-gobject python3-tkinter python3-GitPython git mpg123
```
### ==========>> DESCARGA Y INSTALACION DE AZUCENA <<==========
```bash
$ cd && git clone https://github.com/hero-hz1999yt/azucena.git
$ ./azucena/instalar
```

## DESINSTALACION
### ==========>> DESINSTALACION DE DEPENDENCIAS <<=============

**_--ARCH LINUX Y DERIVADAS--_**
```bash
$ sudo pacman -Rsn libnotify python-gobject tk python-gitpython git mpg123
```
**_--UBUNTU Y DERIVADAS--_**
```bash
$ sudo apt remove libnotify-dev python3-v-sim python3-tk python3-git git mpg123
```

**_--FEDORA Y DERIVADOS--_**
```bash
$ sudo dnf remove libnotify python-gobject python3-tkinter python3-GitPython git mpg123
```
### ==============>> DESINSTALACION DE AZUCENA <<==============
```bash
$ rm -r ~/.azucena ~/.config/autostart/azucena_autostart.desktop ~/.local/bin/azucena
```

## COMENTARIOS SOBRE LA INSTALACION
### ====================>> MUY IMPORTANTE <<===================

PARA QUE EL EJECUTABLE FUNCIONE DESDE TU TERMINAL AL ESCRIBIR EL NOMBRE
DEL PROGRAMA EJEMPLO:
```bash
$ azucena
```
DEBES DE TENER AGREGADA LA DIRECCION /home/nombre_usuario/.local/bin EN
TU VARIABLE DE ENTORNO 'PATH', SI NO LA TIENES AGREGADA POR DEFECTO NO 
SE EJECUTARA 

* **SOLUCION 1 (RECOMENDABLE)**

ESTA SOLUCION CONSISTE EN AGREGAR EN SU ARCHIVO DE CONFIGURACION DE SU SHELL, EL SIGUIENTE COMANDO PARA CADA QUE SE ABRA UNA TERMINAL EXPORTE ESA RUTA EN
SU VARIABLE 'PATH', LES MOSTRARE COMO SERIA EN LAS SHELL BASH, ZSH Y FISH
QUE SON LAS MAS UTILIZADAS

**_---->>BASH<<----_**
```bash
$ nano ~/.bashrc
```
**_---->>ZSH<<----_**
```bash
$ nano ~/.zshrc
```
AGREGAMOS ESTE COMANDO EN EL ARCHIVO DE CONFIGURACION 
```bash
$ export PATH="$HOME/.local/bin:$PATH"
```
**_---->>FISH<<----_**

PARA FISH EJECUTAREMOS EL SIGUIENTE COMANDO
```bash
$ nano ~/.config/fish/config.fish
```
Y AGREGAREMOS EN EL ARCHIVO LA SIGUIENTE FUNCION
```bash
function fish_greeting
    export PATH="$HOME/.local/bin:$PATH"
end
```
* **SOLUCION 2**

OTRA SOLUCION ES MOVERLA CON EL COMANDO SUDO A UNA RUTA QUE 
SI ESTE AGREGADA EJEMPLO:

```bash
$ sudo mv ~/.local/bin/azucena /usr/local/bin
```
O

```bash
$ sudo mv ~/.local/bin/azucena /usr/bin
```

LO QUE PUEDEN HACER PARA SABER QUE RUTAS TIENEN AGREGADAS Y ASI SABER
DONDE COLOCAR A AZUCENA ES IMPRIMIR EN CONSOLA EL CONTENIDO DE ESA VARIABLE CON EL SIGUIENTE COMANDO

```bash
$ echo $PATH
```
Y LES MOSTRARA TODAS LAS RUTAS, SOLO ELIJEN LA QUE USTEDES QUIERAN
## License

[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)


## ==AMANTE DEL SOFTWARE LIBRE==