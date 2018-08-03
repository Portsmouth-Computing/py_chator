window.addEventListener('load', initialize);
var WEBSOCKET_AUTOREFRESH_INTERVAL = 1000;
var WEBSOCKET_AUTOREFRESH_MULTIPLIER  = 1;

var ws = new WebSocket('ws://' + document.domain + ':' + location.port + '/online');

function initialize() {
    var status_box = document.getElementById("status");
    status_box.style.backgroundColor = "FireBrick"; // No connection, ForestGreen on good connection
    status_box.style.color = "White";               // Change the text colour to make it easier to see
}

ws.onmessage = function (event) {
    console.log("Got ", event.data);
    if (document.getElementById("status").style.backgroundColor !== "ForestGreen") {
        document.getElementById("status").style.backgroundColor = "ForestGreen";
    }
};

window.setInterval(function() {
    var data = 'Online?';
    if (ws.readyState === 1) {
        ws.send(data);
    }
    else {
        document.getElementById("status").style.backgroundColor = "FireBrick";
        console.log("No connection");
    }
    // console.log("Sent ", data)
}, WEBSOCKET_AUTOREFRESH_INTERVAL);
