#!/bin/bash
# off <linea> 

#controlla il numero di parametri
if [ "$#" -lt 1 ]
then
    echo "off <linea>"
    exit
fi
cd /usr/Telecontrollo2/controllolinea

./controllolinea.sh $1 off
