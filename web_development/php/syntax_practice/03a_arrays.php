<!DOCTYPE html>
<html>
<head>
	<title>php Arrays</title>
</head>
<body>
	<?php 
		$friends = array("Michael", "George", "Mildred", "Evans");

		//getting the first element
		echo $friends[0];
		echo "<br>";


		//updating the second value
		$friends[1] = "Emily";
		echo $friends[1];
		echo "<br>";

		//getting the number of elements in array
		$totalFriends = count($friends);
		echo "There are a total of $totalFriends friends.";
		echo "<br>";
	?>
</body>
</html>