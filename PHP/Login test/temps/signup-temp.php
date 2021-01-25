<?php

if (isset($_POST["submit"])) { #isset vérifie si l'utilisateur a bien envoyé un formulaire de sign up et on lit chaque input.
    $name = $_POST["uid"];
    $email = $_POST["email"];
    $password = $_POST["password"];
    $pwdrepeat = $_POST["passwordrepeat"];

#on dis que les 2 fichiers php sont requis lors de l'éxecution
    require_once "dbh-temp.php"; require_once "fonctions-temp.php";

#on vérifie que chaque input 1 n'est pas vide et que : 
    if (empty_input_signup($name, $email, $password, $pwdrepeat) !== false) {
        header("location: ../signup.php?error=emptyinput");
        exit();
    }
#le nom d'utilisateur soit valide
    if (invalid_username($name)) {
        header("location: ../signup.php?error=invalidusername");
        exit();
    }
# l'email soit valide
    if (invalid_email($email)) {
        header("location: ../signup.php?error=invalidemail");
        exit();
    }
# les mots de passe correspondent
    if (password_match($password, $pwdrepeat) !== false) {
        header("location: ../signup.php?error=pwdnotmatch");
        exit();
    }
# le nom d'utilisateur n'existe pas déjà
    if (uid_email_exist($conn, $name, $email) !== false) {
        header("location: ../signup.php?error=usernametaken");
        exit();
    }
#ensuite on créer un utilisateur avec les données fournies
    create_user($conn, $name, $email, $password);
}
#sinon on fait retourner a la page de sign up
else {
    header("location : test/signup.php");
    exit();
}