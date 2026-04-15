<?php
$conn = mysqli_connect("localhost","root","","voting_db");

if($_POST){
  $u = $_POST['username'];
  $p = $_POST['password'];

  mysqli_query($conn,"INSERT INTO users (username,password) VALUES ('$u','$p')");
  echo "Registered successfully!";
}
?>

<form method="POST">
<input type="text" name="username" placeholder="Enter username" required>
<input type="password" name="password" placeholder="Enter password" required>
<button type="submit">Register</button>
</form>

<br><br>

<a href="login.php">Back to Login</a>