import flet as ft

import CalculadoraLogica


# https://paletadecolores.com.mx/
def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F3F1E2"
    page.padding = 0
    page.window_maximizable = False
    page.window_resizable = False
    hei = page.window_height

    def con(e):
        campo.value = campo.value+" and"
        page.update()

    def dis(e):
        campo.value = campo.value + " or"
        page.update()

    def neg(e):
        campo.value = campo.value + " not"
        page.update()

    def disE(e):
        campo.value = campo.value + " xor"
        page.update()

    def operar(e):
        cal = CalculadoraLogica.Calculadora()
        if opcion.value == "dos":
            tabla.columns = [ft.DataColumn(ft.Text("P", color="#FFFBE4")), ft.DataColumn(ft.Text("Q", color="#FFFBE4")),
                            ft.DataColumn(ft.Text("Salida", color="#FFFBE4"))]
            datos,result = cal.dos_proposiciones(campo.value)
            row = []
            if datos != "ALGO ANDA MAL...":
                tabla.visible = True
                resultado.value = f'el resultado de hacer la operación: {campo.value} es una {cal.formula_bien_formulada(result)}'
                for i in range(len(datos)):
                    fila = []
                    for j in datos[i]:
                        fila.append(ft.DataCell(ft.Text(j,size=15)))
                    if i%2==0:
                        row.append(ft.DataRow(fila,color="#F2EEB3"))
                    else:
                        row.append(ft.DataRow(fila, color="#7ABF92"))
            else:
                resultado.value = f'La expresión no tiene lógica...'

            tabla.rows = row
            campo.value = ""
        elif opcion.value == "tres":
            tabla.columns = [ft.DataColumn(ft.Text("P",color="#FFFBE4")),ft.DataColumn(ft.Text("Q",color="#FFFBE4")),
                             ft.DataColumn(ft.Text("W",color="#FFFBE4")),ft.DataColumn(ft.Text("Salida",color="#FFFBE4"))]
            datos, result = cal.tres_proposiciones(campo.value)
            row = []
            if datos != "ALGO ANDA MAL...":
                tabla.visible = True
                resultado.value = f'el resultado de hacer la operación: {campo.value} es una {cal.formula_bien_formulada(result)}'
                for i in range(len(datos)):
                    fila = []

                    for j in datos[i]:
                        fila.append(ft.DataCell(ft.Text(j,size=15)))

                    if i % 2 == 0:
                        row.append(ft.DataRow(fila, color="#F2EEB3"))
                    else:
                        row.append(ft.DataRow(fila, color="#7ABF92"))
            else:
                resultado.value = f'La expresión no tiene lógica...'

            tabla.rows = row
            campo.value = ""
        page.update()


    campo = ft.TextField(label="Expresión Lógica...",label_style=ft.TextStyle(color="#1E3833",weight=ft.FontWeight.W_500),
                         hint_text="Ingresa una expresión, ejemplo: p and q", border_color="#4d8f81",width=500)
    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("P",color="#FFFBE4")),
            ft.DataColumn(ft.Text("Q",color="#FFFBE4")),
            ft.DataColumn(ft.Text("SALIDA",color="#FFFBE4")),
        ],
        rows=[],
        border_radius= ft.border_radius.BorderRadius(topRight=10,
                                topLeft=10,bottomLeft=10,bottomRight=10),
        visible=False
        )
    operar = ft.ElevatedButton("Operar ✍️", on_click=operar,
                               style=ft.ButtonStyle(color={ft.MaterialState.DEFAULT: "#1E3833"},
                                                    bgcolor={ft.MaterialState.DEFAULT: "#F22E62"},
                                                    overlay_color="#C72651", shape=ft.RoundedRectangleBorder(radius=10))                               )
    resultado = ft.Text("Aquí descubriras si es una Tautología una Contradicción o una Contingencia 🤔",
                text_align=ft.TextAlign.CENTER,color="#1E3833",size=16)
    botones = ft.Row(controls=[
        ft.ElevatedButton("Disyunción",on_click=dis,
                          style=ft.ButtonStyle(color={ft.MaterialState.DEFAULT:"#1E3833"},
                                               bgcolor={ft.MaterialState.DEFAULT: "#81C99A"},
                                               overlay_color="#72B389",shape=ft.RoundedRectangleBorder(radius=10))),
        ft.ElevatedButton("Conjunción",on_click=con,
                          style=ft.ButtonStyle(color={ft.MaterialState.DEFAULT:"#1E3833"},
                                               bgcolor={ft.MaterialState.DEFAULT: "#81C99A"},
                                               overlay_color="#72B389",shape=ft.RoundedRectangleBorder(radius=10))),
        ft.ElevatedButton("Negación",on_click=neg,
                          style=ft.ButtonStyle(color={ft.MaterialState.DEFAULT:"#1E3833"},
                                               bgcolor={ft.MaterialState.DEFAULT: "#81C99A"},
                                               overlay_color="#72B389",shape=ft.RoundedRectangleBorder(radius=10))),
        ft.ElevatedButton("Disyunción exclusiva",on_click=disE,
                          style=ft.ButtonStyle(color={ft.MaterialState.DEFAULT:"#1E3833"},
                                               bgcolor={ft.MaterialState.DEFAULT: "#81C99A"},
                                               overlay_color="#72B389",shape=ft.RoundedRectangleBorder(radius=10)))
    ],wrap=True,alignment=ft.MainAxisAlignment.CENTER, width=400)

    opcion = ft.RadioGroup(content=ft.Row([
             ft.Radio(value="dos", label="2 proposiciones (p q)", fill_color="#4d8f81",expand=True),
             ft.Radio(value="tres", label="3 proposiciones (p q w)", fill_color="#4d8f81",expand=True)]))


    container1 = ft.Container(content=tabla,expand=True, bgcolor="#3C6E60",padding=100,
                                border_radius=ft.border_radius.BorderRadius(topRight=20,
                                topLeft=0,bottomLeft=0,bottomRight=20),height=hei-36)
    container2 = ft.Column(controls=[ft.Container(opcion,margin=50),
        ft.Text("Ingrese la expresión a evaluar",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,
                color="#1E3833",size=16),
        campo,
        botones,
        resultado,
        operar
    ],expand=True,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=30)

    row = ft.Row(controls=[
        container1,
        container2
    ])

    page.add(row)


ft.app(target=main)