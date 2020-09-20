let recorder, gumStream;
let recordButton = document.getElementById("recordButton");
recordButton.addEventListener("click", toggleRecording);

function toggleRecording() {
    if (recorder && recorder.state === "recording") {
        recorder.stop();
        gumStream.getAudioTracks()[0].stop();
    } else {
        navigator.mediaDevices.getUserMedia({
            audio: true
        }).then(function(stream) {
            gumStream = stream;
            recorder = new MediaRecorder(stream);
            recorder.ondataavailable = function(e) {
                let url = URL.createObjectURL(e.data);
                let preview = document.createElement('audio');
                preview.controls = true;
                preview.src = url;
                document.body.appendChild(preview);
            };
            recorder.start();
        });
    }
}

var icon = document.getElementById("recordButton"),
    bool = true;

function change_icon() {
  if (!bool) {
    icon.innerHTML = '&#9658;';
    bool = true;
  } else {
    icon.innerHTML = '&#9632;';
    bool = false;
  }
}
