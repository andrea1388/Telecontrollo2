# Telecontrollo2
Controllo remoto di 16 relais, tramite interfaccia web, ssh e toni dtmf. Per sistemi remoti

Il sistema è basato su una raspberry e permette di controllare da remoto lo stato di 16 uscite collegate ad altrettanti relays. Il controllo può essere fatto in 3 modi:
1) via web, tramite un web server installato sulla raspberry
2) via ssh, da linea di comando, dando dei comandi tipo controllolinea 6 off
3) tramite l'invio di toni dtmf, da inviare via radio. Alla raspberry è infatti collegata una scheda che decodifica i toni dtmf. Questa è collegata ad una radio.

Il software prevede alcuni componenti:
1) un server che riceve i comandi dal decoder dtmf, li elabora ed esegue i comandi
2) un interfaccia a linea di comando per leggere/scrivere le uscite
3) alcune pagine php, servite da apache, che leggono/scrivono le uscite

