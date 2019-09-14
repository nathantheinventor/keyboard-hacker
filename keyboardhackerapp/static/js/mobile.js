// First we need to know the correct time.

offset = get_server_offset().then(function(offset){
  window.recorder = new WzRecorder({
    onRecordingStart: data=> {
        // Notify the server
        $.post('/activate', {
             csrfmiddlewaretoken: $("input:hidden").val(),
            audio_start_time: new Date() * 1 + offset

        })
    },
    onRecordingStop: data => {
        recorder.upload("/audio-upload", {
            csrfmiddlewaretoken: $("input:hidden").val()
        });
    }
});


});





$(document).ready(_ => {
    // window.setInterval(_ => {
    //     let startTime;
    //     $.ajax({
    //         url: "/sync",
    //         method: "GET",
    //         beforeSend: _ => {
    //             startTime = performance.now();
    //         },
    //         success: _ => {
    //             const time = performance.now() - startTime;
    //             $("#times").append(`<div class='time'>${time}</div>`);
    //         }
    //     });
    // }, 1000);
})
