function redirectRistsõna() {
    window.location.pathname = "/ristsõna"
}

function redirectLeheküljest() {
    window.location.pathname = "/leheküljest"
}

function redirectKodu() {
    window.location.pathname = "/"
}

function printScreen() {
    const body = document.getElementById("body");
    const el0 = document.getElementById("print0");
    const el1 = document.getElementById("print1");
    const el2 = document.getElementById("print2");
    body.style.visibility = "hidden";
    el0.classList.add("print");
    el1.classList.add("print");
    el2.classList.add("print");

    window.print();

    body.style.visibility = "";
    el0.classList.remove("print");
    el1.classList.remove("print");
    el2.classList.remove("print");
}