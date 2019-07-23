<?php
	session_start();
	if (!isset($_SESSION['user'])) header('Location: login.php');
	exec("/usr/Telecontrollo2/controllolinea/leggilinee.sh" ,$op, $ret);
	if ($ret==0) echo $op[0];
?>