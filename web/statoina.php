<?php
	session_start();
	if (!isset($_SESSION['user'])) header('Location: login.php');
	exec("/usr/Telecontrollo2/ina/ina2.py" ,$op, $ret);
	if ($ret==0) foreach($op as $o) echo $o . "<br>\n";
?>