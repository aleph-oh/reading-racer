let recorder, gumStream;
let recordButton = document.getElementById("recordButton");
recordButton.addEventListener("click", toggleRecording);

function toggleRecording() {
    if (recorder && recorder.state === "recording") {
        recorder.stop();
        gumStream.getAudioTracks()[0].stop();
        let audioFile = document.getElementsByTagName('audio');
        sendAudio(audioFile[0]);
    } else {
        navigator.mediaDevices.getUserMedia({
            audio: true
        }).then(function(stream) {
            gumStream = stream;
            recorder = new MediaRecorder(stream);
            recorder.ondataavailable = function(e) {
                var url = URL.createObjectURL(e.data);
                let preview = document.createElement('audio');
                preview.controls = true;
                preview.src = url;
                document.body.appendChild(preview);

            };
            recorder.start();
        });
    }
}

function sendAudio(audioFile) {
    const formData = new FormData();
    formData.append("prev_title", document.getElementById("passageTitle").textContent);
    formData.append("prev_text", document.getElementById("passageText").textContent);
    formData.append("file", audioFile);
    fetch(".",{method: "POST", body: formData});
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
