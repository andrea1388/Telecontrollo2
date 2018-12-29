<?php
	$l=$_GET["linea"];
	$tempo=$_GET["tempo"];
	//$cmd=$_GET["stato"];
	exec("/usr/Telecontrollo2/controllolinea/offonoff.sh $l $tempo > /dev/null &",$op,$ret);
	echo "$l - $tempo - $ret - $op[0]";
?>