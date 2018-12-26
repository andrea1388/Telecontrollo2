#!/bin/bash
# controllolinea <linea> <on|off>

#controlla il numero di parametri
if [ "$#" -lt 2 ]
then
    echo "controllolinea <linea> <on|off>"
    exit
fi

l=$1 # il numero della linea da comandare
cmd=$(echo "$2" | awk '{print tolower($0)}') # il comando (in minuscolo)
base=0x38 # indirizzo del primo pcf

#controlla che il numero di linea sia corretto
if [ "$l" -lt 1 ] || [ "$l" -gt 16 ]
then
    echo "1<= linea <= 16"
    exit
fi

#legge lo stato attuale
sl1=$(./leggilinee.sh)

# se linea > 8 usa l'altro pcf
if [ "$l" -gt 8 ]
then
    l=$(($l-8))
    base=$(($base+1))
    sl1=$(($sl1/256))
fi

if [ "$cmd" == "on" ] 
then
    b=$((2**$(($l-1))))
    out=$((sl1|$b))
    #echo i2cset -y 1 $base $out
    i2cset -y 1 $base $out
elif [ "$cmd" == "off" ]
then
    b=$((2**$(($l-1))))
    b=$((255-$b))
    out=$((sl1&$b))
    #echo i2cset -y 1 $base $out
    i2cset -y 1 $base $out
else
    echo "controllolinea <linea> <on|off>"
    exit
fi

./leggilinee.sh
