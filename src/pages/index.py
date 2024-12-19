from flet import View, AppBar, ElevatedButton, Text, Colors

path = "/"

view = View(
    path,
    [AppBar(title=Text("Flet app"), bgcolor=Colors.PURPLE_100)],
)
