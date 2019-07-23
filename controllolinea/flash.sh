#!/bin/bash
# offonoff <linea> 

#controlla il numero di parametri
if [ "$#" -lt 2 ]
then
    echo "flash <linea> <secondi di flash>"
    exit
fi
cd /usr/Telecontrollo2/controllolinea

sl=$(./leggilinea.sh $1)

echo $sl

if [ $sl -eq "0" ]
then
./controllolinea.sh $1 on
sleep $2
./controllolinea.sh $1 off
else
./controllolinea.sh $1 off
sleep $2
./controllolinea.sh $1 on
fi
