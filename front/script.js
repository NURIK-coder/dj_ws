





let ws = new WebSocket('ws://127.0.0.1:8000/ws/chat/1/');
//co.der.

ws.onopen = () =>{
    setTimeout(()=>{
        

    }, 2000)
}
ws.onmessage = (event) =>{
    const p = document.createElement('p');
    p.textContent = JSON.parse(event.data).message
    document.body.append(p)
}

const btn = document.getElementById('btn');
const inp = document.getElementById('inp');


btn.onclick=(e)=>{
    const data  = {
        'message': inp.value
    }
    ws.send(JSON.stringify(data))
}  