<?php
    session_start();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <title>Login system</title>
</head>
<body>
    
    <header>
        <div class="topnav">
            <a href="index.php">Home</a>
            <?php
                if (isset($_SESSION["usersuid"])) {
                    echo "<a href="account.php">Mon Compte</a>";
                    echo "<a href="temps/logout.php">Déconnexion</a>";
                }
                else {
                    echo "<a href="signup.php">Sign up</a>"
                    echo "<a href="login.php">Login</a>"
                }
            ?>
            <a href="#about">About</a>
          </div>
    </header>

    <div class="wrapper">