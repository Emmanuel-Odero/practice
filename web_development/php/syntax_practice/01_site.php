<!DOCTYPE html>
<html>
<head>
	<title>PHP Practice</title>
</head>
<body>
	<?php 
		echo("<h1>Karibu Techmates PHP Cheatsheet</h1>");
		echo"<hr>";
	?>


	<!-- Variables -->
	<?php 
		$topic = "Variables";
		$characterName = "Ochara";
		$characterAge = 80;
		echo"<h2><u>$topic</u></h2><br>";
		echo "There was once a man named $characterName <br>";
		echo "He was $characterAge years old <br>";
		echo "He really liked the name $characterName <br>";
		echo "But didn't like being $characterAge<br>";
	?>

	<!-- Data Types -->
	<?php
		$topic = "Data Types";
		echo"<h2><u>$topic</u></h2><br>";

		$stringType = "To be or not to be";
		$integerNumberType = 67;
		$floatNumberType = 56.34;
		$booleanType = true;
		$noValueType = null;

		echo "String -> $stringType <br>";
		echo "Integer or whole number type -> $integerNumberType <br>";
		echo "Float or decimal number type -> $floatNumberType <br>";
		echo "Boolean example -> $booleanType <br>";
		echo "Sting with no values -> $noValueType <br>";
	?>

	<!-- Working with Strings -->
	<?php 
		$topic = "Working with Strings";
		echo"<h2><u>$topic</u></h2><br>";

		$ourString = "Karibu Techmates is the Future";
		echo "The sting we are operating on is => $ourString <br>";

		echo "<br><b>1</b>Converting string to all lower case using strtolower()<br>";
		echo strtolower($ourString);
		echo "<br>";

		echo "<br><b>2</b>Converting string to all uppercase case using strtoupper()<br>";
		echo strtolower($ourString);
		echo "<br>";

		echo "<br><b>3</b>Knowing the number of characters in the string using strlen()<br>";
		echo strlen($ourString);
		echo "<br>";

		echo "<br><b>4</b>Getting the character at a particular index using 'stringname[indexOfInterest]' <br>";
		echo "Getting the first index.<br>";
		echo $ourString[0];
		echo "<br>";
		echo "Getting the tenth index.<br>";
		echo $ourString[9];
		echo "<br>";
		echo "Note that this takes account of the spaces within the string, best illustrated by tenth index above.<br>";

		echo "<br><b>5</b>We can also modify a particular character. eg 'stringName[indexOfInterest] = newCharacter'<br>";
		$ourString[0] = 'J';
		echo "$ourString";
		echo "<br>";

		echo "<br><b>6</b>Replacing a substring within a string. using a funtion str_replace(oldSubtring, newSubstring, actualString)<br>";
		echo "Reverting our string to the original string we started with<br>";
		echo "Our current string is => $ourString <br>";
		$ourUpdatedString = str_replace("Jaribu", "Karibu", $ourString);
		echo "Our updated string is => $ourUpdatedString <br>";

		echo "<br><b>7)</b> Grabbing a section of a string. Using 'substr(actualString, startIndex, stringCountAfterStartIndex)' <br>";
		echo "<strong>NB:</strong>If stringCountAfterStartIndex is not specified then by default all the characters aftwards are accounted for and included as substring. startIndex starts from 0. <br>";
		echo "Our current string => $ourUpdatedString <br>";
		$extractedSubstring = substr($ourUpdatedString, 7, 9);
		echo "Our extracted substring => $extractedSubstring<br>";

	?>

	<!-- Working with Numbers -->
	<?php 
		$topic = "Working with Numbers";
		echo"<h2><u>$topic</u></h2><br>";

		echo "<br> We can perform operations like addtion(+), subtraction(-), multiplication(*), division(/), modulus(%) <br>";
		echo "<b>NB:</b> php will follow the mathematical order of operation. BODMAS.<br><br>";
		echo "Increment and decrement of numbers using variableName++ and variableName-- respectively.<br>";
		$actualAge = 27;
		echo "Current actual age => $actualAge <br>";
		$actualAge++;
		echo "After increment Age => $actualAge <br>";

		echo "<br><b>3</b>Getting the absolute value of a number using abs()<br>";
		$currentNumber = -364;
		echo "The current number is => $currentNumber <br>";
		echo "Absolute value of the current number is => abs($currentNumber)<br>";

		echo "We can use pow(2, 4) for 2 raised to power 4, sqrt(), min(), max(), round(), ceil(), floor()";


	?>


</body>
</html>