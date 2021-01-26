<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
    $est_riche  = True;
    $est_intelligent = True;
    if ($est_intelligent && $est_riche){ # and = &&, or dans php == ||, is not est !$est_riche. if elif les conditions se mettent entre () 
        echo "Tu est riche et intelligent";
    } else {
        echo "Tu n'est ni riche ni intelligent";
    }


    $personnes =  array("Wilfried", "Christophe", "Maxime", "Virginie"); # Les Arrays permettent de stocker une plus grande quantité d'information qu'une variable classique
    echo count($personnes);
    
    $fruits =$_POST["fruits"];
    echo $fruits[0];

    $notes = array("Maxime" => "20/20", "Wilfried" => "10/20"); # comme dictonnaire Python, ici Maxime est la clé et 20/20 est l'information
    echo $notes[$_POST["student"]] #ici on peut choisir quel personne on veut voir en rentrant son nom

    ?>

<!-- <form action="site.php" method="post">
            Apples: <input type="checkbox" name="fruits[]" value="apples"><br> <name= permet de donner un nom à la zone de texte pour qu'on puisse le référencer plus tard
            Student: <input type="text" name="student"><br> <!-- avec une checkbox, préciser dans le nom les [] pour signifier plusieurs choix 
            <input type="submit">
        </form>
    GET vs POST = get met l'input dans l'URL alors que post le camoufle.-->

</body>
</html>