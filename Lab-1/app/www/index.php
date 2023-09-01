
<html>
    <head>
        <title>Aplicaciones de Internet</title>
        <meta charset="utf-8">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
    </head>
    <body>
        <div class="container-fluid">
            <div class="row">
                <h1>Aplicaciones de Internet</h1>
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th></th>
                            <th>id</th>
                            <th>Nombre</th>
                            <th>Apellido</th>
                        </tr>
                    </thead>
                    <?php

                        include 'conexion.php';

                        $query = 'SELECT * From Person';
                        $result = mysqli_query($conexion, $query);

                        while($value = $result->fetch_array(MYSQLI_ASSOC)){
                            echo '<tr>';
                            echo '<td><a href="#"><span class="glyphicon glyphicon-search"></span></a></td>';
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
                    </table>
            </div>
        
            <form method="POST" action="registro.php">
                <div class="mb-3" >
                    <label for="exampleInputEmail1" class="form-label">Nombre</label>
                    <input type="text" class="form-control" name="nombre" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                    <label for="exampleInputPassword1" class="form-label">Apellido</label>
                    <input type="text" class="form-control" name="apellido">
                </div>

                <button type="submit" class="btn btn-primary" name="enviar">Enviar</button>
            </form>

        </div>
    </body>
</html>
