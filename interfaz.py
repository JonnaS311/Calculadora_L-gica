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
                resultado.value = f'el resultado de hacer la operación: {campo.value} es una {cal.formula_bien_formulada(result)}'
                for i in range(len(datos)):
                    fila = []
                    for j in datos[i]:
                        fila.append(ft.DataCell(ft.Text(j)))
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
                resultado.value = f'el resultado de hacer la operación: {campo.value} es una {cal.formula_bien_formulada(result)}'
                for i in range(len(datos)):
                    fila = []

                    for j in datos[i]:
                        fila.append(ft.DataCell(ft.Text(j)))

                    if i % 2 == 0:
                        row.append(ft.DataRow(fila, color="#F2EEB3"))
                    else:
                        row.append(ft.DataRow(fila, color="#7ABF92"))
            else:
                resultado.value = f'La expresión no tiene lógica...'

            tabla.rows = row
            campo.value = ""
        page.update()


    campo = ft.TextField(label="Underlined", border="UNDERLINE", hint_text="Expresión Lógica", border_color="#4d8f81",width=500)
    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("P",color="#FFFBE4")),
            ft.DataColumn(ft.Text("Q",color="#FFFBE4")),
            ft.DataColumn(ft.Text("SALIDA",color="#FFFBE4")),
        ],
        rows=[],
        border=ft.border.all(2, "#7ABF92"),
        border_radius= ft.border_radius.BorderRadius(topRight=10,
                                topLeft=10,bottomLeft=10,bottomRight=10),
        )
    operar = ft.ElevatedButton("Operar 🧠", on_click=operar)
    resultado = ft.Text("Aquí descubriras si es una Tautología una Contradicción o una Contingencia 🤔",
                text_align=ft.TextAlign.CENTER,color="#1E3833")
    botones = ft.Row(controls=[
        ft.ElevatedButton("Disyunción",on_click=dis),
        ft.ElevatedButton("Conjunción",on_click=con),
        ft.ElevatedButton("Negación",on_click=neg),
        ft.ElevatedButton("Disyunción exclusiva",on_click=disE)
    ],wrap=True,alignment=ft.MainAxisAlignment.CENTER, width=400)

    opcion = ft.RadioGroup(content=ft.Column([
            ft.Radio(value="dos", label="2 proposiciones", fill_color="#4d8f81"),
            ft.Radio(value="tres", label="3 proposiciones", fill_color="#4d8f81")]))

    container1 = ft.Container(content=tabla,expand=True, bgcolor="#C42550",padding=10,
                                border_radius=ft.border_radius.BorderRadius(topRight=20,
                                topLeft=0,bottomLeft=0,bottomRight=20),height=hei-36)
    container2 = ft.Column(controls=[opcion
        ,
        ft.Text("Ingrese la expresión a evaluar",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color="#1E3833"),
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