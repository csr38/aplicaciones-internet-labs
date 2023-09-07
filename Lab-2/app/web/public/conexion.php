<?php
    $servername = "mysql"; // Nombre del servicio del contenedor MySQL en Docker Compose
    $username = "root";
    $password = "root";
    $dbname = "dbname";
    $port = 3306;

    $conn = new mysqli($servername, $username, $password, $dbname, $port);

    if ($conn->connect_error) {
        die("Error de conexión: " . $conn->connect_error);
    }

    echo "Conexión exitosa";

    // Cierra la conexión al finalizar tu código
    $conn->close();
?>