
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
$ mkdir /home/$USER/.config/autostart
$ cd && git clone https://github.com/hero-hz1999yt/azucena.git
$ mv /home/$USER/azucena/iniciar-azucena.desktop /home/$USER/.config/autostart/
$ mv /home/$USER/azucena /home/$USER/.azucena
$ sudo cp /home/$USER/.azucena/azucena /usr/local/bin/
$ echo "Exec=/home/$USER/.azucena/azucena" >> /home/$USER/.config/autostart/iniciar-azucena.desktop
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
$ rm -r /home/$USER/.azucena /home/$USER/.config/autostart/azucena_autostart.desktop
```
## License

[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)


## ==AMANTE DEL SOFTWARE LIBRE==