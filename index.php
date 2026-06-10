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
    <input type="text" name="first">
    Last Name:
    <input type="text" name="last"> <br>
    <br>
    
    Grade:
    <input type="text" name="grade">
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
      if(empty($_POST["first"])){
        echo "Enter your first name". "<br>";
      }
      if(empty($_POST["last"])){
        echo "Enter your last name" . "<br>";
      }
      
      if(empty($_POST["grade"])){
        echo "Enter your grade" . "<br>";
      }
      else{
        $first= $_POST['first'];
        $last= $_POST['last'];
        $grade= $_POST['grade'];
        $sql= "INSERT INTO information (FirstName, LastName,  Grade)
               VALUES ('$first', '$last',  '$grade')";
        mysqli_query($conn, $sql);
        echo" Student enrollment successful";
        
      }
    }

  }
 mysqli_close($conn);
 ?>
