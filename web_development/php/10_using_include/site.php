<!DOCTYPE html>
<html>
<head>
	<title>Using Include</title>
</head>
<body>
	<!-- including our header template -->
	<?php include "header.html" ?>

	<!-- importing functions from another file -->
	<?php 

	include "useful-tools.php"; 
	sayHi();


	?>
	<p>This is a site using the template of footer and header.</p>

	<!-- including our footer template -->
	<?php include "footer.html" ?>
</body>
</html>