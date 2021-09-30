<!DOCTYPE html>
<html>
<head>
	<title>php Functions</title>
</head>
<body>
	<?php

		function sayHi($name, $age){
			echo "Hello $name, you are $age years.<br>";
		}

		sayHi("Michael", 80);
		sayHi("John", 43);
		sayHi("Alice", 13);


		//using return statement on functions
		function cube($num){
			return $num * $num * $num;
		}

		$results = cube(4);
		echo $results;

	?>
</body>
</html>