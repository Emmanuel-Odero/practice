<!DOCTYPE html>
<html>
<head>
	<title>Php Practice</title>
</head>
<body>
	<!-- Getting User Input -->
	

	<form action="02_site.php" method="get">
		Name: <input type="text" name="name">
		<br>
		Age: <input type="number" name="age">
		<br>
		<input type="submit">
	</form>
	<br>

	<p>Your name is <?php echo $_GET["name"] ?> and you are <?php echo $_GET["age"]?> years old</p>

</body>
</html>