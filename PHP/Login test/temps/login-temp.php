<?php

if (isset($_POST['submit'])) {
    
    $username = $_POST["uid"];
    $password = $_POST["password"];


    require_once 'dbh-temp.php'; require_once 'fonctions-temp.php';
    if (empty_input_login($username, $password) !== false) {
        header("location: ../login.php?error=emptyinput");
        exit();
    }
    login_user($conn, $username, $password);
}
else {
    header("location: ../login.php");
    exit();
}