#!/bin/bash
# off <linea> 

#controlla il numero di parametri
if [ "$#" -lt 1 ]
then
    echo "off <linea>"
    exit
fi

./controllolinea.sh $1 off
