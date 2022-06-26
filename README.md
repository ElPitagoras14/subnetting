# IP Segmentation Algorithm

## Tabla de Contenidos

1. [Descripción](#descripción)
2. [Uso](#uso)
    - [FLSM por red](#flsm-por-redes-mínimas)
    - [FLSM por host](#flsm-por-host-mínimos)
    - [VLSM host ordenado](#vlsm-por-host-ordenados)
    - [VLSM host](#vlsm-por-host)
    - [Mostrar por consola](#imprimir-por-consola)
    - [Guardar en un archivo](#guardar-en-un-archivo)
3. [Términos y Ecuaciones](#términos-y-ecuaciones)
4. [FLSM](#flsm-fixed-length-subnet-mask)
    - [Algoritmo](#algoritmo)
    - [Ejemplo](#ejemplo)
5. [VLSM](#vlsm-variable-length-subnet-mask)
    - [Algoritmo](#algoritmo-1)
    - [Ejemplo](#algoritmo-1)


## Descripción

Código escrito en python donde se emplea el algoritmo para la segmentación de IP con las técnicas FLSM y VLSM.

## Uso

Para hacer uso de las funciones de FLSM y VLSM hay 4 opciones y 2 funciones para presentar las subredes. Adicionalmente hay un código de ejemplo en `./ejercicio.py`.

Todos las funciones evuelven un diccionario donde la clave es el número de red y el valor una lista con la ip de subred, nueva máscara e ip de broadcast.

### FLSM por redes mínimas

Realiza subnetting con la técnica FLSM pasando como argumentos la ip inicial, la máscara de la red y la cantidad de redes mínimas que necesita.

```python
def red_FLSM(ip: str, mascara: int, redes_minima: int):
    #method
```

### FLSM por host mínimos

Realiza subnetting con el técnica FLSM pasando como argumentos la ip inicial, la máscara de la red y la cantidad de host mínimos que necesita.

```python
def host_FLSM(ip: str, mascara: int, host_minimo: int):
    #method
```

### VLSM por host ordenados

Realiza subnetting con el técnica VLSM pasando como argumentos la ip inicial, la máscara de la red y una lista de la cantidad de host por red necesaria. 

Adicionalmente esta función ordena la lista antes de realizar el subnetting.

```python
def host_ord_VLSM(ip: str, mascara: int, lista: list):
    #method
```

### VLSM por host

Realiza subnetting con el técnica VLSM pasando como argumentos la ip inicial, la máscara de la red y una lista de la cantidad de host por red necesaria. 

Es necesario que se haya hecho el arbol de direccionamiento para que la lista tenga consistencia con los host y redes.

```python
def host_VLSM(ip: str, mascara: int, lista: list):
    #method
```

### Imprimir por consola

Esta función muestra por consola una tabla con el subnetting realizado por alguno de las funciones previas. 

Recibe como argumentos el diccionario de subnetting y opcionalmente una lista de string paralela a la cantidad de items del diccionario para mostrar cada red con un nombre personalizado sino imprime **Red i**.

```python
def print_subnets(dic_redes: dict, nombres: list = None):
    #method
```

### Guardar en un archivo

Esta función guarda en un archivo una tabla con el subnetting realizado por alguno de las funciones previas. 

Recibe como argumentos el diccionario de subnetting, opcionalmente una lista de string paralela a la cantidad de items del diccionario para guardar cada red con un nombre personalizado sino imprime **Red i** y opcionalmente un directorio donde guardarlo.

```python
def write_subnets(dic_redes: dict, nombres: list = None, path: str = "./redes.txt"):
    #method
```

## Términos y Ecuaciones

- Número de bits de subred = $n$
- Número de bits de host = $m$
- $32=MascaraAnterior + n + m$
- Número de subredes = $2^n$
- Tamaño de bloque = $2^m$
- Número de host utilizables = $2^n-2$
- $NewMask=LastMask+n$

## FLSM (Fixed Length Subnet Mask)

Se requiere que la división de la red sea en bloques fijos, es decir, la misma cantidad de host en cada subred.

### Algoritmo

1. Se determina los valores de $n$ y $m$ con las ecuaciones anteriores.
2. Se determina la nueva mascara mediante $LastMask+n$
3. Se calcula cómo va a crecer la IP en caso de que el numero de host por subred sea mayor a $256$ dividiendo $2^m/256$. Caso contrario solo se aumenta el numero de host a la nueva subred con la nueva máscara.

### Ejemplo

Se requieren **14 host por subred** para la dirección **199.6.14.0/25.** 

$$
32=n+m+25\rightarrow n+m=7;
$$

$$
2^m-2\ge 14\rightarrow m=4\rightarrow n=3
$$

$$
Mask=25+n\rightarrow n=28
$$

|IP|Máscara|Subred|Broadcast|
|--|-------|------|---------|
|199.6.14.0|28|199.6.14.0|199.6.14.15|
|199.6.14.16|28|199.6.14.16|199.6.14.31|
|199.6.14.32|28|199.6.14.32|199.6.14.47|
|199.6.14.48|28|199.6.14.48|199.6.14.63|
|...|28|...|...|
|199.6.14.112|28|199.6.14.112|199.6.14.127|

## VLSM (Variable-Length Subnet Mask)

Se requiere que la división de la red sea en bloques de tamaño variable, es decir, puede haber distintas cantidad de host en cada subred.

El proceso de VLSM es similar a realizar FLSM para cada nueva subred.

### Algoritmo

1. Ordenar de mayor a menor las subredes dependiendo de la cantidad de host de cada una.
2. Para la primera subred determinar $n$ y $m$ a partir de las ecuaciones anteriores.
3. Obtener la nueva máscara de red sumando la máscara previa con n.
4. Tener anotada la dirección IP de la siguiente subred.
5. Repetir los pasos 2 a 4 para las siguientes subredes

### Ejemplo

Se necesita una **red de 100, 50, 25 y 25 host.** A partir de la **dirección IP 200.10.100.0/24.**

|IP|Host|n|m|Máscara|Subred|Broadcast|
|--|----|-|-|-------|------|---------|
|200.10.100.0|100|1|7|25|2000.10.100.0|200.10.100.127|
|200.10.100.128|50|1|6|26|200.10.100.128|200.10.100.191|
|200.10.100.192|25|1|5|27|200.10.100.192|200.10.100.223|
|200.10.100.224|25|0|5|27|200.10.100.224|200.10.100.255|