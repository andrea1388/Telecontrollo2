/*
    controlla via i2c lo stato di 16 uscite collegate a degli i/o expander
    uso: controllolinea [<numero linea> <on|off|offonoff tempo]>
    senza parametri legge le uscite

    22/12/2018 Andrea Carrara iw3gcb
*/

var numparametri = process.argv.length;

if(numparametri>=4) leggilinee();
else {
    var cmd=process.argv[2].toLowerCase();
    if(cmd=="on")
}

