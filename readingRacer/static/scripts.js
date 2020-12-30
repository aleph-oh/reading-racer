let recorder, gumStream;
let recordButton = document.getElementById("recordButton");
recordButton.addEventListener("click", toggleRecording);

function toggleRecording() {
    if (recorder && recorder.state === "recording") {
        recorder.stop();
        gumStream.getAudioTracks()[0].stop();
        let audioFile = document.getElementsByTagName('audio')[0];
        sendAudio(audioFile);
    } else {
        navigator.mediaDevices.getUserMedia({
            audio: true
        }).then(function(stream) {
            gumStream = stream;
            recorder = new MediaRecorder(stream);
            recorder.ondataavailable = function(e) {
                const url = URL.createObjectURL(e.data);
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
    console.log(document.location)
    fetch(document.location.href,{method: "POST", body: formData}).then((success) => void(0),
        (failure) => void(0));
}

let icon = document.getElementById("recordButton"),
    squarePlayIcon = true;

function change_icon() {
  if (!squarePlayIcon) {
    icon.innerHTML = '&#9658;';
    squarePlayIcon = true;
  } else {
    icon.innerHTML = '&#9632;';
    squarePlayIcon = false;
  }

}
