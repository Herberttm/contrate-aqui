import flet as ft

def main(page: ft.Page):
    # Configuração da página
    page.title = "Contrate Aqui"
    page.window_width = 360  # Largura padrão de dispositivos móveis
    page.window_height = 640  # Altura padrão de dispositivos móveis
    page.scroll = ft.ScrollMode.AUTO
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#F3F4F6"  # Cor de fundo azul usando hexadecimal
    # Logo e título
    logo = ft.Image(
        src="icon.png",  # Insira o caminho correto da imagem do logo
        width=80,  # Ajustado para tamanho de dispositivo móvel
        height=80,
        fit=ft.ImageFit.CONTAIN,
    )
    
    titulo = ft.Text(
        "CONTRATE\nAQUI",
        size=24,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
        color="black",
    )
    
    # Botões
    cliente_button = ft.ElevatedButton(
        text="CLIENTE",
        bgcolor="black",
        color="white",
        width=200,
        height=50,
        on_click=lambda _: print("Cliente clicado"),
    )
    
    profissional_button = ft.ElevatedButton(
        text="PROFISSIONAL",
        bgcolor="orange",
        color="white",
        width=200,
        height=50,
        on_click=lambda _: print("Profissional clicado"),
    )
    
    # Texto inferior
    subtitulo = ft.Text(
        "Conectando pessoas e serviços com praticidade",
        size=14,
        color="orange",
        text_align=ft.TextAlign.CENTER,
    )
    
    # Layout principal
    layout = ft.Column(
        [
            logo,
            titulo,
            cliente_button,
            profissional_button,
            subtitulo,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
    )
    
    # Adiciona o layout à página
    page.add(layout)

ft.app(target=main, view=ft.AppView.FLET_APP)