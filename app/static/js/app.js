// app.js
const socket = new WebSocket('ws://localhost:8001/ws/speech/');

socket.onopen = function() {
    console.log('WebSocket connection established');
    // Send a message if needed
    // socket.send('Hello Server!');
};

socket.onmessage = function(event) {
    console.log('Message from server: ', event.data);
};

socket.onerror = function(error) {
    console.error('WebSocket Error: ', error);
};

socket.onclose = function(event) {
    console.log('WebSocket connection closed: ', event);
};
