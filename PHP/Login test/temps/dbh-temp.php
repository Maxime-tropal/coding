<?php 
# on défini le nom du serveur, mdp et nom de la base de donnée 
$servername = "localhost";
$dBUsername = "root";
$dBPassword = "";
$dBName = "test";

$conn = mysqli_connect($servername, $dBUsername, $dBPassword, $dBName); #variable qui fait la connexion avec la base de données

if (!$conn) { #si il y a une erreur de connection arrêt + message
    die("Connection failed: " . mysqli_connect_error());
}