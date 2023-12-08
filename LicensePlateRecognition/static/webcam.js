// webcam.js
document.addEventListener('DOMContentLoaded', function () {
    const videoElement = document.getElementById('webcam');
    const startButton = document.getElementById('start');
    const stopButton = document.getElementById('stop');
    const mediaRecorder = null;
    const recordedChunks = [];

    // Check for webcam support
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices
            .getUserMedia({ video: true })
            .then(function (stream) {
                videoElement.srcObject = stream;

                // Create a MediaRecorder to capture video
                mediaRecorder = new MediaRecorder(stream);

                // Event handler to capture video data
                mediaRecorder.ondataavailable = (event) => {
                    if (event.data.size > 0) {
                        recordedChunks.push(event.data);
                    }
                };

                // Event handler for the start button
                startButton.addEventListener('click', () => {
                    mediaRecorder.start();
                });

                // Event handler for the stop button
                stopButton.addEventListener('click', () => {
                    mediaRecorder.stop();
                });

                // Event handler to save the video on stop
                mediaRecorder.onstop = () => {
                    const blob = new Blob(recordedChunks, { type: 'video/webm' });
                    const formData = new FormData();
                    formData.append('video', blob, 'webcam_video.webm');

                    // Send the captured video data to the server for storage
                    fetch('/your-api-endpoint/', {
                        method: 'POST',
                        body: formData,
                    })
                    .then(response => response.json())
                    .then(data => {
                        // Handle the response, e.g., show a success message
                    })
                    .catch(error => {
                        // Handle errors
                    });

                    recordedChunks.length = 0; // Clear the chunks for the next recording
                };
            })
            .catch(function (error) {
                console.error('Error accessing webcam:', error);
            });
    } else {
        console.error('getUserMedia not supported in this browser');
    }
});
