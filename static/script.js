// ===================================
// SEND MOVEMENT COMMAND
// ===================================

function sendCommand(command){

    fetch('/' + command)

    .then(response => response.text())

    .then(data => {

        console.log(data);
    });
}

// ===================================
// VOICE COMMANDS
// ===================================

function startVoice(){

    const recognition = new webkitSpeechRecognition();

    recognition.lang = 'en-US';

    recognition.onresult = function(event){

        let command =
            event.results[0][0].transcript.toLowerCase();

        console.log(command);

        // ======================
        // FORWARD
        // ======================

        if(command.includes("forward")){

            sendCommand('forward');
        }

        // ======================
        // BACKWARD
        // ======================

        else if(command.includes("backward")){

            sendCommand('backward');
        }

        // ======================
        // LEFT
        // ======================

        else if(command.includes("left")){

            sendCommand('left');
        }

        // ======================
        // RIGHT
        // ======================

        else if(command.includes("right")){

            sendCommand('right');
        }

        // ======================
        // STOP
        // ======================

        else if(command.includes("stop")){

            sendCommand('stop');
        }
    };

    recognition.start();
}