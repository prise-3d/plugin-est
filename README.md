
# Plugin Test

***
Ce projet consiste en la création d'un add-on pour Blender. Cet add-on de test permet de comprendre la structuration d'un add-on pour Blender, et de prendre en main l'API Python pour Blender : bpy.
***

## Sommaire
  - [Installation](#installation)
  - [Utilisation](#utilisation)
  - [Technologies](#technologies)

***

## Installation

Pour installer ce plugin, veuillez télécharger l'archive qui porte son nom, **add_sphere_formation.zip** dans la section **Releases** de ce projet.
Une fois le fichier .zip récupéré, ouvrez Blender, puis dans **Edit>Preferences**, sélectionnez l'onglet **Add-ons**. 
En appuyant sur le bouton **Install**, une fenêtre d'explorateur de fichier s'ouvre.
Sélectionnez l'archive .zip du plugin, puis cliquez sur **install Add-on**.
Lorsque l'add-on s'affiche dans la liste, **cochez la case** située à coté de son nom pour activer l'extension.
Une fois l'add-on activé, un onglet s'ajoute à la **barre latérale**. 

***

## Utilisation

Après avoir sélectionné l'onglet du plugin, **un sous menu** de la barre latérale s'affiche, avec plusieurs options de formes à générer. Un clic sur l'un de ces boutons fait apparaître, en plus de la fome choisie, un **panneau d'ajustements** qui permet de faire varier les propriétés de la forme à générer.

L'add-on permet d'ajouter quatre types de structure, faites de sphères, à la scène. Ces structures sont:
* Une ligne de sphères
* Un cube de sphères
* Une pyramide de sphères
* Une pyramide de pyramides du type Sierpinski (De niveau 2)

L'utilisateur peut interagir avec les paramètres suivants:

* Le nombre de sphères constituant une arrête 
* La taille et le niveau de détail d'une sphère
* La distance entre les sphères
* La position de la structure

Il peut également choisir si les sphères doivent être jointes pour former la structure, ou non (hormis la pyramide de Sierpinski). 

*** 

## Technologies

* Blender 2.93
* Blender Python API