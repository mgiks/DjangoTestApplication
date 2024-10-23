// WebSockets
const host = window.location.host

let url = `ws://${host}/ws/socket-server/`

const socket = new WebSocket(url)

socket.onmessage = function(e) {
    let data = JSON.parse(e.data)
    console.log('Data', data)

    if (data.type === 'notification') {
        let notificationDiv = document.getElementById('notificationDiv')

        notificationDiv.innerHTML = `<div>
            <p>${data.notification}</p>
        </div>` + notificationDiv.innerHTML
    }
}


async function listItems(path, name) {
    const divResult = document.getElementById("result");
    const url = `http://${host}${path}`;
    try {
        const response = await fetch(url).then(response => response.json());
        const jsonResponse = JSON.stringify(response, undefined, 4)
        divResult.innerHTML = `<pre>${jsonResponse}</pre>`
    }
    catch (error) {
        console.log(error.message);
    }
    socket.send(JSON.stringify({
        'notification': `${name} listed!`
    }))
}


async function createItem(path, name) {
    const divResult = document.getElementById("result");
    const form = document.getElementById(`${name.toLowerCase()}CreateForm`);
    const formData = new FormData(form)
    const url = `http://${host}${path}create/`;
    try {
        response = await fetch(url, {body: formData, method: "post"})
        .then(
            response => {
                if (!response.ok) {
                    socket.send(JSON.stringify({
                        'notification': `${name} failed to be created!`
                    }))
                }
                else {
                    socket.send(
                        JSON.stringify({
                                'notification': `${name} created!`
                            })
                        )
                };
                response.json()
                .then(
                    response => (
                        divResult.innerHTML = JSON.stringify(response, undefined, 4),
                        console.log(JSON.stringify(response, undefined, 4))
                    )
                );
            }
        )
    }
    catch (error) {
        console.log(error.message);
    }
}

async function getItem(path, name) {
    const divResult = document.getElementById("result");
    const id = document.getElementById(`${name.toLowerCase()}Id`).value
    const url = `http://${host}${path}${id}`;
    try {
        response = await fetch(url)
        .then(
            response => {
                if (!response.ok) {
                    socket.send(JSON.stringify({
                        'notification': `${name} failed to be gotten!`
                    }))
                }
                else {
                    socket.send(
                        JSON.stringify({
                                'notification': `${name} gotten!`
                            })
                        )
                };
                response.json()
                .then(
                    response => (
                        divResult.innerHTML = JSON.stringify(response, undefined, 4),
                        console.log(JSON.stringify(response, undefined, 4))
                    )
                );
            }
        )
    }
    catch (error) {
        console.log(error.message);
    }
}

async function populateItem(path, name) {
    const divResult = document.getElementById("result");
    const id = String(document.getElementById(`${name.toLowerCase()}Id`).value).trim()
    const url = `http://${host}${path}${id}`;
    try {
        response = await fetch(url)
        .then(
            response => {
                if (!response.ok) {
                    socket.send(JSON.stringify({
                        'notification': `${name} failed to be populated!`
                    }))
                }
                else {
                    socket.send(
                        JSON.stringify({
                                'notification': `${name} populated!`
                            })
                        )
                };
                response.json()
                .then(
                    response => {
                        let jsonResponse = JSON.stringify(response, undefined, 4);
                        let parsedResponse = JSON.parse(jsonResponse);
                        const fields = document.getElementById(`${name.toLowerCase()}UpdateForm`).elements
                        divResult.innerHTML = jsonResponse;
                        for (let key in parsedResponse) {
                            if (fields[key]) {
                                fields[key].value = parsedResponse[key];
                            }
                            console.log(parsedResponse[key]);
                        }
                    }
                );
            }
        )
    }
    catch (error) {
        console.log(error.message);
    }
}

async function deleteItem(path, name) {
    const divResult = document.getElementById("result");
    const id = document.getElementById(`${name.toLowerCase()}Id`).value
    const url = `http://${host}${path}${id}`;
    try {
        response = await fetch(url, {method: "delete"})
        .then(
            response => {
                if (!response.ok) {
                    socket.send(JSON.stringify({
                        'notification': `${name} failed to be deleted!`
                    }))
                }
                else {
                    socket.send(
                        JSON.stringify({
                                'notification': `${name} got deleted!`
                            })
                        )
                    divResult.innerHTML = "<p>Succesfully deleted!</p>"
                };
                response.json()
                .then(
                    response => (
                        divResult.innerHTML = JSON.stringify(response, undefined, 4),
                        console.log(JSON.stringify(response, undefined, 4))
                    )
                );
            }
        )
    }
    catch (error) {
        console.log(error.message);
    }
}
