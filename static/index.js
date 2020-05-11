
function add_player(name) {
    players.push(name);
    let players_div = document.getElementById("current_players");
    add_p_element(players_div, name);
}



function add_p_element(node, text) {
    let p_block = document.createElement("P");
    let textnode = document.createTextNode(text);
    p_block.appendChild(textnode);
    node.appendChild(p_block);
}


function host_game() {
    console.log("hosting game");
    let gid = document.getElementById("new_game_id").value;
    console.log(gid);
    let name = document.getElementById("new_user_name").value;
    console.log(name);
    let args = JSON.stringify({"gid": gid, "name": name});
    console.log(args);
    fetch('new_game', { method: 'post', 
                        body: args, 
                        headers: new Headers({
                            "content-type": "application/json"
                        })})
        .then(response => response.json())
        .then(function(data) {
            if(data == 0) {
                window.location.replace("gameboard.html?gid=" + gid + "&uname=" + name);
            }
            else {
                alert("Error starting game");
            }
        });
}

function join_game() {
    let name = document.getElementById("user_name").value;
    fetch('join_game', {method: 'post',
                        body: JSON.stringify({"name":name}),
                        headers: new Headers({
                            "content-type": "application/json"
                        })})
        .then(response => response.json())
        .then(function(data) { 
            if(data == 0) {
                window.location.replace("gameboard.html?uname=" + name);
            }
            else {
                alert("Error joining game");
            }
        });
}

//window.onload = function() {
    //fetch('status')
    //    .then(response => response.json())
    //    .then(data => console.log(data));
//}
