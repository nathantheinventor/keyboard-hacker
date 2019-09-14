const recorder = new WzRecorder({
    onRecordingStop: data => {
        recorder.upload("/audio-upload", {
            csrfmiddlewaretoken: $("input:hidden").val()
        });
    }
});


$.post("/example", {
    csrfmiddlewaretoken: $("input:hidden").val(),
    data: JSON.stringify(data)
}, callback)

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
