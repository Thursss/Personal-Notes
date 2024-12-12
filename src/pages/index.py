from flet import Page, Text, TextField, Button, MainAxisAlignment, FilledTonalButton
from src.utils.rsa import DocumentRsa


def main(page: Page):
    page.title = "Lock"
    page.vertical_alignment = MainAxisAlignment.CENTER

    def on_change(e):
        tfLenght.value = len(tf.value.encode("utf-8"))
        page.update()

    tf = TextField(
        label="",
        multiline=True,
        min_lines=5,
        max_lines=30,
        on_change=on_change,
    )
    tf.value = ""
    tfLenght = Text(len(tf.value))

    def lock(e):
        tf.value = DocumentRsa.encrypt_data(tf.value)
        tfLenght.value = len(tf.value)
        page.update()

    def unlock(e):
        tf.value = DocumentRsa.decrypt_data(tf.value)
        tfLenght.value = len(tf.value)
        page.update()

    page.add(
        tf,
        tfLenght,
        FilledTonalButton("加密", on_click=lock),
        FilledTonalButton("解密", on_click=unlock),
    )
