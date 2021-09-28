<!DOCTYPE html>
<html>
<head>
	<title>While Loops</title>
</head>
<body>
	<?php
		$index = 1;
		while($index <= 5){
			echo "The index is $index <br>";
			$index++;
		}

		//do while loop does the same thing but runs the code befor checking the conditions
		echo "<br><br>Using do while loop<br>";
		$index = 6;
		do{
			echo "The index is $index<br>";
			$index++;
		}while($index <= 10);
	?>
</body>
</html>