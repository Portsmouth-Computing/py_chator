window.addEventListener('load', initialize);

function initialize() {
    var status_box = document.getElementById("status");
    status_box.style.backgroundColor = "FireBrick"; // No connection, ForestGreen on good connection
    status_box.style.color = "White";               // Change the text colour to make it easier to see
}

var ws = new WebSocket('ws://' + document.domain + ':' + location.port + '/online');

ws.onmessage = function (event) {
    console.log("Got ", event.data)
    if (document.getElementById("status").style.backgroundColor !== "ForestGreen") {
        document.getElementById("status").style.backgroundColor = "ForestGreen";
    }
};

window.setInterval(function() {
    var data = 'Online?';
    ws.send(data);
    console.log("Sent ", data)
}, 1000);
