# Proyecto-Sintetizador
![SynthUML](https://github.com/Caltafulla/Proyecto-Sintetizador/blob/main/TL9DZzCm4BtFhx3sr28IYKRYK75O188BK6bRSOsciRjOSZnbxFH0uB_ZZwPnO7jftvjvpvuypwFpo7xe3NG6dHFVF-n6kA0XRibAt8gJ8VJWTNzajHNQUZYnwWPbEutj4PsQ91SoGw_iqvUiokw3FbEx2n0-AwiOEUBL6lv0lcyMZ13XBhcSvrcHcvRI0Abr8ku7WotzSzOdRJpJ23z-pM.svg)

UML CODE
@startuml
class VCO{
valor_onda: float
timbre: int
frecuencia_base: float
volumenRL: int
onda: Tipo_Onda
GenerarOnda()
}

class Tipo_Onda{
TipoOnda: str
}

class Onda{
nombre: str
formula_onda()
}

class Filtro{
hz: float
tipo: str
pass(): void
}

class Sonido{
volumen: float
adsr: ADSR
adsrMetodo()
reproducirSonido()
}

class ADSR{
a: float
d: float
s: float
r: float
}

class Notas{
nota: float
}

class Teclado_generador_nota{
octavas: int
sensibilidad: int
TocarTeclas()
}

class Sine{
}
class Square{
}
class Triangle{
}

class VCO1{
}
class VCO2{
}
class VCO3{
}

Sonido -- VCO1
Sonido -- VCO2
Sonido -- VCO3
(Sonido, VCO1) .. Filtro
(Sonido, VCO2) .. Filtro
(Sonido, VCO3) .. Filtro
VCO <|- VCO1
VCO <|- VCO2
VCO <|- VCO3

Tipo_Onda -- VCO 
Sine -- Tipo_Onda
Square -- Tipo_Onda
Triangle -- Tipo_Onda
Onda <|-- Sine
Onda <|-- Square
Onda <|-- Triangle

Teclado_generador_nota - VCO
ADSR - Teclado_generador_nota
Teclado_generador_nota "36...n" *-- Notas
@enduml
