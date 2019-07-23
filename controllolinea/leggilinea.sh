#!/bin/bash
# leggilinea <linea>

#controlla il numero di parametri

if [ "$#" -ne 1 ]
then
    echo "leggilinea <linea>"
    exit
fi
l=$1 # il numero della linea da leggere

#legge lo stato attuale
cd /usr/Telecontrollo2/controllolinea
sl1=$(./leggilinee.sh)

out=$((sl1 & $l))
echo $out