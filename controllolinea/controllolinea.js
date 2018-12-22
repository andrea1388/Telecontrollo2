/*
    controlla via i2c lo stato di 16 uscite collegate a degli i/o expander
    uso: controllolinea [<numero linea> <on|off|offonoff tempo]>
    senza parametri legge le uscite

    22/12/2018 Andrea Carrara iw3gcb
*/
const i2c = require('i2c-bus');
const PCF1 = 0x48;
const PCF2 = 0x49;

var numparametri = process.argv.length;
setlinea(1,1);

/*
if(numparametri>=4) leggilinee();
else {
    var cmd=process.argv[2].toLowerCase();
    if(cmd=="on")
}
*/

function setlinea(linea, valore) {
    var add=PCF1;
    var bit=linea-1;
    il (linea>8) 
    {
        add=PCF2;
        bit=linea-8;
    }
    var val=i2c1.receiveByteSync(add);
    if(valore==true)
        i2c1.sendByteSync(add, val | Math.pow(2,bit));
    else
        i2c1.sendByteSync(add, val & (255-Math.pow(2,bit));
}