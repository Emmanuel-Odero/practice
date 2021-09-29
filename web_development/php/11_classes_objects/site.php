<!DOCTYPE html>
<html>
<head>
	<title>Classes and Objects</title>
</head>
<body>
	<?php
		class Book {
			var $title;
			var $author;
			var $pages;

			
		}

		//creating an instance of the book class which is known as object
		$book1 = new Book('Mike');
		$book1->title = "Harry Potter";
		$book1->author = "JK Rowling";
		$book1->pages = "400";

		echo "The book $book1->title was writen by $book1->author and it has $book1->pages pages.";


		//using constructors
		class Student{
			//constructors : gets executed once the book is created from $book1 = new Book()
			function __construct($name, $major, $gpa){
				$this->name =$name;
				$this->major = $major;
				$this->gpa = $gpa;
			}

			//defining an object function
			function hasHonors(){
				if($this->gpa >= 3.5){
					return "true";
				}else{
					return "false";
				}
			}
		}

		//creating an instance of the student class with arugenments enabled by our constructer
		$student1 = new Student("Michael Ochara", "Computer science", 3.6);
		$student2 =  new Student("Alfred Ngalima", "Business", 2.8);
		echo "<br>Our top student is $student1->name who is a $student1->major major with gpa of $student1->gpa .";
		echo "<br>";

		//we can still modify the instances of a class for example name below
		$student1->name = "Ochara Michael";
		echo $student1->name;

		echo "<br> Using object function to know if a student has honors or not.<br>";
		$student1Honors = $student1->hasHonors();
		$student2Honors = $student2->hasHonors();
		echo "Does student 1 have honors : $student1Honors <br>";
		echo "Does student 2 have honors : $student2Honors <br>";
	?>

</body>
</html>