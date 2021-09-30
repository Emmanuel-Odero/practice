<!DOCTYPE html>
<html>
<head>
	<title>Associative Arrays</title>
</head>
<body>
	<!-- Associative Arrays -->

	<?php 
		$grades = array('Jim'=>"A+", 'Pam'=>"B-", "Oscar"=>"c+", "Milka"=>"B+");
		echo $grades["Jim"];
		echo "<br><br>";

		//getting the number of key mappings
		$totalStudents = count($grades);
		echo "There are a total of $totalStudents students graded.";

	?>

	<!-- Getting user input then quering the associative array. -->
	<form action="03b_associativeArrays.php" method="post">
		<p>Search Student grade.</p>
		Student:<input type="text" name="student"><br>
		<input type="submit">
	</form>

	<?php
		$grades = array('Jim'=>"A+", 'Pam'=>"B-", "Oscar"=>"c+", "Milka"=>"B+");
		$studentName = $_POST["student"];
		echo $grades[$studentName];
	?>


</body>
</html>