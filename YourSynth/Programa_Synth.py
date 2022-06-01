
#%%
from xmlrpc.client import boolean
import pygame
from VCO import VCO
from PianoM import piano
from SonidoP import SonidoP as sp
import sounddevice as sd

#Variables Globales
vco1 = VCO(0, 0, 0, 0, 0)
vco2 = VCO(0, 0, 0, 0, 0)
vco3 = VCO(0, 0, 0, 0, 0)
posx = 0
White = (255,255,255)
Negro = (33,33,33)
posy0 = 87

#Cambios de los botones
def ButtonChanges (VCO: VCO, y):
    global posy0
    if pygame.mouse.get_pressed()[0]:
        #Cambio de estado del VCO
        if pygame.mouse.get_pos()[0] >= 226 and pygame.mouse.get_pos()[1] >= posy0 + y and pygame.mouse.get_pos()[0] <= 296 and pygame.mouse.get_pos()[1]<= posy0 + 70 + y:
            SineVCO = pygame.image.load("ImageSources/SynthSelected-06.png")
            WIN.blit(SineVCO,[226,posy0 + y])
            SquareVCO = pygame.image.load("ImageSources/Synth-04.png")
            WIN.blit(SquareVCO,[323,posy0 + y])
            SawVCO = pygame.image.load("ImageSources/Synth-05.png")
            WIN.blit(SawVCO,[420,posy0 + y])
            VCO.onda = 1
        elif pygame.mouse.get_pos()[0] >= 323 and pygame.mouse.get_pos()[1] >= posy0 + y and pygame.mouse.get_pos()[0] <= 393 and pygame.mouse.get_pos()[1]<= posy0 + 70 + y:
            SineVCO = pygame.image.load("ImageSources/Synth-03.png")
            WIN.blit(SineVCO,[226,posy0 + y])
            SquareVCO = pygame.image.load("ImageSources/SynthSelected-07.png")
            WIN.blit(SquareVCO,[323,posy0 + y])
            SawVCO = pygame.image.load("ImageSources/Synth-05.png")
            WIN.blit(SawVCO,[420,posy0 + y])
            VCO.onda = 2
        elif pygame.mouse.get_pos()[0] >= 420 and pygame.mouse.get_pos()[1] >= posy0 + y and pygame.mouse.get_pos()[0] <= 490 and pygame.mouse.get_pos()[1]<= posy0 + 70 + y:
            SineVCO = pygame.image.load("ImageSources/Synth-03.png")
            WIN.blit(SineVCO,[226,posy0 + y])
            SquareVCO = pygame.image.load("ImageSources/Synth-04.png")
            WIN.blit(SquareVCO,[323,posy0 + y])
            SawVCO = pygame.image.load("ImageSources/SynthSelected-08.png")
            WIN.blit(SawVCO,[420,posy0 + y])
            VCO.onda = 3
        #Resetear iconos del VCO
        elif pygame.mouse.get_pos()[0] >= 9 and pygame.mouse.get_pos()[1] >= 107 + y and pygame.mouse.get_pos()[0] <= 41 and pygame.mouse.get_pos()[1]<=139 + y:
            SineVCO1 = pygame.image.load("ImageSources/Synth-03.png")
            WIN.blit(SineVCO1,[226,posy0 + y])
            SquareVCO1 = pygame.image.load("ImageSources/Synth-04.png")
            WIN.blit(SquareVCO1,[323,posy0 + y])
            SawVCO1 = pygame.image.load("ImageSources/Synth-05.png")
            WIN.blit(SawVCO1,[420,posy0 + y])
            VCO.onda = 0

pygame.init()
#Establecer:

#Dimensiones
WIN = pygame.display.set_mode((975, 720))

#Icono
pygame_icon = pygame.image.load("ImageSources/Icon_Mesa de trabajo 1.png")
pygame.display.set_icon(pygame_icon)

#Fondo
Fondo = pygame.image.load("ImageSources/Fondo_Mesa de trabajo 1 copia.png")
WIN.blit(Fondo,[0,0])

#Nombre de ventana
pygame.display.set_caption("Synth")


#BttIcons
#Wave Icons
#VCO1
SineVCO1 = pygame.image.load("ImageSources/Synth-03.png")
WIN.blit(SineVCO1,[226,87])
SquareVCO1 = pygame.image.load("ImageSources/Synth-04.png")
WIN.blit(SquareVCO1,[323,87])
SawVCO1 = pygame.image.load("ImageSources/Synth-05.png")
WIN.blit(SawVCO1,[420,87])

#VCO2
SineVCO2 = pygame.image.load("ImageSources/Synth-03.png")
WIN.blit(SineVCO2,[226,186])
SquareVCO2 = pygame.image.load("ImageSources/Synth-04.png")
WIN.blit(SquareVCO2,[323,186])
SawVCO2 = pygame.image.load("ImageSources/Synth-05.png")
WIN.blit(SawVCO2,[420,186])

