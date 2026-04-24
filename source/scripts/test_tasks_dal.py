from app.dal.tasks_dal import list_tasks


def test():
    result = list_tasks()
    print("Resultado DAL:", result)


if __name__ == "__main__":
    test()