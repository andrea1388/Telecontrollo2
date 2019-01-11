<?php
	 exec("/usr/Telecontrollo2/ina/ina2.py" ,$op, $ret);
	 if ($ret==0) foreach($op as $o) echo $o . "<br>\n";
?>