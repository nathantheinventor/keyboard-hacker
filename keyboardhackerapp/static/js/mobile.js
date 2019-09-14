// First we need to know the correct time.

offset = get_server_offset().then(function(offset){
  window.recorder = new WzRecorder({
    onRecordingStart: data=> {
        // Notify the server
        $.post('/activate', {
            csrfmiddlewaretoken: $("input:hidden").val(),
            audio_start_time: Math.round(new Date() * 1 + offset)

        })
    },
    onRecordingStop: data => {
        try {
            recorder.upload("/audio-upload", {
                csrfmiddlewaretoken: $("input:hidden").val()
            });
        } catch (e) {
            $("#error").append(`<div>${e.stack}</div>`)
        }
    }
});

});

$(document).ready(_ => {
    get_server_offset()
        .then(offset => {
            server_offset = offset;
            $("#start").attr("disabled", false);
        });
    $("#error").append(`<div>ready</div>`);
    try {
    navigator.mediaDevices.getUserMedia({audio: true})
        .then(stream => {
            $("#error").append(`<div>success: ${stream}</div>`);
        })
        .catch(err => {
            $("#error").append(`<div>Error: ${err}</div>`);
        });
    } catch (e) {
        $("#error").append(`<div>${e.message}</div>`)
        $("#error").append(`<div>${ navigator.mediaDevices}</div>`)
    }
});

function start_recording() {
    // TODO: remember start time
    $("#start").attr("disabled", true);
    $("#stop").attr("disabled", false);
    recorder.start();
}

function stop_recording() {
    try {
        $("#error").append(`<div>Hello, world</div>`);
        $("#error").append(`<div>${window.localStream}</div>`);
        $("#error").append(`<div>${window.localStream.getTracks()}</div>`);
		$("#stop").attr("disabled", true);
        recorder.stop();
    } catch (e) {
        $("#error").append(`<div>${e.stack}</div>`)
    }
}
