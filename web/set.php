<?php
	session_start();
	if (!isset($_SESSION['user'])) header('Location: login.php');
	$l=$_GET["linea"];
	$cmd=$_GET["stato"];
	exec("/usr/Telecontrollo2/controllolinea/controllolinea.sh $l $cmd",$op, $ret);
	echo "$l - $cmd - $ret - $op[0]";
?>