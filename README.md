
# AZUCENA

Es una notificacion que se muestra en el inicio de sesion de tu usuario.
Pero se tiene pensado que sera un asistente virtual para linux mejor que cortana y siri.




## AUTOR

- [@hero-hz1999yt(GITHUB)](https://www.github.com/hero-hz1999yt)
- [@hero-hz1999yt(YOUTUBE_CHANEL_1)](https://www.youtube.com/@erik87373)
- [@hero-hz1999yt(YOUTUBE_CHANEL_2)](https://www.youtube.com/@hero-linux)
- [@hero-hz1999yt(FACEBOOK)](https://www.facebook.com/hero.hz1999yt/)
- [@hero-hz1999yt(TWITTER)](https://twitter.com/ErikAlbertoRod3)
## INSTALACION
===================>> DEPENDENCIAS <<======================
```bash
--ARCH LINUX Y DERIVADAS--
$ sudo pacman -S libnotify python-gobject tk python-gitpython git mpg123

--UBUNTU Y DERIVADAS--
$ sudo apt install libnotify-dev python3-v-sim python3-tk python3-git git mpg123

--FEDORA Y DERIVADOS--
$ sudo dnf install libnotify python-gobject python3-tkinter python3-GitPython git mpg123
```
==========>> DESCARGA Y INSTALACION DE AZUCENA <<==========
```bash
$ cd && git clone https://github.com/hero-hz1999yt/azucena.git
$ ./azucena/instalar
```

## DESINSTALACION
==========>> DESINSTALACION DE DEPENDENCIAS <<=============
```bash
--ARCH LINUX Y DERIVADAS--
$ sudo pacman -Rsn libnotify python-gobject tk python-gitpython git mpg123

--UBUNTU Y DERIVADAS--
$ sudo apt remove libnotify-dev python3-v-sim python3-tk python3-git git mpg123

--FEDORA Y DERIVADOS--
$ sudo dnf remove libnotify python-gobject python3-tkinter python3-GitPython git mpg123
```
==============>> DESINSTALACION DE AZUCENA <<==============
```bash
$ rm -r ~/.azucena ~/.config/autostart/azucena_autostart.desktop ~/.local/bin/azucena
```
====================>> MUY IMPORTANTE <<===================
```bash
PARA QUE EL EJECUTABLE FUNCIONE DESDE TU TERMINAL AL ESCRIBIR EL NOMBRE
DEL PROGRAMA EJEMPLO:

$ azucena

DEBES DE TENER AGREGADA LA DIRECCION /home/nombre_usuario/.local/bin EN
TU VARIABLE DE ENTORNO 'PATH', SI NO LA TIENES AGREGADA POR DEFECTO NO 
SE EJECUTARA, UNA SOLUCION ES MOVERLA CON EL COMANDO SUDO A UNA RUTA QUE 
SI ESTE AGREGADA EJEMPLO:

$ sudo cp ~/.azucena/azucena /usr/local/bin

O

$ sudo cp ~/.azucena/azucena /usr/bin
```

## License

[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)


## ==AMANTE DEL SOFTWARE LIBRE==