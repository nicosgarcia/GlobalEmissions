import random

import flet as ft
import pandas as pd

    # LOADING IN THE DATA BASE

carbon_emission_data = pd.read_csv("global_Carbon_Emissions.csv")


    # CREATION OF THE MAIN PAGE

def main(page: ft.Page):
    page.bgcolor = '#080917' # background color

    # TEXT REFERENCES FOR FUTURE PURPOSES

    text_ref1 = ft.Ref[ft.Text]()
    text_ref2 = ft.Ref[ft.Text]()
    text_refEmi3 = ft.Ref[ft.Text]()
    text_refEmi4 = ft.Ref[ft.Text]()
    text_refScore = ft.Ref[ft.Text]()

    # BACKGROUND COLOR CHANGE ON HOVER

    def changebg(e):
        e.control.bgcolor = '#1e1542' if e.data == "true" else '#150d30'
        e.control.update()

    # GENERATES A RANDOM COUNTRY FROM THE DATABASE

    def paisAleatorio():
        numeroAleatorio = random.randint(0, 242)

        pais = carbon_emission_data.iloc[numeroAleatorio, 0]

        emission = carbon_emission_data.iloc[numeroAleatorio, 2]

        return pais, emission  # Storing the data inside variables


    # THIS FUNCTION WILL GET THE TEXT VALUE FROM THE CONTAINER WE CLICK ON, YOUR CURRENT SCORE AND THE EVENT


    def higher_num(ref, ref2, leaderboard, e):

        # Generates a random country and store the data inside p and Emi

        p, Emi = paisAleatorio()

        # CHECK IF THE COUNTRY YOU CLICK IS HIGHER THAN THE OTHER ONE, IF ITS NOT, YOUR SCORE GOES TO ZERO

        if ref == text_ref1 and ref2 == text_refEmi3:

            if ref2.current.value >= text_refEmi4.current.value:
                leaderboard += 1
                text_refScore.current.value = leaderboard


            else:
                text_refScore.current.value = 0

            # Using the data from p and Emi to change the country you clicked

            ref.current.value = p
            ref2.current.value = float(Emi)

            # Changing the other country

            outroPais(text_ref2, text_refEmi4)


        # CHECK IF THE COUNTRY YOU CLICK IS HIGHER THAN THE OTHER ONE, IF ITS NOT YOUR SCORE GOES TO ZERO


        if ref == text_ref2 and ref2 == text_refEmi4:

            if ref2.current.value >= text_refEmi3.current.value:
                leaderboard += 1
                text_refScore.current.value = leaderboard


            else:
                text_refScore.current.value = 0

            # Using the data from p and Emi to change the country you clicked

            ref.current.value = p
            ref2.current.value = float(Emi)

            # Changing the other country

            outroPais2(text_ref1, text_refEmi3)

        # Update to show changes

        page.update()


    def outroPais(refer1, refer2):
        p, Emi = paisAleatorio()

        refer1.current.value = p
        refer2.current.value = float(Emi)

    def outroPais2(refer1, refer2):
        p, Emi = paisAleatorio()

        refer1.current.value = p
        refer2.current.value = float(Emi)


    score = ft.Container(
        width=200,
        height=100,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.BLACK87,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    ref=text_refScore, # Using the text references
                    size=40,
                    value="CLIQUE PARA COMEÇAR",
                    text_align=ft.TextAlign.CENTER,
                    color=ft.colors.WHITE,
                )
            ]
        )
    )

    player_part = ft.Container(
        data="player",
        width=300,
        height=page.height/1.55,
        alignment=ft.alignment.top_center,
        bgcolor='#150d30',
        on_hover=changebg,
        on_click=lambda e: higher_num(text_ref1, text_refEmi3, text_refScore.current.value, e),
        border_radius=50,
        content=ft.Column(
            height=page.height / 1.38,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(
                            ft.Text(
                                ref=text_ref1, # Using the text references
                                width=700,
                                value="",
                                size=50,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.colors.AMBER,
                            )
                        ),


                        ft.Container(
                            ft.Text(
                                ref=text_refEmi3, # Using the text references
                                opacity=0,
                                width=700,
                                value="",
                                size=10,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.colors.AMBER,
                            )
                        )
                    ]
                )
            ]
        )
    )

    bot_part = ft.Container(
        data="emissions",
        width=300,
        height=page.height / 1.55,
        alignment=ft.alignment.top_center,
        bgcolor='#150d30',
        on_hover=changebg,
        on_click=lambda e: higher_num(text_ref2, text_refEmi4, text_refScore.current.value, e),
        border_radius=50,
        content=ft.Column(
            height=page.height / 1.38,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(
                            ft.Text(
                                ref=text_ref2, # Using the text references
                                width=700,
                                value="",
                                size=50,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.colors.AMBER,
                            )
                        ),

                        ft.Container(
                            ft.Text(
                                ref=text_refEmi4, # Using the text references
                                opacity=0,
                                width=700,
                                value="",
                                size=10,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.colors.AMBER,
                            )
                        )
                    ]
                )
            ]
        )
    )

    layout = ft.Container(
        expand=True,
        bgcolor=ft.colors.BLACK38,
        content=ft.ResponsiveRow(
            columns=2,
            controls=[
                player_part,
                score,
                bot_part
            ]
        )
    )

    ft.Stack([
        player_part,
        score,
        bot_part
    ])

    # When the app loads, it will generate 2 random countries

    outroPais(text_ref2, text_refEmi4)
    outroPais2(text_ref1, text_refEmi3)

    # Set the score to zero

    text_refScore.current.value = 0

    page.update()

    page.add(layout)


# Iniciate the app

if __name__ == '__main__':
    ft.app(target=main)



