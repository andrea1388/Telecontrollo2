<?php
	$l=$_GET["linea"];
	$tempo=$_GET["tempo"];
	$cmd=$_GET["stato"];
	exec("/usr/Telecontrollo2/controllolinea/offonoff.sh $l $tempo",$op);
	echo "$l $cmd ret: $op[0]";
?>