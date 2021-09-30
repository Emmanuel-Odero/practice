<!DOCTYPE html>
<html>
<head>
	<title>Getters and Setters</title>
</head>
<body>
	<?php

		class Movie{

			//note that var and public are in most cases interchangible
			//the public visibility modifier inplies that this attribte is open to the world and can be accessed and changed from anywhere

			//the private visibility modifier implies that the attribute is private to 					movie class and cannot be modified outside this class.	
			public $title; 
			private $rating; 

			function __construct($title, $rating){
				$this->title = $title;
				$this->setRating($rating);
			}

			//we define an object function which can allow us to get the private attribute rating
			//this is the getter.
			function getRating(){
				return $this->rating;
			}

			//we define an object function which can allow us to set the private attributer rating
			//this is the setter function which also dictates the possible values that can be set
			function setRating($rating){
				$allowedRatings = array("G", "PG", "PG-13", "R", "NR");
				if (in_array($rating, $allowedRatings)) {
					$this->rating = $rating;	
				}else {
					$this->rating = "NR";
				}
				
			}
		}


		$avengers = new Movie("Avengers", "G");

		//getting the rating
		echo $avengers->getRating();
		echo "<br>";
		echo $avengers->setRating("PG");
		echo "<br>";
		echo $avengers->getRating();
	?>
</body>
</html>