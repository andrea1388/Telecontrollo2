<?php
	session_start();
  	if (!isset($_SESSION['user'])) 
		header('Location: login.php');
	$linee = array("5V centralina meteo e rasp aerei", "24V connessione eolo","inutilizzato","ATV postazione","computer","link nazionale"
    ,"meteowebcam","?","mikrotik wifi","switch router lan","radio remota","videoserver + webcam","?","?","?","tasto accensione pc",);
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="favicon.ico">
    <title>Telecontrollo Cisar</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <link href="grid.css" rel="stylesheet">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.bundle.js"></script>

	<script>
		var myVar = setInterval(refresh, 1000);
		var myVar2 = setInterval(refresh2, 5000);
function refresh() {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() 
        {
            if (this.readyState == 4 && this.status == 200) 
            {
		    	var valore=this.responseText;
		    	var stato=parseInt(valore);
		    	var numerolinee= 4*(valore.length-2); 
		    	$("#tonto").text(stato + " " + numerolinee);
		    	for(i=0;i<numerolinee;i++)
		    	{
		    		var l=i+1;
		    		if ((stato & Math.pow(2, i)) >0 )
		    		{
		    			// la linea è accesa
		    			$("#jj" +i).text("Spegni");
						$("#jj" +i).attr('class', 'btn btn-danger');
						$("#jj" +i).attr("onclick","set("+l+",\"off\")");
						$("#kk" +i).attr("onclick","flash("+l+",4,0)");
						$("#ll" +i).attr("onclick","flash("+l+",60,0)");
		    		}
		    		else
		    		{
		    			$("#jj" +i).text("Accendi");
						$("#jj" +i).attr('class', 'btn btn-success');		    
						$("#jj" +i).attr("onclick","set("+l+",\"on\")");
						$("#kk" +i).attr("onclick","flash("+l+",4,1)");
						$("#ll" +i).attr("onclick","flash("+l+",60,1)");
						}
		    		
            		}
            }
        }
        xmlhttp.open("GET", "stato.php", true);
        xmlhttp.send();
}
function refresh2() {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() 
        {
            if (this.readyState == 4 && this.status == 200) 
            {
		    	var valore=this.responseText;
		    	$("#statoina").html(valore);
            }
        }
        xmlhttp.open("GET", "statoina.php", true);
        xmlhttp.send();
}
function set(linea,stato) {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.open("GET", "set.php?linea=" +linea+ "&stato="+stato, true);
        xmlhttp.send();
        setTimeout(refresh,50);
}
function flash(linea,tempo,stato) {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.open("GET", "flash.php?linea=" +linea+ "&tempo="+tempo+"&stato="+stato, true);
        xmlhttp.send();
        setTimeout(refresh,50);
}

	</script>
  </head>
<?php
	 exec("/usr/Telecontrollo2/controllolinea/leggilinee.sh" ,$op, $ret);
	 //echo $ret." --- ".$op[0]. "<br>";
	 if ($ret==0) {
	 	$numerolinee=4*(strlen($op[0])-2);
		$Statolinea=decodifica(base_convert(substr($op[0],2), 16, 10),$numerolinee);
	 }
	 function decodifica($stato,$bits)
	 {
	  for($i=0;$i<$bits;$i++)
	  {
	      $ret[$i]=0;
	      if($stato & pow(2,$i)) $ret[$i]=1;
        //echo $ret[$i]. "<br>";
	  }
	  return $ret;
	 }
?>
  <body>
  <form action="index.php" method="get">
    <div class="container">

      <div class="page-header">
        <h1>Telecontrollo Cisar</h1>
        <p class="lead">Controllo remoto delle uscite</p>
      </div>

      <h3>Stato linee</h3>
      <p>Premere il pulsante per esercitare la funzione corrispondente</p>
      <div class="row">
	  <?php
	  for($i=0;$i<$numerolinee;$i++) {
	  	$l=$i+1;
	  ?>
    	<div class="col-md-6" align="center">
    	<strong>Linea <?php echo "$l ($linee[$i])"; ?></strong><br>
    	<button type="button" id="jj<?php echo $i; ?>" class="btn btn-default" onclick="">...</button>
    	<button type="button" id="kk<?php echo $i; ?>" class="btn btn-info" onclick="">Flash 4s</button>
    	<button type="button" id="ll<?php echo $i; ?>" class="btn btn-info" onclick="">Flash 60s</button>
		</div>
	<?php
		 }
		?>
      </div>

    <label id="statoina">-</label>     
	<canvas id="myChart"></canvas>
    </div> <!-- /container -->
    </form>
  </body>
  <?php
			exec("/usr/Telecontrollo2/ina/leggidati.py" ,$op, $ret);
			//echo "ret=".$op[1]."<br>";
		?>
  <script>

		var ctx = document.getElementById('myChart').getContext('2d');
		var chart = new Chart(ctx, {
			// The type of chart we want to create
			type: 'line',

			// The data for our dataset
			data: {
				labels: ['-6', '-5', '-4', '-3', '-2', '-1', 'now'],
				datasets: [{
					label: 'Tensione batteria',
					fill: false,
					backgroundColor: 'rgb(255, 99, 132)',
					borderColor: 'rgb(255, 99, 132)',
					//data: [11.4,12,12,12.1,11.8,12,12.1]
					data: <?php echo $op[1]; ?>
				}]
			},

			// Configuration options go here
			options: {
				scales: {
					yAxes: [{
						ticks: {
							min: 4,
							max: 14
						}
					}]
				}
    		}
		});
	</script>
</html>
