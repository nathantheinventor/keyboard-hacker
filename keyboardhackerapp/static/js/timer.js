/**
 * Get the offset in ms between the time in the browser and the time on the server
 * Use this offset like this: browser_time + offset = server_time
 */
function get_server_offset(depth=0) {
    return new Promise((resolve, reject) => {
        if (depth >= 50) {
            alert("Could not get an accurate sync between the browser and the server");
            reject();
            return;
        }
        let startTime;
        $.ajax({
            url: "/sync",
            method: "GET",
            beforeSend: _ => {
                startTime = performance.now();
            },
            success: server_time => {
                const time = performance.now() - startTime;
                console.log(time);
                if (time < 20) {
                    // get the midpoint time on the browser
                    const browser_time = new Date().getTime() - time / 2;
                    resolve(server_time - browser_time);
                } else {
                    get_server_offset(depth + 1)
                        .then(resolve)
                        .catch(reject);
                }
            }
        });
    });
}