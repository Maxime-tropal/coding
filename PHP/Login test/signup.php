<?php 
    include_once "header.php"
?>

        <section class="sign-up-form">
            <div class="signup-form-style">
                <h2>Sign up</h2>
                <form action="temps/signup-temp.php" method="post">
                <input type="text" name="email" placeholder="e-Mail" >
                <input type="text" name="uid" placeholder="Nom d'utilisateur">
                <input type="password" name="password" placeholder="Mot de passe">
                <input style="margin-bottom: 10px;" type="password" name="passwordrepeat" placeholder="Retapez le mot de passe">
                <button type="submit" name="submit">Sign up</button>
                </form>
            </div>
            <?php
            if (isset($_GET["error"])) {
                if ($_GET["error"] == "emptyinput"){
                    echo "<p> Remplissez tout les champs ! </p>";
                }
                else if ($_GET["error"] == "invalidusername"){
                    echo "<p> Nom d'utilisateur invalide ! </p>";
                }
                else if ($_GET["error"] == "invalidemail"){
                    echo "<p> Email invalide ! </p>";
                }
                else if ($_GET["error"] == "pwdnotmatch"){
                    echo "<p> Les mots de passe ne correspondent pas ! </p>";
                }
                else if ($_GET["error"] == "usernametaken"){
                    echo "<p> Nom d'utilisateur déjà pris ! </p>";
                }
                else if ($_GET["error"] == "none"){
                    echo "<p> Inscription réussie ! </p>";
                }
                else if ($_GET["error"] == "stmtfailed"){
                    echo "<p> Oops ! </p>";
                }
                    }
            ?>
        </section>

<?php 
    include_once "footer.php"
?>