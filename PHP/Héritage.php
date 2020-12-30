<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        class Cuisto{
            function poulet(){
                echo "Le cuisto fait du poulet <br>";
            }
            function salade(){
                echo "Le cuisto fait de la salade <br>";
            }
            function platDuJour(){
                echo "le cuisto fait des oeufs au plat";
            }


        }

        class ChefCuisto extends Cuisto{ #extends permet de récuperer les fonctions de la classe cuisto, on peut les écraser sans modifier l'original
            function platDuJour(){
                echo "Le cuisto fait une pizza";
            }

        }

        $cuisto = new cuisto();
        $cuisto->platDuJour();

        $chefcuisto = new ChefCuisto();
        $chefcuisto->platDuJour();
    ?>
</body>
</html>