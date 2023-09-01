<?php

$conexion = mysqli_connect('db', 'root', 'test', "dbname");
   if (!$conexion){
        echo 'Error al conectar a la base de datos';
    }
?>