<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php

    class Book{ #définition de la classe et de ses variables
            var $titre;
            var $auteur;
            var $pages;

            function __construct($unTitre, $unAuteur, $nbPages){ # on peut les définir dans le constructeur en passant des arguments, bcp plus rapide
                $this->titre = $unTitre;
                $this->auteur = $unAuteur;
                $this->pages = $nbPages;
            }
            function nbpages(){                     #fonction de classe
                if($this->pages >= 400){
                    return "true <br>";
                }
                return "false <br>";
            }
        }

    $book1 = new Book("Tropal Viandes", "Maxime", 400);  #on peut définir les variables une par une ou
    $book2 = new Book("Isitech", "Maxime", 800);

    #echo $book1->nbpages();
    #echo $book2->nbpages();
    
    class film{
        public $nom;                # public permet a tout le monde de modifier, var == public
        private $rating;            # variable private personne ne peux y modifier en dehors de la classe film

        function __construct($nomFilm, $unRating){
            $this->nom = $nomFilm;
            $this->setRating() = $unRating;
        }

        function getRating(){ #fonction getter
            return $this->rating;
        }
        function setRating($rating){  #fonction setter 
            if($rating == "G" || $rating == "PG" || $rating =="PG-13" || $rating == "R" || $rating == "NR"){
            }
        }

    }

    $avengers = new film("Avengers", "PG-13");
    $avengers = setRating("Dog");
    #$avengers->rating  ="Dog";  
    echo $avengers->getRating();       # en passant par une fonction contenue dans la classe on peut acceder au rating
    

    ?>
</body>
</html>