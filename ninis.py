import matplotlib.pyplot as plt

# Datos para la gráfica
labels = ['Total Jóvenes', 'Hombres', 'Mujeres']
poblacion_miles = [2597, 881, 1716]  # Población en miles
proporcion = [23.1, 7.8, 15.3]  # Proporción en %

# Crear figura y ejes
fig, ax1 = plt.subplots()

# Gráfica de barras para la población en miles
color = '#061dc0'
ax1.set_xlabel('Categoría')
ax1.set_ylabel('Población (miles)', color=color)
ax1.bar(labels, poblacion_miles, color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Crear un segundo eje para la proporción en porcentaje
ax2 = ax1.twinx()  
color = 'tab:green'
ax2.set_ylabel('Proporción (%)', color=color)
ax2.plot(labels, proporcion, color=color, marker='o', linestyle='dashed')
ax2.tick_params(axis='y', labelcolor=color)

# Añadir grilla
ax1.grid(True)

# Añadir título
plt.title('Jóvenes entre 15 y 28 años que no estudian ni trabajan')

# Mostrar la gráfica
plt.show()