#!/bin/bash
# leggilinea <linea>

#controlla il numero di parametri

if [ "$#" -ne 1 ]
then
    echo "leggilinea <linea>"
    exit
fi
l=$1 # il numero della linea da leggere
b=$((2**$(($l-1))))

#legge lo stato attuale
cd /usr/Telecontrollo2/controllolinea
sl1=$(./leggilinee.sh)

out=$((sl1 & $b))

if [ $out -gt 1 ]
then
    out=1
fi

echo $out