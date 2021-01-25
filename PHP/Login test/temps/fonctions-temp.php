<?php
# création de fonctions de vérifications
function empty_input_signup($name, $email, $password, $pwdrepeat){
    $result;
    if (empty($name) || empty($email) || empty($password) || empty($pwdrepeat)) {
        $result = true;
    }
    else{
        $result = false;
    }
    return $result;
}
function invalid_username($name){
    $result;
    if (!preg_match("/^[a-zA-Z0-9]*$/", $name)) { #algorithme qui vérifie que le nom d'utilisateur a des lettres de a à z maj et min et chiffres de 0 à 9
        $result = true;
    }
    else{
        $result = false;
    }
    return $result;
}
function invalid_email($email){
    $result;
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) { #fonction built in permet de vérifier validité d'une adresse mail
        $result = true;
    }
    else{
        $result = false;
    }
    return $result;
}
function password_match($password, $pwdrepeat){
    $result;
    if ($password !== $pwdrepeat) {
        $result = true;
    }
    else{
        $result = false;
    }
    return $result;
}

function uid_email_exist($conn, $email, $name){
    $sql = "SELECT * FROM users WHERE usersUid = ? OR usersEmail = ?;"; # on prend les infos de la table users de la base de données
    $stmt = mysqli_stmt_init($conn); #sécurisation de la base de donnée sql, sinon l'user peut changer des choses dans notre base de données
    if (!mysqli_stmt_prepare($stmt, $sql)) {
        header("location: ../signup.php?error=stmtfailed");
        exit();
    }
    mysqli_stmt_bind_param($stmt, "ss", $name, $email); # s = string, ici on check 2 infos username et mail donc 2 s
    mysqli_stmt_execute($stmt);

    $resultData = mysqli_stmt_get_result($stmt);

    if ($row = mysqli_fetch_assoc($resultData)) { #on récupère les données sous forme d'associative array dans la variable $row
        return $row;
    }
    else{
        $result = false;
        return $result;
    }

    mysqli_stmt_close($stmt);
}

function create_user($conn, $name, $email){
    $sql = "INSERT INTO users (usersUid, usersEmail, usersPwd) VALUES (?, ?, ?)"; #on ajoute l'utilisateur dans la base de donnée
    $stmt = mysqli_stmt_init($conn); 
    if (!mysqli_stmt_prepare($stmt, $sql)) {
        header("location: ../signup.php?error=stmtfailed1");
        exit();
    }
    # on crypte le mot de pass en hash
    $modif_pwd = password_hash($password, PASSWORD_DEFAULT);

    #envoi des données à la base de données
    mysqli_stmt_bind_param($stmt, "sss", $name, $email, $modif_pwd); # ici on ajoute 3 infos donc 3 s.
    mysqli_stmt_execute($stmt);
    mysqli_stmt_close($stmt);
    header("location: ../signup.php?error=none");
}

function empty_input_login($username, $password){
    $result;
    if (empty($username) || empty($password)) {
        $result = true;
    }
    else{
        $result = false;
    }
    return $result;
}
function login_user($conn, $username, $password){
    $uid_exists = uid_email_exist($conn, $username , $username);
    
    if ($uid_exists === false) {
        header("location: ../login.php?error=wronglogin");
        exit();
    }

    $password_hashed = $uid_exists["usersPwd"];
    $check_password = password_verify($password, $password_hashed);
    if ($check_password === false) {
        header("location: ../login.php?error=$password et $password_hashed");
        exit();
    }
    else if ($check_password === true){
        session_start();
        # les sessions permettent de garder des variables en mémoire tout le temps de l'utilisation de la page web ex pas obligé de se reconnecter quand
        #on clique sur un onglet d'un site
        $_SESSION["userid"] = $uid_exists["usersId"];
        $_SESSION["useruid"] = $uid_exists["usersUid"];
        header("location: ../index.php");
        exit();
    }
}