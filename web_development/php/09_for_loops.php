<!DOCTYPE html>
<html>
<head>
	<title>For Loops</title>
</head>
<body>
	<?php
		$friends = array("Michael", "George", "Mildred", "Evans");

		for ($i=0; $i < count($friends); $i++) { 
			$current = $friends[$i];
			echo "My current friend is $current<br>";
		}
	?>
</body>
</html>