#VCO3
SineVCO3 = pygame.image.load("ImageSources/Synth-03.png")
WIN.blit(SineVCO3,[226,285])
SquareVCO3 = pygame.image.load("ImageSources/Synth-04.png")
WIN.blit(SquareVCO3,[323,285])
SawVCO3 = pygame.image.load("ImageSources/Synth-05.png")
WIN.blit(SawVCO3,[420,285])

#ReloadIcons
ReloadVCO1 = pygame.image.load("ImageSources/Reload-09.png")
WIN.blit(ReloadVCO1,[9,107])
ReloadVCO2 = pygame.image.load("ImageSources/Reload-09.png")
WIN.blit(ReloadVCO2,[9,205])
ReloadVCO3 = pygame.image.load("ImageSources/Reload-09.png")
WIN.blit(ReloadVCO3,[9,303])

#Perilla de volumen
def ImprB(x):
    pygame.draw.rect(WIN,White,(732 + x,185,10,30))

def ButtonChangesP():
    global posx
    if pygame.mouse.get_pressed()[0]:
        if pygame.mouse.get_pos()[0] >= (732 + posx) and pygame.mouse.get_pos()[1] >= 185 and pygame.mouse.get_pos()[0] <= (742 + posx) and pygame.mouse.get_pos()[1]<=215:
            ImprB(pygame.mouse.get_pos()[0] - 732)
            posx = pygame.mouse.get_pos()[0] - 732

#Impresión del Piano
def ImprTecla():
    #Impresión Teclas Blancas
    for x in range (115,975-135,50):
        pygame.draw.rect(WIN,White,(x,430,50,250))

    #Impresión Separación Teclas
    for ln in range (165,840,50):
        pygame.draw.line(WIN,Negro,(ln,430),(ln,680),1)

    #Impresión Teclas Negras    
    cont = 1
    for y in range (150,840,50):
        if cont != 3 and cont != 7 and cont != 10 and cont != 14:
            pygame.draw.rect(WIN,Negro,(y,430,30,150))
            cont = cont + 1
        else:
            cont = cont + 1
       
    #Impresión Bordeado del Piano
    pygame.draw.line(WIN,Negro,(115,430),(865,430),1)
    pygame.draw.line(WIN,Negro,(865,430),(865,680),1)
    pygame.draw.line(WIN,Negro,(865,680),(115,680),1)
    pygame.draw.line(WIN,Negro,(115,680),(115,430),1)

def KeySound(chord):
    if pygame.key.get_pressed() [pygame.K_a]:
        print("Entro")
        sp.playN(sp.sonarO, chord, piano(1,4).frecuencia())
        return
    elif pygame.key.get_pressed() [pygame.K_s]:
        sp.playN(sp.sonarO, chord, piano(1,4).frecuencia())
    elif pygame.key.get_pressed() [pygame.K_d]:
        sp.playN(chord, piano(1,4).frecuencia())
    elif pygame.key.get_pressed() [pygame.K_f]:
        sp.playN(chord, piano(1,4).frecuencia())
    elif pygame.key.get_pressed() [pygame.K_g]:
        sp.playN(chord, piano(1,4).frecuencia())
    elif pygame.key.get_pressed() [pygame.K_h]:
        sp.playN(chord, piano(1,4).frecuencia())

sp.playN(sp.sonarO, [vco1.onda, vco2.onda, vco3.onda], piano(1,4).frecuencia())
    #Bucle infinito para actividad   
def main ():
    ImprB(0)
    run = True
    corx = 0
    while run:
        for event in pygame.event.get():
            #Llamado a Cambios en VCO
            ButtonChanges(vco1, 0)
            ButtonChanges(vco2, 99)
            ButtonChanges(vco3, 99*2)

            if pygame.mouse.get_pressed()[0]:
                if pygame.mouse.get_pos()[0] >= (732 + (corx)) and pygame.mouse.get_pos()[0] <= (742 + (corx)) and pygame.mouse.get_pos()[1] >= 185 and pygame.mouse.get_pos()[1]<=215:
                    if (732 <= pygame.mouse.get_pos()[0] - corx):
                        corx = pygame.mouse.get_pos()[0] - 732
                        ButtonChangesP()
                    else:
                        corx = -pygame.mouse.get_pos()[0] + 732
                        ButtonChangesP()
            
            #Llamado a Impresión de Piano
            ImprTecla()

            #Bucle de uso de teclas
            KeySound([vco1.onda, vco2.onda, vco3.onda])
            sd.sleep(10)

            #KeySound(vcog)

            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
# %%
