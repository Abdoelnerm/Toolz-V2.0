B
    ��\D  �               @   sP  d dl Z d dlZd dlZe�d� e�d� ed� e�d� ed� e�d� ed� e�d� ed� e�d� ed	� e�d� ed
� e�d� ed� e�d� ed�Zedkr�e�d� n�edkr�e�d� nredkr�e�d� n^edk�red� e�d� n@edk�r"e�d� n*edk�r8e�d� nedk�rLe�d� dS )�    Nz apt update && apt upgrade z3 apt -y install gnupg gpg tar bash curl wget proot z[91m1- Termux-Ubuntu �   z 2- Termux-Fedora z 3- Termux-ArchLinux z 4- Termux-Parrot-Os z 5- Termux-KaliNetHunter z 6- Termux-CentOs z[91m7- Termux-Debian zEnter Your Choice: �1zZ git clone https://github.com/Neo-Oli/termux-ubuntu && cd termux-ubuntu && bash ubuntu.sh �2zX https://github.com/nmilosev/termux-fedora && cd termux-fedora && bash termux-fedora.sh �3zq wget https://raw.githubusercontent.com/sdrausty/TermuxArch/master/setupTermuxArch.sh && bash setupTermuxArch.sh �4zT You Need Ubuntu To Install Parrot Os On It And You Can Install It from this Script zm git clone https://github.com/developerkunal/Converto && cd Converto && bash converto.sh && 1 && 2 && 2 && 4 �5z� git clone https://github.com/Hax4us/Nethunter-In-Termux && cd Nethunter-In-Termux && mv kalinethunter $HOME && cd && bash kalinethunter �6z} wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/CentOS/centos.sh && bash centos.sh �7z} wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh && bash debian.sh )�sys�os�time�system�print�sleep�inputZ
user_input� r   r   �2/data/data/com.termux/files/home/tests/Toolz/.3.py�<module>   sD   












