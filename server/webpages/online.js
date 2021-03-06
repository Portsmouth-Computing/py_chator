window.addEventListener('load', initialize);
var WEBSOCKET_AUTOREFRESH_INTERVAL = 1000;
var WEBSOCKET_AUTOREFRESH_MULTIPLIER  = 1;

websocket();

function websocket() {
    ws = new WebSocket('wss://' + document.domain + ':' + location.port + '/online');
    ws.onmessage = function (event) {
        console.log("Got ", event.data);
        if (document.getElementById("status").style.backgroundColor !== "ForestGreen") {
            document.getElementById("status").style.backgroundColor = "ForestGreen";
        }
    };
    // console.log(ws.readyState)
}

function restart_websocket() {
    try {
        setTimeout(websocket, WEBSOCKET_AUTOREFRESH_INTERVAL * WEBSOCKET_AUTOREFRESH_MULTIPLIER)
    }
    finally {
        if (WEBSOCKET_AUTOREFRESH_MULTIPLIER < 16) {
            WEBSOCKET_AUTOREFRESH_MULTIPLIER = WEBSOCKET_AUTOREFRESH_MULTIPLIER * 2
        }
    }
}

function initialize() {
    var status_box = document.getElementById("status");
    status_box.style.backgroundColor = "FireBrick"; // No connection, ForestGreen on good connection
    status_box.style.color = "White";               // Change the text colour to make it easier to see
}

window.setInterval(function() {
    var data = 'Online?';
    if (ws.readyState === 1) {
        ws.send(data);
        WEBSOCKET_AUTOREFRESH_MULTIPLIER = 1;
        if (!LOADMESSAGES_RUNNING) {
            loadMessages()
        }
    }
    else {
        document.getElementById("status").style.backgroundColor = "FireBrick";
        console.log("No connection");
        restart_websocket()
    }
    // console.log("Sent ", data)
}, WEBSOCKET_AUTOREFRESH_INTERVAL);
