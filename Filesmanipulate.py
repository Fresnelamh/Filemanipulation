import os

def Menu():
 print( "Bienvenue dans le Gestionnaire de Fichiers ! \n" 
  "1. Créer un fichier \n"
  "2. Écrire dans un fichier \n"
  "3. Lire un fichier \n"
  "4. Supprimer un fichier \n"
  "5. Quitter \n"
  
  )



def Creer_fichier(name):
    try:
      with open(name + ".txt", "x") as filecreate:
         print("Le fichier a bien été créé")
    except FileExistsError:
       print(f"A file with the same name '{name}.txt' as already exists")
    except Exception as e:
       print(f"An error '{e}' occured during the creation of the file")
    
   

def Ecrire_fichier (name,content):
   try:
      with open(name + ".txt", "a") as filewrite:
       filewrite.write(content)
   except FileExistsError:
       print(f"A file with the same name '{name}.txt' as already exists")
   except Exception as e:
       print(f"An error '{e}' occured during the  writing in the file")
   finally:
      filewrite.close()

def Lire_Fichier(name):
    try:
       with open(name + ".txt", "r") as fileread:
          print(fileread.read())
          
    except FileNotFoundError:
       print(f"A file with the name '{name}.txt' doesn't exist")
    except Exception as e:
       print(f"An error '{e}' occured during the reading of the file")
    finally:
       fileread.close()

def Supprimer(name):
    try:
     
         os.remove(name +".txt")
    
    except FileNotFoundError:
       print(f"A file with the name '{name}.txt' doesn't exist")
    except Exception as e:
       print(f"An error '{e}' occured during the file deleting process")
   

def mymainfunctionswitchingchoices():
 Menu()

 Choosedoption=int(input("Veuillez choisir une option : "))

 if Choosedoption==1:


  NameChoosed=str(input("Veuillez choisir un nom pour le fichier à créer : "))
  Creer_fichier(NameChoosed)

  

 elif Choosedoption==2:


   NameChoosed=str(input("Veuillez choisir le nom du fichier dans lequel écrire : "))
   Texte_ajout=str(input("Veuillez saisir le texte à ajouter dans le fichier: "))
   Ecrire_fichier(NameChoosed,Texte_ajout)
   
 elif  Choosedoption==3:


  NameChoosed=str(input("Veuillez choisir un nom pour le fichier à lire : "))
  Lire_Fichier(NameChoosed)
  
 elif Choosedoption==4:
   NameChoosed=str(input("Veuillez choisir un nom pour le fichier à supprimer : "))
   Supprimer(NameChoosed)
   
 elif Choosedoption==5:
  
  exit()



 else:
   print("Votre choix est invalide")



while True:

  mymainfunctionswitchingchoices()





    


