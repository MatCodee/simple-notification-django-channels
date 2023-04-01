var ws_url = 'ws://' + window.location.host + '/ws/notifications/';

var websocket = new WebSocket(ws_url);

websocket.onopen = function(event) {
    console.log('WebSocket connected');
};

websocket.onmessage = function(event) {
    console.log('WebSocket message received:', event.data);
    var message = JSON.parse(event.data).message;
    var messagesDiv = document.getElementById('messages');
    messagesDiv.innerHTML += '<p>' + message + '</p>';
};

document.getElementById('connect').addEventListener('click', function() {
    websocket.send(JSON.stringify({'message': 'Connected to WebSocket'}));
});