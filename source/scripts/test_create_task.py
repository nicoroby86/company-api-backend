from app.dal.tasks_dal import create_task


def test():
    result = create_task("Tarea creada desde Python", "blocked")
    print("Nueva tarea:", result)


if __name__ == "__main__":
    test()