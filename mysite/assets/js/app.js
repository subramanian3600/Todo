const todoinput=document.querySelector('.todo_input');
const todoadd=document.querySelector('.todo_add');
const todoul=document.querySelector('.todo_ul');

todoadd.addEventListener('click',addTodo);


function addTodo(event){

    event.preventDefault();

    const listdiv=document.createElement('div');
    listdiv.classList.add('list_div');
    

    const  item=todoinput.value.trim();
    if (item!=''){
        const newtodo=document.createElement('li');
        newtodo.innerText=item;
        todoinput.value='';
        newtodo.classList.add('new_todo');
        const com_btn=document.createElement('button');
        com_btn.classList.add('com_btn');
        com_btn.innerText='C';
        const del_btn=document.createElement('button');
        del_btn.classList.add('del_btn');
        del_btn.innerText='D';
        newtodo.appendChild(com_btn);
        newtodo.appendChild(del_btn);
        listdiv.appendChild(newtodo);
        todoul.appendChild(listdiv);  
    }
    else{
        alert("Enter any todos to add to your list...");
    }
}

const delbtn=document.querySelector('.del_btn');
delbtn.addEventListener('click',deleteItem);

function deleteItem(){
    const todoitem=document.querySelector('.new_todo');
    todoitem.delete();
}
