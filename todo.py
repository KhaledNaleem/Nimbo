import typer
from rich.console import Console
from rich.table import Table
from model import Todo
from database import get_all_todos, delete_todo, update_todo, insert_todo, complete_todo
import time

console = Console()

app = typer.Typer()

@app.command(short_help='Add a task')
def add(task:str, category:str):                #Adds a task
    typer.echo(f"Okey dokey. Give me a second to add your task... : Task Name - {task} | Category - {category}")
    time.sleep(4)
    todo = Todo(task, category)
    insert_todo(todo)
    show()

@app.command(short_help='Delete a task')
def delete(position: int):                  #deletes a task
    typer.echo(f"Throwing Task {position} right into the bin......")
    time.sleep(4)
    typer.echo("Done! 👍")
    delete_todo(position-1)
    show()

@app.command(short_help='Update a task')
def update(position: int, task: str = None, category: str = None):      #updates a task
    typer.echo(f"Updating Task {position}...")
    time.sleep(4)
    typer.echo("Done! 👍")
    update_todo(position-1, task, category)
    show()

@app.command(short_help='Marks a task as "Complete"')
def complete(position: int):                  #deletes a task
    typer.echo(f"Wohooo.. You've done it. Marking Task {position} as completed....")
    time.sleep(3)
    typer.echo("Done! 👍")
    complete_todo(position-1)
    show()


@app.command()
def show(short_help = 'Shows all options'):
    tasks = get_all_todos()
    console.print("Todos 💻:", style='#fcbf49')

    table = Table(show_header=True, header_style="#a7c957")
    table.add_column("No.", style="dim", width=6)
    table.add_column("Todo", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Completed", min_width=12, justify="right")


    def get_category_color(category):
        COLORS = {'Study' : '#e63946', 'Workout': '#f77f00'}
        if category in COLORS:
            return COLORS[category]
        else:
            return 'white'

    for index, task in enumerate(tasks, start=1):
        c = get_category_color(task.category)
        is_done_str = '✅' if task.status == 2 else '❌'
        table.add_row(str(index), task.task, f'[{c}] {task.category}[/{c}]', is_done_str)
    console.print(table)


if __name__ == "__main__":
    print("----------")
    print()
    print("NIMBO! To learn more, type --help")
    print()
    time.sleep(2)
    app()