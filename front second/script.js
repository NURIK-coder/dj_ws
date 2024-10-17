





let ws = new WebSocket('ws://127.0.0.1:8000/ws/chat/1/');
//co.der.

ws.onopen = () =>{
    setTimeout(()=>{
        const data = {
            'message': 'from websocket'
        }
        ws.send(JSON.stringify(data))

    }, 2000)
}
ws.onmessage = (event) =>{
    console.log(event.data);
}

