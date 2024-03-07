function soulignerTexte(element) {
    element.style.textDecoration = "underline";
    element.style.textDecorationColor="rgb(65, 118, 65)";
  }
  
function enleverSoulignement(element) {
    element.style.textDecoration = "none";
  }

var monElement1 = document.getElementById("accueil");

monElement1.addEventListener("mouseover", function() {
  soulignerTexte(monElement1);
});

monElement1.addEventListener("mouseout", function() {
  enleverSoulignement(monElement1);
});

var monElement2 = document.getElementById("information");

monElement2.addEventListener("mouseover", function() {
  soulignerTexte(monElement2);
});

monElement2.addEventListener("mouseout", function() {
  enleverSoulignement(monElement2);
});

var monElement = document.getElementById("compte");

monElement.addEventListener("mouseover", function() {
  soulignerTexte(monElement);
});

monElement.addEventListener("mouseout", function() {
  enleverSoulignement(monElement);
});

var monElement3 = document.getElementById("identifier");

monElement3.addEventListener("mouseover", function() {
  soulignerTexte(monElement3);
});

monElement3.addEventListener("mouseout", function() {
  enleverSoulignement(monElement3);
});

