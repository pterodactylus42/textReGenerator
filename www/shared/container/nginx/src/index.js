async function fetchJsonData(req) {
  try {
      const response = await fetch(req);
      if (!response.ok) {
          throw new Error('Network response was not ok');
      }
      const data = await response.json();
      return data;
  } catch (error) {
      console.error('There was a problem with the fetch operation:', error);
  }
}

async function fetchSeed() {
  var seed_request = new Request('http://localhost:8080/seed',
  { method: 'POST',
    body: {'options': 'standard'},
    headers: new Headers({ 'Content-Type': 'application/json' })
  });
  return fetchJsonData(seed_request)
}

async function fetchNudge(json_sequence) {
  var nudge_request = new Request('http://localhost:8080/nudge',
    { method: 'POST',
    body: JSON.stringify(json_sequence),
    headers: new Headers({ 'Content-Type': 'application/json' })
  });
  return fetchJsonData(nudge_request)
}

async function fetchWord(last_element) {
  var word_request = new Request('http://localhost:8080/word',
  { method: 'POST',
    body: JSON.stringify({sequence: last_element}),
    headers: new Headers({ 'Content-Type': 'application/json' })
  });
  return fetchJsonData(word_request)
}

async function etah_generate(func) {
  var predicted_text = ""
  var json_sequence = await fetchSeed()
  for (let i = 0; i < 900; i++) {
    var nudged_sequence = await fetchNudge(json_sequence)
    var last_element = nudged_sequence.sequence.at(39)
    var word_json = await fetchWord(last_element)
    predicted_text = predicted_text + ' ' + word_json.word
    func(predicted_text)
    json_sequence = nudged_sequence // iterate on the outer sequence          
  }
}

jQuery(document).ready(function($) {
  var speechElement = $("#etah-speech");
  $("#etah-generate").click(function() {
    speechElement.text("Text wird generiert...");
    function display_text(word) { speechElement.text(word); }
    etah_generate(display_text)
  });
});
