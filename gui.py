import PySimpleGUI as sg 
import functions 

label = sg.Text("Todo List")
input_box = sg.InputText(tooltip="Enter Todo", key = "todo")
add_button = sg.Button("Add")
delete_button = sg.Button("delete")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")

window = sg.Window("My to do",
                    layout=[[label],
                      [input_box, add_button],
                      [list_box, edit_button]],
                    font= ("Helvetica", 15) )

while True:
    event, value = window.read()
    print(1,event)
    print(2, value)
    print(3,value["todos"])
    match event:
        case "Add":
            todo = functions.get_todos()
            new_value = value["todo"] + '\n'
            todo.append(new_value)
            functions.write_todos(todo)
            window["todos"].update(values= todo)

        case "Edit":
            try:
                new_todo_edit = value["todos"][0]
                new_todo = value["todo"]
                todo = functions.get_todos()
                index = todo.index(new_todo_edit)
                todo[index]= new_todo
                functions.write_todos(todo)
                window["todos"].update(values= todo)
               
            except IndexError:
                sg.popup("Please select a todo to edit.")
            except Exception as e:
                sg.popup(f"An error occurred: {e}")
        case "todos":
            window["todo"].update(value= value["todos"][0])

        #case "delete":
            #todo = functions.get_todos()
            #index = value["todo"]
            #index = 
        


            
        case WIN_CLOSED:
            break
window.close()

        

