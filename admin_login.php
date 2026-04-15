<form method="POST">
<input type="text" name="username" placeholder="Admin username">
<input type="password" name="password" placeholder="Password">
<button type="submit">Login</button>
</form>

<?php
session_start();
$conn = mysqli_connect("localhost","root","","voting_db");

if($_POST){
  $u = $_POST['username'];
  $p = $_POST['password'];

  $q = mysqli_query($conn,"SELECT * FROM admin WHERE username='$u' AND password='$p'");
  $data = mysqli_fetch_array($q);

  if($data){
    $_SESSION['admin'] = $u;
    header("Location: admin_panel.php");
  } else {
    echo "Invalid admin login!";
  }
}
?>