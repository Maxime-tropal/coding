<?php 
    include_once "header.php"
?>
    <section class="sign-up-form">
        <div class="signup-form-style">
            <h2>Login</h2>
            <form action="temps/login-temp.php" method="post">
            <input type="text" name="uid" placeholder="Nom d'utilisateur ou e-mail">
            <input type="password" name="password" placeholder="Mot de passe">
            <button style="margin-bottom: 10px;" type="submit" name="submit">Log in</button>
            </form>
        </div>
        <?php
            if (isset($_GET["error"])) {
                if ($_GET["error"] == "emptyinput"){
                    echo "<p> Remplissez tout les champs ! </p>";
                }
                else if ($_GET["error"] == "wronglogin"){
                    echo "<p> Mot de passe ou utilisateur incorrect ! </p>";
                }
            }
            ?>
    </section>

<?php 
    include_once "footer.php"
?>