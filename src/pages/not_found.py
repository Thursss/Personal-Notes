from flet import View, AppBar, ElevatedButton, Text, Colors

path = "/404"

view = View(
    path,
    [
        Text(
            "Page not found",
            color=Colors.RED,
        )
    ],
)
