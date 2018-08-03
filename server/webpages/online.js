window.addEventListener('load', initialize);
var WEBSOCKET_AUTOREFRESH_INTERVAL = 1000;
var WEBSOCKET_AUTOREFRESH_MULTIPLIER  = 1;

websocket();

function websocket() {
    ws = new WebSocket('ws://' + document.domain + ':' + location.port + '/online');
    console.log(ws.readyState)
}

function restart_websocket() {
    try {
        setTimeout(websocket, WEBSOCKET_AUTOREFRESH_INTERVAL * WEBSOCKET_AUTOREFRESH_MULTIPLIER)
    }
    finally {
        if (WEBSOCKET_AUTOREFRESH_MULTIPLIER < 32) {
            WEBSOCKET_AUTOREFRESH_MULTIPLIER = WEBSOCKET_AUTOREFRESH_MULTIPLIER * 2
        }
    }
}

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
        restart_websocket()
    }
    // console.log("Sent ", data)
}, WEBSOCKET_AUTOREFRESH_INTERVAL);