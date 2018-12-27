#!/bin/bash
# on <linea> 

#controlla il numero di parametri
if [ "$#" -lt 1 ]
then
    echo "on <linea>"
    exit
fi

./controllolinea.sh $1 on
