// Quelle: https://stackoverflow.com/questions/41654006/numpy-random-choice-in-javascript
function randomChoice(p) {
    var rnd = p.reduce(function (a, b) {
        return a + b;
    }) * Math.random();
    return p.findIndex(function (a) {
        return (rnd -= a) < 0;
    });
}


jQuery(document).ready(function($) {
    var speechElement = $("#etah-speech");

    $("#etah-generate").click(function() {
        speechElement.text("Text wird generiert, dies kann einige Sekunden dauern...");
        var request = new Request('http://lpp.sohnco.de/predict',
          { method: 'POST',
            body: {'name': 'Klaus'},
            headers: new Headers({ 'Content-Type': 'application/json' })
          });
        // Now use it!
        fetch(request)
          .then(response => response.json())
	  .then(data => speechElement.text(data.prediction))
          .catch(err => console.log(err)); 

    });

})
