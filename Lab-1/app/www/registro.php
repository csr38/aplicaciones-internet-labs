<!DOCTYPE html>
<head>
    <meta http-equiv="refresh" content="1; url=/">
</head>

<?php

    include 'conexion.php';

    $nombre = $_POST['nombre'];
    $nombre .= ' ' . $_POST['apellido'];

    

    $id = mysqli_query($conexion, "SELECT MAX(id) AS id FROM Person");

   
    $row = $id->fetch_assoc();

    $max_id = $row['id'] + 1;
    $insertar =mysqli_query($conexion, "INSERT INTO Person(id, name) VALUES ('$max_id', '$nombre')");


    if (!$insertar){
        echo 'Error al registrarse';

    }else {
        echo'Usuario registrado exitosamente';
    }

?>
</html>
