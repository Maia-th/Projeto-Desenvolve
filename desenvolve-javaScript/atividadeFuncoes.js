function soma(numero1, numero2) {
    return numero1 + numero2;
}

function subtrai(numero1, numero2) {
    return numero1 - numero2;
}

function multiplica(numero1, numero2) {
    return numero1 * numero2;
}

function divide(numero1, numero2) {
    return numero1 / numero2;
}

function mostraResultado (numero1,numero2){
    console.log(`Soma entre ${numero1} e ${numero2} =`, soma(numero1,numero2));
    console.log(`Subtração entre ${numero1} e ${numero2} =`, subtrai(numero1,numero2));
    console.log(`Multiplicação entre ${numero1} e ${numero2} =`, multiplica(numero1,numero2));
    console.log(`Divisão entre ${numero1} e ${numero2} =`, divide(numero1,numero2));
}

mostraResultado(10,5);