<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
   

    <?php
        $note = $_POST["note"]
        switch($note){
            case "18":
                echo "très bonne note";
                break;
            case "10":
                echo "note passable";
                break;
        }
        function say_hi($name){  #fonctions pareil que dans Python, au lieu de : utiliser {} pour contenir la fonction, les arguments utilisent $.
            echo "Hello $name";
        }

        say_hi("Maxime <br>");
        say_hi("Maxime1 <br>");
        say_hi("Maxime2 <br>");
        say_hi("Maxime3 <br>");
        say_hi("Maxime5 <br>");

        function add($num){
            return $num * 5;
        }
    ?>

</body>
</html>
