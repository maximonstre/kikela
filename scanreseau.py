#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests as rq
import math 

#######VARIABLES POUR COMMUNICATION
API_KEY = "941d176c66ef92d587e6d7e1c03040b1"
AUTH_USER = ""
URL_BASE = "api.openweathermap.org/data/2.5/weather?q=London"

#######HEADER
headers = {
    'X-Auth-User': AUTH_USER,
    'X-Auth-Key': API_KEY,
   }



def perimetre_cercle(un_rayon):
    """Calculer le périmètre d'un cercle à partir de son rayon.
	:param un_rayon: le rayon du cercle (positif)
	:return le périmètre d'un cercle de rayon un_rayon
    """
    diametre = 2 * un_rayon
    return math.pi * diametre


def main():
    """Le programme principal."""
    # demander le rayon à l'utilisateur
    #saisie = input("Rayon du cercle : ")    # une chaîne de caractères
    #le_rayon = float(saisie)                # convertie en un nombre réel
    # calculer le périmètre
    # perimetre = perimetre_cercle(le_rayon)
    # afficher le périmètre à l'utilisateur
    # print("Le périmètre d'un cercle de rayon", le_rayon, "est", perimetre)
    test = rq.request("GET",URL_BASE, headers=headers, verify=False)
    print (test.text)


if __name__ == "__main__":
    main()
