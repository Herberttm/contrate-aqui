import flet as ft

def main(page: ft.Page):
    # Alterando a cor de fundo da página
    page.title = "App Responsivo"
    page.bgcolor = "#F3F4F6"  # Cor de fundo azul usando hexadecimal 
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Conteúdo da tela inicial
    page.add(ft.Container(
            content=ft.Text(
                "Este app tem uma nova cor de fundo!",
                size=20,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,  # Texto branco para contraste
            ),
            alignment=ft.alignment.center,
     ))


    page.add(
            ft.Image(
            src="icon.png",  # URL da imagem
            width=300,  # Largura da imagem
            height=200,  # Altura da imagem
           fit=ft.ImageFit.CONTAIN  # Ajusta como a imagem será renderizada
    ) )




ft.app(target=main)

