#!/usr/bin/python3
# -- COMENTARIO: este archivo es para pruebas de codigo
from gtts import gTTS
from subprocess import Popen

tts = gTTS("hola mundo, yo soy un text to speech en el que se estan haciendo pruebas analmente sensuales", tld="com.mx", lang="es", slow=False)

tts.save("/home/hero-hz1999yt/Descargas/texto2.mp3")

audio = Popen("mpg123 /home/hero-hz1999yt/Descargas/texto2.mp3 &> /dev/null", shell=True)

