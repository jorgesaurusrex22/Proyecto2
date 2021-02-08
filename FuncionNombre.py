nom=[]
ed=[]
def IngresarNombreYEdad(Nombre,Edad):
    for i in range(5):
        while True:
            try:
                print('Ingrese Nombre y edad')
                Nombre=input()
                Edad=int(input())
                break
            except ValueError:
                print('Debe poner un número entero')
        nom.append(Nombre)
        ed.append(Edad)
def ImprimirNombreYEdad(impNom,impEd):
    for i in range(5):
        print('Nombre: '+impNom[i]+' Edad: '+str(impEd[i])+' años')
def EdadMayor(nomMay,edMay):
    edMayor = None
    nomMayor=None
    for i in range(5):
        if edMayor is None or edMay[i] > edMayor:
            edMayor=edMay[i]
            nomMayor=nomMay[i]
    print('La edad mayor es '+nomMayor+' con '+str(edMayor)+' años')
def EdadMenor(nomMen,edMen):
    edMenor=None
    nomMenor=None
    for i in range(5):
        if edMenor is None or edMen[i] < edMenor:
            edMenor=edMen[i]
            nomMenor=nomMen[i]
    print('La edad menor es ' + nomMenor + ' con ' + str(edMenor) + ' años')
def ordenarEdades(edOrd):
    for i in range(5):
        edOrd.sort()
        print(str(edOrd[i]))
def ordenarNombres(nomOrd):
    for i in range(5):
        nomOrd.sort()
        print(nomOrd[i])
IngresarNombreYEdad(nom,ed)
ImprimirNombreYEdad(nom,ed)
EdadMayor(nom,ed)
EdadMenor(nom,ed)
ordenarEdades(ed)