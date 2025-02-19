<!DOCTYPE html>
<html lang="es">
<head>
    <title>Aplicaciones de Internet</title>
    <meta charset="utf-8">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
</head>
<body>
    <div class="container">
        <div class="row">
            <h1>Aplicaciones de Internet</h1>
            <table class="table table-striped" id="tabla-usuarios">
                <thead>
                    <tr>
                        <th>id</th>
                        <th>Nombre</th>
                        <th>Apellido</th>
                    </tr>
                </thead>
                <tbody>
                <?php
                    include 'conexion.php';

                    $query = 'SELECT * From Person';
                    $result = mysqli_query($conexion, $query);

                    while($value = $result->fetch_array(MYSQLI_ASSOC)){
                        echo '<tr>';
                        foreach($value as $element){
                            $porcion = explode(" ", $element);
                            foreach($porcion as $elemento){
                                echo '<td>' . $elemento . '</td>';
                            }
                        }

                        echo '</tr>';
                    }

                    $result->close();
                    mysqli_close($conexion);
                    ?>
                </tbody>
            </table>
        </div>
        <div class="row">
            <form id="formulario">
                <div class="mb-3">
                    <label class="form-label">Nombre</label>
                    <input type="text" class="form-control" name="nombre" id="nombre">
                </div>
                <div class="mb-3">
                    <label class="form-label">Apellido</label>
                    <input type="text" class="form-control" name="apellido" id="apellido">
                </div>
                <button type="button" class="btn btn-primary" onclick="agregarUsuario()">Agregar</button>
                
            </form>
        </div>
    </div>



    <?php

        include 'conexion.php';

       
    ?>


    <script src="script.js"></script>
</body>
</html>
