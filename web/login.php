<?php
$err="";
if (isset($_POST["login"])) {
	session_start();
	$logindata = parse_ini_file("/etc/telecontrollo/tlc.ini");
	if($_POST["login"]==$logindata["user"] && $_POST["password"]==$logindata["password"])
	{
        	$_SESSION["user"]=$_POST["login"];
		header('Location: index.php');
    	    exit;
	}
    $err="Dati errati";
}
?>
<!DOCTYPE html>
<html lang="it">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="favicon.ico">
    <title>Login</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <link href="grid.css" rel="stylesheet">
  </head>

  <body>
    <div class="container">

      <div class="page-header">
        <h1>Telecontrollo Cisar - Prego autenticarsi</h1>
        <h2><?php echo $err; ?></h2>
        <p class="lead">Inserire nome utente e password</p>
      </div>
      <form name="form1" action="login.php" method="post">
  <div class="form-group">
    <label for="exampleInputEmail1">Nome utente</label>
    <input type="text" name="login" class="form-control" id="exampleInputEmail1" placeholder="nome utente">
  </div>
  <div class="form-group">
    <label for="exampleInputPassword1">Password</label>
    <input type="password" name="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
  </div>
        <button type="submit" class="btn btn-primary">Invio</button>
              </form>   

     
    </div> <!-- /container -->
  </body>
</html>
