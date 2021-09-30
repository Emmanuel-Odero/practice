<!DOCTYPE html>
<html>
<head>
	<title>php Arrays</title>
</head>
<body>
	<form action="04_checkboxes.php", method="post">
		Apple: <input type="checkbox" name="fruits[]" value="apple"><br>
		Oranges: <input type="checkbox" name="fruits[]" value="oranges"><br>
		Pears: <input type="checkbox" name="fruits[]" value="pears"><br>
		<input type="Submit">	
	</form>

	<?php 
		$fruits = $_POST["fruits"];
		echo $fruits[0];
	?>
</body>
</html>