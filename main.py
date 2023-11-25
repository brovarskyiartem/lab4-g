from PIL import Image, ImageDraw
import numpy as np

# Зчитування датасету з файлу
dataset_path = 'dataset.txt'
dataset = np.loadtxt(dataset_path)

# Задання точки сходження та зміщення зображення
vanishing_point = np.array([960, 540])
z = 100

# Створення матриці центральної проекції
projection_matrix = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1/z]
])

# Проектування точок датасету
projected_dataset = np.dot(projection_matrix, np.vstack([dataset.T, np.ones_like(dataset[:, 0])])).T[:, :2]

# Встановлення розмірів полотна
canvas_size = (960, 540)

# Створення білого зображення
image = Image.new("RGB", (canvas_size[0], canvas_size[1]), "white")
draw = ImageDraw.Draw(image)

# Масштабування та зміщення координат для відображення на новому полотні
scaled_dataset = (projected_dataset * 0.5).astype(int) + np.array(canvas_size) // 2

# Відображення точок на зображенні
for point in scaled_dataset:
    draw.ellipse([point[0] - 2, point[1] - 2, point[0] + 2, point[1] + 2], fill=(0, 0, 255))  # Сині точки

# Збереження зображення
output_path = 'результат.jpg'
image.save(output_path)

print(f"Зображення збережено у файл {output_path}")
