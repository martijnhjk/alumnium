def test_add_todo_item(al, navigate):
    """Test adding a todo item to TodoMVC Vue application."""
    navigate("https://todomvc.com/examples/vue/dist")

    al.do("add a new todo item with the text 'buy milk'")
    al.check("there is a todo item with the text 'buy milk'")
