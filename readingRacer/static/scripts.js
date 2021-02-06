let recorder;
let data = [];
let recordButton = document.getElementById("recordButton");
recordButton.addEventListener("click", toggleRecording);

function toggleRecording() {
    if (recorder && recorder.state === "recording") {
        recorder.stop();
        const blob = new Blob(data, {
            'type': 'audio/wav'
        });
        sendAudio(blob, "doot.wav");
    } else {
        navigator.mediaDevices.getUserMedia({
            audio: true
        }).then(function(stream) {
            recorder = new MediaRecorder(stream);
            recorder.ondataavailable = event => {
                data.push(event.data);
            };
            recorder.start();
        });
    }
}

function sendAudio(audioFile, fileName) {
    const formData = new FormData();
    formData.append("file", audioFile);
    formData.append("filename", fileName);
    formData.append("prev_title", document.getElementById("passageTitle").textContent);
    formData.append("prev_text", document.getElementById("passageText").textContent);
    fetch(document.location.href,
        {method: "POST",
            body: formData}).then((_) => void(0),
        (_) => void(0));
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
