<?php
session_start();
$conn = mysqli_connect("localhost","root","","voting_db");

if(!isset($_SESSION['admin'])){
  header("Location: admin_login.php");
}
?>

<h2>Admin Panel</h2>

<h3>Add Candidate</h3>
<form method="POST">
<input type="text" name="name" placeholder="Candidate name" required>
<button type="submit" name="add">Add</button>
</form>

<?php
if(isset($_POST['add'])){
  $name = $_POST['name'];
  mysqli_query($conn,"INSERT INTO candidates(name) VALUES('$name')");
  echo "Candidate Added!";
}
?>

<h3>Results</h3>

<?php
$result = mysqli_query($conn,"SELECT * FROM candidates");

while($row = mysqli_fetch_array($result)){
  echo $row['name'] . " - Votes: " . $row['votes'] . "<br>";
}
?>

<br>
<a href="logout.php">Logout</a>