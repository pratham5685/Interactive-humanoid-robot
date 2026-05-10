function sendCommand(command){

    fetch('/' + command)
    .then(response => response.text())
    .then(data => console.log(data));
}

function startVoice(){

    const recognition = new webkitSpeechRecognition();

    recognition.onresult = function(event){

        let command = event.results[0][0].transcript;

        console.log(command);

        if(command.includes("forward")){
            sendCommand('forward');
        }

        else if(command.includes("backward")){
            sendCommand('backward');
        }

        else if(command.includes("left")){
            sendCommand('left');
        }

        else if(command.includes("right")){
            sendCommand('right');
        }

        else if(command.includes("stop")){
            sendCommand('stop');
        }
    }

    recognition.start();
}