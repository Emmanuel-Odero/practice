<!DOCTYPE html>
<html>
<head>
	<title>Switch Statement</title>
</head>
<body>
	<form action="07_switch_statement.php" method="get">
		What is your grade?<br>
		<input type="text" name="grade"><br>
		<input type="submit">
	</form>
	<?php
		$grade = $_GET["grade"];
		
		switch ($grade) {
			case 'A':
				echo "You did amazing!";
				break;
			case 'B':
				echo "You did pretty good!";
				break;
			case 'C':
				echo "You did poorly.";
				break;
			case 'D':
				echo "You did very bad.";
				break;
			case 'E':
				echo "You failed!";
				break;
			default:
				echo "Enter a valid grade.";
				break;
		}
	?>
</body>
</html>