#!/bin/bash
# offonoff <linea> 

#controlla il numero di parametri
if [ "$#" -lt 2 ]
then
    echo "offonoff <linea> <secondi di on>"
    exit
fi

./controllolinea.sh $1 off
./controllolinea.sh $1 on
sleep $2
./controllolinea.sh $1 off
