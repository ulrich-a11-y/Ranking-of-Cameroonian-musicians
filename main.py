# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 16:15:23 2023

@author: Ulrich
"""

import requests
import json
from bs4 import BeautifulSoup
import pandas as panda

def getPage(url):
    
    r = requests.get(url)
    return BeautifulSoup(r.text, 'lxml')


def getData(url):
    
    bs = getPage(url)
    stringData = bs.find('body').findAll('script')[13].text.replace('var ytInitialData = ','').replace(";","")
    return json.loads(stringData)


def enregistrementData(index,ligne,titreChaine,nbreAbon,titreVideo,nbre_vue,temps_ann,temps_compl):
    
    tableau.loc[ligne] = [index ,titreChaine , nbreAbon , titreVideo , nbre_vue , temps_ann , temps_compl ]
    
    
def traitement_nombre_vue(nombreVue):
    text = nombreVue.split(" ")
    textf = text[0].replace(",","")
    
    return int(textf)
    
    
    
def rechercheData(index,url):
        
    jsonData = getData(url)
    
    titreChaine = jsonData['header']['c4TabbedHeaderRenderer']['title']
    nbreAbon = jsonData['header']['c4TabbedHeaderRenderer']['subscriberCountText']['simpleText']


    for i in range(100):
        
         # durée
            
        temps_ann = jsonData['contents']['twoColumnBrowseResultsRenderer']['tabs'][1]['tabRenderer']['content']['richGridRenderer']['contents'][i]['richItemRenderer']['content']['videoRenderer']['publishedTimeText']['simpleText']
        temps_compl = jsonData['contents']['twoColumnBrowseResultsRenderer']['tabs'][1]['tabRenderer']['content']['richGridRenderer']['contents'][i]['richItemRenderer']['content']['videoRenderer']['lengthText']['accessibility']['accessibilityData']['label']
       
        
        if(temps_ann == '1 year ago'):
            break

       

        # Titre vidéo
        
        titreVideo = jsonData['contents']['twoColumnBrowseResultsRenderer']['tabs'][1]['tabRenderer']['content']['richGridRenderer']['contents'][i]['richItemRenderer']['content']['videoRenderer']['title']['runs'][0]['text']
      
   
        # Nombre de vues
        nbre_vue_brut = jsonData['contents']['twoColumnBrowseResultsRenderer']['tabs'][1]['tabRenderer']['content']['richGridRenderer']['contents'][i]['richItemRenderer']['content']['videoRenderer']['viewCountText']['simpleText']
        
        nbre_vue = traitement_nombre_vue(nbre_vue_brut)
        
        
        enregistrementData(index, len(tableau),titreChaine,nbreAbon,titreVideo,nbre_vue,temps_ann,temps_compl) #Ici j'enregistre les données en utilisant le nombre de ligne du tableau
   
# liste des liens des chaînes youtube sur onglet video

chaineYoutube = [

                'https://www.youtube.com/@krysm4403/videos',
                'https://www.youtube.com/@Martins237/videos',
                'https://www.youtube.com/@Sabrina-Love/videos',
                'https://www.youtube.com/@IAMLIBIANCA/videos',
                'https://www.youtube.com/@mrshyne3798/videos',
                'https://www.youtube.com/@CYSOULOfficiel/videos',
                'https://www.youtube.com/@fhishgophmen1614/videos',
                'https://www.youtube.com/@AkumbaMusic/videos',
                'https://www.youtube.com/@Lockoofficial/videos',
                'https://www.youtube.com/@BlancheBailly237/videos',
                'https://www.youtube.com/@shabamuzik/videos',
                'https://www.youtube.com/@Lydol/videos',
                'https://www.youtube.com/@TENOR237/videos',
                'https://www.youtube.com/@lionnprod/videos',
                'https://www.youtube.com/@starfishentertainment6538/videos',
                'https://www.youtube.com/@CharlotteDipandaOfficielle/videos',
                'https://www.youtube.com/@MrLeo237/videos',
                'https://www.youtube.com/@AlphaBetterRecords237/videos',
                'https://www.youtube.com/@mimieofficial185/videos',
                'https://www.youtube.com/@vanisterenamaofficiel4986/videos',
                'https://www.youtube.com/@sandrinennanga237/videos',
                'https://www.youtube.com/@indira3427/videos',
                'https://www.youtube.com/@BluNationRecording/videos',
                'https://www.youtube.com/@cleograe6931/videos',
                'https://www.youtube.com/@vividsmith668/videos',
                'https://www.youtube.com/@kwatamusicinc7718/videos',
                'https://www.youtube.com/@EBENENTERTAINMENTOFFICIAL/videos',
                'https://www.youtube.com/@StanleyEnow/videos',
                'https://www.youtube.com/@koppo237/videos',
                'https://www.youtube.com/@magascoofficiel5742/videos',
                'https://www.youtube.com/@bendeccaofficiel9660/videos',
                'https://www.youtube.com/@vernyuytinamusica/videos',
                'https://www.youtube.com/@happydefoulanofficiel3576/videos',
                'https://www.youtube.com/@COCOARGENTEEOFFICIEL/videos',
                'https://www.youtube.com/@gomezoba6621/videos',
                'https://www.youtube.com/@EWUBEOFFICIAL/videos',
                'https://www.youtube.com/@Darinavictryofficiel/videos',
                'https://www.youtube.com/@LadyPonceOfficiel/videos',
                'https://www.youtube.com/@Hopiho/videos',
                'https://www.youtube.com/@walimelomusic3415/videos',
                'https://www.youtube.com/@maahloxofficiel222/videos',
                'https://www.youtube.com/@PETITBOZARD/videos',
                'https://www.youtube.com/@NewBellMusicChannel/videos',
                'https://www.youtube.com/@minksofficiel5855/videos',
                'https://www.youtube.com/@AveiroDjess/videos',
                'https://www.youtube.com/@StevensME/videos',
                'https://www.youtube.com/@ktinoofficiel1674/videos',
                'https://www.youtube.com/@StevensME/videos',
                'https://www.youtube.com/@Sabiboient/videos',
                'https://www.youtube.com/@kangquintusmusic548/videos',
                'https://www.youtube.com/@gracedeccaofficiel/videos',
                'https://www.youtube.com/@lucky2officiel142/videos',
                'https://www.youtube.com/@longuesimon8269/videos',
                'https://www.youtube.com/@ZeevalOfficial/videos',
                'https://www.youtube.com/@jolygarcon2338/videos',
                'https://www.youtube.com/@lesrythmeursabc8642/videos',
                'https://www.youtube.com/@XMALEYAOFFICIAL/videos',
                'https://www.youtube.com/@shabamuzik/videos',
                'https://www.youtube.com/@TchakalaVIPOriginale/videos',
                'https://www.youtube.com/@CabrelNanjipNyamton/videos',
                'https://www.youtube.com/@fulofficiel/videos',
                'https://www.youtube.com/@UniversalMusicAfrica-UMA/videos',
                'https://www.youtube.com/@petitmaloofficiel583/videos'   ]


# Création d'un tableau vide
tableau = panda.DataFrame(columns=['indexe','nomChaine','nombreAbon','titreVideo','nombreVue','temps','tempsCompl'])


    
for index in range(len(chaineYoutube)):
    
    try:
        rechercheData(index,chaineYoutube[index])
        
    except KeyError:
        error =( "La chaine Youtube d'index {i} n'a pas pu être scrapé!").format(i = index)
        print(error)
    
    except IndexError:
        print ("erreur d'index")

        #Affichage de l'éntête du dataframe
tableau.head()


# Debut de l'analyse des données

# Remarque :  On doit determiner le nombre de vues sur Youtube pour chaque artiste de debut 2022 jusqu'à maintenant.

# a) liste de chaine sans doublon

nomChaineBrut = tableau["nomChaine"]

list_nom_chaine_brut = list(nomChaineBrut)

liste_new = list(set(list_nom_chaine_brut))   # Ici on retire les doublons puis on cree une liste
liste_new.sort(reverse = False)             # Trie par ordre alphabétique
print(liste_new)

# b) J'initialise un regroupement à partir des enregistrement ayant les mêmes noms de chaîne
groups = tableau.groupby(['nomChaine'])   

# c) J'additionne le nombre de vue pour chaque groupe que je recupère et je crée une bibliothèque
dict_nombre_vues = { nom : groups.get_group(nom)['nombreVue'].sum()  for nom in liste_new} 
print(dict_nombre_vues)

# d) Classement par ordre décroissant des artistes musiciens camerounais et labels de musique  les plus vues sur Youtube de 2022 à maintenant

classement = (["%s: %s" % (k, v) for  k, v in sorted(dict_nombre_vues.items(), key=lambda x: x[1] , reverse = True)])

print(classement)




