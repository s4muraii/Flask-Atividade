const tabela = document.querySelector(".tabela-js");
axios.get("https://api-todo.1gabsfps1.repl.co").then(function(resposta){
    getData(resposta.data)
})
.catch(function (error) {
    console.error(error)})

    function getData(dados){
        dados.map((item)=>{ 
            tabela.innerHTML += `
            <tr>
                <th scope="row">${item.ID}</th>
                <td>${item.Tarefa}</td>
                <td>${item.Status}</td>
                <td>
                    <button class="btn btn-danger delete-btn"><i class="bi bi-trash"></i></button>
                    <button type="button" class="btn btn-primary edit-btn" data-bs-toggle="modal" data-bs-target="#editModal"
                    data-bs-whatever="@mdo"><i class="bi bi-pen"></i></button>
                </td>
            </tr>`
        });
    };
    document.querySelector(".btn-add").addEventListener("click", function(){
        const tarefa = document.querySelector("#recipient-name").value;
        if(tarefa === ""){
            alert("Digite uma tarefa!");
            return;
        }
        axios.post("https://api-todo.1gabsfps1.repl.co/task", {
            Tarefa: tarefa
        })
        .then(function (response) {
            console.log(response);
            location.reload();
        })
        .catch(function (error) {
            console.log(error);
        });
    })

document.querySelector(".tabela-js").addEventListener("click", function(e){
    if(e.target.classList.contains("delete-btn")){
        const id = e.target.parentElement.parentElement.firstElementChild.textContent;
        axios.delete(`https://api-todo.1gabsfps1.repl.co/delete_task/${id}`)
        .then(function (response) {
            console.log(response);
            location.reload();
        })
        .catch(function (error) {
            console.log(error);
        });
    }
})

let id;

document.querySelector(".tabela-js").addEventListener("click", function(e){
    if(e.target.classList.contains("edit-btn")){
        id = e.target.parentElement.parentElement.firstElementChild.textContent;
    }
})

document.querySelector(".modal-edit-btn").addEventListener("click", function(){
    const tarefaupdate = document.querySelector("#update-text").value;
    if (id) {
        axios.put(`https://api-todo.1gabsfps1.repl.co/task/${id}`,{
            Tarefa: tarefaupdate
        })
        .then(function (response) {
            console.log(response);
            location.reload();
        })
        .catch(function (error) {
            console.log(error);
        })
        .finally(function () {
            id = null;
        });
    }
})
