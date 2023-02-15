import os

class Folder:

    def __init__(self,name , path , convert_decision):
        self.name = name
        self.path = path
        self.descicion = convert_decision
    
    def create_folders (self):

        dir = ('video' ,  'audio' , 'docs' , 'conv_mp3')

        os.mkdir(os.path.join( self.path , self.name))

        for folders in dir:
            os.mkdir(os.path.join(self.path , self.name , folders))
        print("Folders creados")










name_folder = input("Ingrese el nombre de la carpeta: ")
path = input("Ingresar dirección de carpeta: ")
path.strip()
convert_decision = input("¿ Desea conversión a mp3 automaticamente ? (Y/n)")

folder =  Folder(name_folder , path , convert_decision)
folder.create_folders()