<?php
session_start();

$user = $_GET['user'];
$_SESSION['user'] = $user;

header("Location: vote.php");
?>