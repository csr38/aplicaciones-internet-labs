<?php
    $servername = "mysql"; // Nombre del servicio del contenedor MySQL en Docker Compose
    $username = "root";
    $password = "root";
    $dbname = "dbname";
    $port = 3306;

    $conexion = new mysqli($servername, $username, $password, $dbname, $port);

    if ($conexion->connect_error) {
        die("Error de conexión: " . $conexion->connect_error);
    }

    echo "Conexión exitosa";
?>