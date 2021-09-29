<!DOCTYPE html>
<html>
<head>
	<title>Inheritance</title>
</head>
<body>
	<?php
		class Chef{
			function makeChicken(){
				echo "The chef maks chicken <br>";
			}

			function makeSalad(){
				echo "The chef makes salad <br>";
			}
			function makeSpecialDish(){
				echo "The chef mkes bbq rios <br>";
			}
			
		}


		//Here we inherit all the functionality of the chef class to the Italian Chef
		class ItalianChef extends Chef{

			//function only applicable to the ItalianChef class.
			function makePasta(){
				echo "The chef makes pasta.<br>";
			}

			//we can also override a function within the chef class eeg we are overiding teh makespecialdibh
			function makeSpecialDish(){
				echo "The chef makes parm<br>";
			}

		}

		$chef = new Chef();
		$chef->makeChicken();
		$chef->makeSpecialDish();

		$italianChef =  new ItalianChef();
		$italianChef->makesalad();  //italianChef inherits makeSalad method form chef class.
		$italianChef->makeSpecialDish(); //function within chef class overriden with the ItaliaChef class

	?>
</body>
</html>