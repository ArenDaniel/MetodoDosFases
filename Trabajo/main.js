var intentos = 2;
window.addEventListener('load', inicio, false);

function inicio() {
    document.getElementById('palabra1').addEventListener('dragstart', dragInicio, false);
    document.getElementById('palabra2').addEventListener('dragstart', dragInicio, false);
    document.getElementById('palabra3').addEventListener('dragstart', dragInicio, false);
    document.getElementById('palabra4').addEventListener('dragstart', dragInicio, false);
    document.getElementById('palabra5').addEventListener('dragstart', dragInicio, false);
    document.getElementById('palabra6').addEventListener('dragstart', dragInicio, false);

    document.getElementById('recuadro1').addEventListener('dragover', permitirDrop, false);
    document.getElementById('recuadro1').addEventListener('drop', drop, false);

    document.getElementById('recuadro2').addEventListener('dragover', permitirDrop, false);
    document.getElementById('recuadro2').addEventListener('drop', drop, false);

    document.getElementById('recuadro3').addEventListener('dragover', permitirDrop, false);
    document.getElementById('recuadro3').addEventListener('drop', drop, false);

    document.getElementById('recuadro4').addEventListener('dragover', permitirDrop, false);
    document.getElementById('recuadro4').addEventListener('drop', drop, false);

    document.getElementById('recuadro5').addEventListener('dragover', permitirDrop, false);
    document.getElementById('recuadro5').addEventListener('drop', drop, false);

    document.getElementById('recuadro6').addEventListener('dragover', permitirDrop, false);
    document.getElementById('recuadro6').addEventListener('drop', drop, false);
}

function dragInicio(ev) {
    ev.dataTransfer.setData("Text", ev.target.id);
}

function drop(ev) {
    //tid = ev.target.id;
    ev.preventDefault();
    var dato = ev.dataTransfer.getData("Text");
    ev.target.appendChild(document.getElementById(dato));
    document.getElementById(dato).removeEventListener('dragstart', dragInicio, false);
    ev.target.style.background = "rgb(255,255,0)";
    //document.getElementById(e.target.style).style.background = "rgb(255,255,0)";   
    validarCampos(ev)
}
function permitirDrop(ev) {
    ev.preventDefault();
}
function validarCampos(ev) {
    console.log("Entrada");
    var contador = 0

    for (let i = 1; i <= 6; i++) {
        let auxRecuadro = "recuadro" + i;

        for (let j = 1; j <= 6; j++) {
            let auxPalabra = "palabra" + j;
            if (document.getElementById(auxPalabra).parentNode.id == auxRecuadro) {
                console.log("Si")
                contador = contador + 1;
            }
        }
    }
    if (contador == 6) {
        alert("Ha llenado todos los campos");
        document.getElementById("boton").style.display = "block";
    }
}
function validarColor(ev) {
    var contadorpositivos = 0;

    for (let index = 1; index <= 6; index++) {
        let auxPalabra = "palabra" + index;
        let auxRecuadro = "recuadro" + index;
        checkElement(auxPalabra, auxRecuadro);
        if (document.getElementById(auxPalabra).parentNode.id == auxRecuadro) {
            contadorpositivos = contadorpositivos + 1;
        }
    }
    alert(contadorpositivos);
}
function checkElement(id, recuadro) {
    let color = "red";
    if (document.getElementById(id).parentNode.id == recuadro) {
        color = "green";
        console.log("set");
    } else {
    }
    document.getElementById(recuadro).style.background = color;
}