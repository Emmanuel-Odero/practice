<!DOCTYPE html>
<html>
<head>
	<title>If Statements</title>
</head>
<body>
	<?php 
		$isMale = true;
		$isTall = false;
		if ($isMale && $isTall){
			echo "You are a tall male.";
		}elseif($isMale && !$isTall){
			echo "You are a short male.";
		}elseif(!$isMale && $isTall){
			echo "Your are not male but tall.";
		}else {
			echo "You are not male and not tall.";
		};

	?>
</body>
</html>