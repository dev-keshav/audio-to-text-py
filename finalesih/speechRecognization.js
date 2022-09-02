if ("webkitSpeechRecognition" in window) {
  let speechRecognition = new webkitSpeechRecognition();
  let final_transcript = "";
  var speech = true;
  speechRecognition.continuous = true;
  speechRecognition.interimResults = true;
  speechRecognition.lang = document.querySelector("#select_dialect").value;

  speechRecognition.onstart = () => {
    document.querySelector("#status").style.display = "block";
  };
  speechRecognition.onerror = () => {
    document.querySelector("#status").style.display = "none";
    console.log("Speech Recognition Error");
  };
  speechRecognition.onend = () => {
    if (speech === true) {
      speechRecognition.start();
    }
    console.log(speech, 'dd')
    document.querySelector("#status").style.display = "none";
    console.log("Speech Recognition Ended");
  };

  speechRecognition.onresult = (event) => {
    let interim_transcript = "";

    for (let i = event.resultIndex; i < event.results.length; ++i) {
      if (event.results[i].isFinal) {
        final_transcript += event.results[i][0].transcript;
      } else {
        interim_transcript += event.results[i][0].transcript;
      }
    }

    document.getElementById('final').innerHTML = final_transcript;
    document.querySelector("#interim").innerHTML = interim_transcript;
  };

  document.querySelector("#start").onclick = () => {
    speechRecognition.start();
  };
  document.getElementById('stop').
    addEventListener('click', e => {
      speechRecognition.removeEventListener("end", speechRecognition.start);
      speechRecognition.stop();
      speech = false;
      console.log('paused')
    });
} else {
  console.log("Speech Recognition Not Available");
}
// -------------------downloadFile----------------------
function downloadFile(filename, content) {
  const element = document.createElement('a');
  const blob = new Blob([content], { type: 'plain/text' });
  const fileUrl = URL.createObjectURL(blob);
  element.setAttribute('href', fileUrl); //file location
  element.setAttribute('download', filename); // file name
  element.style.display = 'none';
  document.body.appendChild(element);
  element.click();
  document.body.removeChild(element);
  document.getElementById("final").innerHTML = ''
  document.getElementById('filename').innerHTML = ''
};
window.onload = () => {
  document.getElementById('save-note-btn').
    addEventListener('click', e => {
      var select = document.getElementById('filetype');


      const filename = document.getElementById('filename').value;
      const content = document.getElementById('final').value;

      if (filename && content) {
        downloadFile(filename + '.txt', content);
        document.getElementById("final").innerHTML = ''
        document.getElementById('filename').innerHTML = ''
        window.location.reload();
      }

    });
};


$(document).ready(function () {
  $('#htmltopdf').click(function () {
    $('#final').printThis();
  });
})