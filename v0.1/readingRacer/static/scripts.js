let recorder;
let data = [];
let recordButton = document.getElementById("recordButton");
recordButton.addEventListener("click", toggleRecording);

/**
 * Toggle audio recording, ending and sending recording if previous button press started recording.
 */
function toggleRecording() {
    if (recorder && recorder.state === "recording") {
        recorder.stop();
        const blob = new Blob(data, {
            'type': 'audio/webm'
        });
        sendAudio(blob, "doot.webm");
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

/**
 * Store current title and text for later use by next reading_practice_init.
 */
function storeCurrent() {
    sessionStorage.setItem("prev_title", document.getElementById("passageTitle").textContent);
    sessionStorage.setItem("prev_text", document.getElementById("passageText").textContent);
}

/**
 * Send audio via POST request, as well as previous title and text; endpoint will redirect.
 * @param audioFile audio data to send
 * @param fileName filename to upload to
 */
function sendAudio(audioFile, fileName) {
    storeCurrent();
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
