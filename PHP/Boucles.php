<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <?php

    $index = 1;
    while ($index <= 5) {              #Boucle While
    echo "$index <br>";
    $index ++;
    }

    $nombre_chance = array(4, 7, 10, 24, 9, 47);
    for($i = 0; $i <= count($nombre_chance); $i++){     #for loop ici on initialise notre variable, la condition, et le code a executer. Plus court et simple a lire
        echo "$nombre_chance[$i] <br>";
    }

    $index1 = 6;               #Boucle Do While = inverse, on execute le code et ensuite on vérifie la condition.
    do{
        echo "$index1 <br>"
    }while ($index1 <= 5);

    ?>



</body>
</html>


