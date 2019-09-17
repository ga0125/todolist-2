// load global var
var task_div = "#task-div"


//call todoGet when the page load
window.onload = todoGet();


// GET todo tasks
 function todoGet(id) {
 	document.getElementById('todo').focus();
	html_string = ""
	$.get("/api?complete=false&filed=false", function(result){
		renderHTML(result);
	})
}


// GET ccmplete tasks
function doneGet() {
	html_string = ""
	$.get("/api?complete=true&filed=false", function(result){
		renderHTML(result);
	})
}


// GET filed tasks
function filedGet() {
	html_string = ""
	$.get("/api?filed=true", function(result){
		renderHTML(result);
	})
}


// render the HTML fiels with the tasks
function renderHTML(data){
	for (i=0; i< data.length; i++){

					if (data[i].complete == true && data[i].filed == false){			
						html_style = `<th scope="col" class="th-task">
							<a class="fa fa-check chk-done" onclick="doneTask( `+ data[i].id +` )" title="Tarefa completa"></a>
						</th>	
						<th scope="col" class=" done-task"> `+ data[i].title +` </th>`
						
						html_style_2 = `<a class="fa fa-trash btn-act" onclick="delTask( `+ data[i].id +` )" title="Excluir"></a>
										<a class="fa fa-download btn-act" onclick="filedTask( `+ data[i].id +` )" title="Arquivar"></a>`
				
					}

					else if (data[i].filed == true){
						html_style = `<th scope="col" class="th-task">
							<a class="fa fa-archive chk-filed" onclick="doneTask( `+ data[i].id +` )" title="Tarefa arquivada"></a>
						</th>
						<th scope="col" class="filed-task"> `+ data[i].title +` </th>`

						html_style_2 = `<a class="fa fa-trash btn-act" onclick="delTask( `+ data[i].id +` )" title="Excluir"></a>`
					}
					else {
						html_style = `<th scope="col" class="th-task">
							<a class="fa fa-check chk-todo" onclick="doneTask( `+ data[i].id +` )" title="Completar tarefa"></a>
						</th>
						<th scope="col" class="task-title"> `+ data[i].title +` </th>`

						html_style_2 = `<a class="fa fa-trash btn-act" onclick="delTask( `+ data[i].id +` )" title="Excluir"></a>
										<a class="fa fa-download btn-act" onclick="filedTask( `+ data[i].id +` )" title="Arquivar"></a>`
					}

		html_string +=
		`<table class="table">
			<tbody>
				<tr class="task-menu" >`
					+ html_style + 
					`<th scope="col">`
						+ html_style_2 +
						`<a class="fa fa-chevron-down btn-act" onclick="showDesc( `+ data[i].id +` )" title="Descrição"></a>
						<a class="dln-act" title="Prazo de entrega">`+ data[i].deadline +`</a>
					</th>
				</tr>		
			</tbody>
		</table>
		
		<div class="form-control desc-task" id="`+ data[i].id +`" style="display: none;"><a class="desc-sub"> Descrição: </a><a class="desc-line">`+ data[i].desc +`</a></div>`
	}
	$(task_div).html(html_string);
}


// DELETE tasks
function delTask(el) {
	$.post(
		"del-task",
		{
		id: el},
		function(data) {
			location.reload();
		}
	);
}



// UPDATE the filed field
function filedTask(el) {
	$.post(
		"filed-task",
		{
		id: el},
		function(data) {
			location.reload();
		}
	);
}


// UPDATE complete field
function doneTask(el) {
	$.post(
		"done-task",
		{
			id: el
		},
		function(data) {
			location.reload();
		}
	);
}



// Show or hide Desc task
function showDesc(el) {
    var display = document.getElementById(el).style.display;

    if(display == "none")
        document.getElementById(el).style.display = 'block';
    else
        document.getElementById(el).style.display = 'none';
}


// The testField function will test if the obrigatory field (title, deadline) has value or not
function testField (){
    if(document.getElementById("title").value == ""){
        alert('É necessário incluir um título para sua tarefa!');
        document.getElementById("title").focus();
        return false
    }
    else if (document.getElementById("deadline").value == ""){
        alert('É necessário incluir um prazo para sua tarefa!');
        document.getElementById("title").focus();
        return false
    }
}


// This function is setting the DatePicker
$(function () {
	var minDate = new Date();
	$("#datetimepicker1").datetimepicker({
		format: 'YYYY-MM-DD',
		minDate: minDate,
		showAnim: 'drop',
	});
});