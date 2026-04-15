<?php
session_start();
$conn = mysqli_connect("localhost","root","","voting_db");

if(!isset($_SESSION['user'])){
  header("Location: login.php");
}

$user = $_SESSION['user'];

// check vote status
$q = mysqli_query($conn,"SELECT * FROM users WHERE username='$user'");
$data = mysqli_fetch_array($q);

if($data['vote_status'] == 1){
  echo "You have already voted!";
  exit();
}

// vote submit
if($_POST){
  $candidate = $_POST['candidate'];

  mysqli_query($conn,"UPDATE candidates SET votes = votes + 1 WHERE id='$candidate'");
  mysqli_query($conn,"UPDATE users SET vote_status = 1 WHERE username='$user'");

  echo "Vote submitted successfully!";
  exit();
}
?>

<h2>Welcome <?php echo $user; ?></h2>

<form method="POST">
<input type="radio" name="candidate" value="1"> Candidate A <br>
<input type="radio" name="candidate" value="2"> Candidate B <br>
<input type="radio" name="candidate" value="3"> Candidate C <br><br>

<button type="submit">Vote</button>
</form>

<br>

<a href="logout.php">Logout</a>