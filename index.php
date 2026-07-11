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
    <label for="fname">First Name</label>
    <input type="text" id= "fname" name="first" >

    <label for="lname">Last Name</label>
    <input type="text" id="lname" name="last" > <br>
    <br>
    
    <label for="grade">Grade</label>
    <input type="text" id="grade" name="grade" >
    <br>
    <br>
    

    <label for="rolln">Roll No.</label>
    <input type="number" id="rolln" name="roll" min="1" >
    <br>
    <br>

<label>Gender:</label><br>

<input type="radio" id="male" name="gender" value="Male">
<label for="male">Male</label>

<input type="radio" id="female" name="gender" value="Female">
<label for="female">Female</label>

<input type="radio" id="other" name="gender" value="Other">
<label for="other">Other</label>
    <br>
    <br>

    <input type="submit" name="submit" value="Register">


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
    empty($_POST["roll"]) ||
    empty($_POST["gender"])
) {

    if(empty($_POST["first"]))
        echo "Enter your first name<br>";

    if(empty($_POST["last"]))
        echo "Enter your last name<br>";

    if(empty($_POST["grade"]))
        echo "Enter your grade<br>";

    if(empty($_POST["roll"]))
        echo "Enter your roll number<br>";
    
    if(empty($_POST["gender"]))
      echo "Select your gender<br>";

}
elseif ($_POST["roll"] <= 0) {

    echo "Roll number must be greater than 0.";

}
else {

    $first = $_POST["first"];
    $last = $_POST["last"];
    $grade = $_POST["grade"];
    $rollNo = $_POST["roll"];
    $gender = $_POST["gender"];

    $sql = "INSERT INTO information (FirstName, LastName, Grade, RollNo, Gender)
            VALUES ('$first', '$last', '$grade', '$rollNo', '$gender')";

    if (mysqli_query($conn, $sql)) {
    header("Location: index.php?success=1");
    exit();
}
  }

    }

  }
 mysqli_close($conn);
 ?>
