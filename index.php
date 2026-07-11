<?php 
 include("database.php");
 ?>



<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Student Registration Form</title>
</head>
<body>
  <form action="index.php" method="post">
    <h2> Student Enrollment Registration </h2>
    First Name:
    <input type="text" name="first" required>
    Last Name:
    <input type="text" name="last" required> <br>
    <br>
    
    Grade:
    <input type="text" name="grade" required>
    <br>
    <br>
    

    RollNo.:
    <input type="number" name="roll" min="1" required>
    <br>
    <br>
    <input type="submit" name="submit" value="register"> 


  </form>
</body>
</html>


 <?php
 

  if($_SERVER["REQUEST_METHOD"]=="POST"){
    if(isset($_POST['submit']))
    {
      if (
    empty($_POST["first"]) ||
    empty($_POST["last"]) ||
    empty($_POST["grade"]) ||
    empty($_POST["roll"])
) {

    if(empty($_POST["first"]))
        echo "Enter your first name<br>";

    if(empty($_POST["last"]))
        echo "Enter your last name<br>";

    if(empty($_POST["grade"]))
        echo "Enter your grade<br>";

    if(empty($_POST["roll"]))
        echo "Enter your roll number<br>";

}
elseif ($_POST["roll"] <= 0) {

    echo "Roll number must be greater than 0.";

}
else {

    $first = $_POST["first"];
    $last = $_POST["last"];
    $grade = $_POST["grade"];
    $rollNo = $_POST["roll"];

    $sql = "INSERT INTO information (FirstName, LastName, Grade, RollNo)
            VALUES ('$first', '$last', '$grade', '$rollNo')";

    if (mysqli_query($conn, $sql)) {
    header("Location: index.php?success=1");
    exit();
}
  }

    }

  }
 mysqli_close($conn);
 ?>
