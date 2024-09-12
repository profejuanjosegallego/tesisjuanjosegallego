import matplotlib.pyplot as plt

# Datos para la gráfica
labels = ['TGP', 'TO', 'TD']  # Indicadores
valores_2023 = [58.4, 48.8, 16.4]  # Valores de 2023
valores_2024 = [59.6, 49.2, 17.5]  # Valores de 2024

# Configuración del gráfico de barras
x = range(len(labels))  # Posición en el eje x para cada indicador
width = 0.35  # Ancho de las barras

fig, ax = plt.subplots()  # Crear la figura y los ejes
ax.bar(x, valores_2023, width, label='2023', color='#061dc0')  # Barras personalizadas para 2023
ax.bar([i + width for i in x], valores_2024, width, label='2024', color='#0f8641')  # Barras personalizadas para 2024

# Configuración de etiquetas y títulos
ax.set_xlabel('Indicadores')  # Etiqueta del eje x
ax.set_ylabel('Porcentaje (%)')  # Etiqueta del eje y
ax.set_title('Comparación de TGP, TO y TD (2023 vs 2024)')  # Título de la gráfica
ax.set_xticks([i + width / 2 for i in x])  # Posición de las etiquetas en el eje x
ax.set_xticklabels(labels)  # Nombres de los indicadores en el eje x
ax.legend()  # Añadir leyenda

# Activar la grilla
ax.grid(True)

# Mostrar la gráfica
plt.show()
