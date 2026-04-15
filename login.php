<?php
session_start();
$conn = mysqli_connect("localhost","root","","voting_db");

if($_POST){
  $u = $_POST['username'];
  $p = $_POST['password'];

  $query = mysqli_query($conn,"SELECT * FROM users WHERE username='$u' AND password='$p'");
  $data = mysqli_fetch_array($query);

  if($data){
    $_SESSION['user'] = $data['username'];
    header("Location: vote.php");
  } else {
    echo "Invalid login!";
  }
}
?>

<form method="POST">
<input type="text" name="username" placeholder="Enter username" required>
<input type="password" name="password" placeholder="Enter password" required>
<button type="submit">Login</button>
</form>

<br><br>

<!-- FACE LOGIN -->
<a href="http://127.0.0.1:8000/face-login">
    <button>Login with Face</button>
</a>

<br><br>

<a href="register.php">Register</a>