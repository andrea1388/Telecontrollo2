<?php
	$l=$_GET["linea"];
	$cmd=$_GET["stato"];
	exec("/usr/Telecontrollo2/controllolinea/controllolinea.sh $l $cmd",$op);
	echo "$l $cmd ret: $op[0]";
?>