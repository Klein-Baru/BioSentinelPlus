import flet as ft
import matplotlib.pyplot as plt
import numpy as np
from flet.matplotlib_chart import MatplotlibChart

# This is required for Matplotlib to work with Flet
plt.switch_backend('Agg')

def main(page: ft.Page):
    page.title = "Flet Data Viz"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Generate some sample data
    x = np.linspace(0, 10, 100)
    y = np.sin(x) + np.random.normal(0, 0.2, len(x)) # Sine wave with some noise

    # Create a Matplotlib figure
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x, y, label="Sine Wave with Noise")
    ax.set_title("Simple Line Chart")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.grid(True)
    ax.legend()
    plt.tight_layout() # Adjust layout to prevent labels from overlapping

    # Create a Flet MatplotlibChart control
    # You pass the Matplotlib figure directly to it
    chart_control = MatplotlibChart(fig, expand=True)

    page.add(
        ft.Column(
            [
                ft.Text("My Data Visualization App", size=24, weight=ft.FontWeight.BOLD),
                ft.Container(
                    content=chart_control,
                    width=page.width * 0.9, # Take 90% of page width
                    height=page.height * 0.6, # Take 60% of page height
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(10),
                    #bgcolor=ft.colors.BLUE_GREY_100,
                    padding=10
                ),
                ft.Text("Generated using Flet and Matplotlib", size=14,), #color=ft.colors.GREY_600),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=main)