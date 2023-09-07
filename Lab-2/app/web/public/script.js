// Contador para IDs
var idContador = 2;

// Función para agregar un usuario a la tabla
function agregarUsuario() {
    var nombre = document.getElementById("nombre").value;
    var apellido = document.getElementById("apellido").value;

    if (nombre && apellido) {
        // Crea una nueva fila en la tabla
        var tabla = document.getElementById("tabla-usuarios").getElementsByTagName('tbody')[0];
        var newRow = tabla.insertRow(tabla.rows.length);

        // Asigna un nuevo ID único a la fila
        newRow.setAttribute("data-id", idContador);

        // Crea las celdas de la fila
        var cellId = newRow.insertCell(0);
        var cellNombre = newRow.insertCell(1);
        var cellApellido = newRow.insertCell(2);

        // Llena las celdas con datos
        cellId.innerHTML = idContador;
        cellNombre.innerHTML = nombre;
        cellApellido.innerHTML = apellido;

        // Incrementa el contador de IDs
        idContador++;

        // Limpia los campos de entrada
        document.getElementById("nombre").value = "";
        document.getElementById("apellido").value = "";
    } else {
        alert("Por favor, ingrese un nombre y un apellido.");
    }
}