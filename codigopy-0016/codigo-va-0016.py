# Johan Paulo Aros Reveles

import cv2
from pathlib import Path

# 1. Definir las rutas de trabajo
carpeta_proyecto = Path(__file__).resolve().parent.parent

ruta_original = (
    carpeta_proyecto
    / "img-original-0016"
    / "tigre.jpg"
)

carpeta_resultados = (
    carpeta_proyecto / "resultados-img-0016"
)

# Crear la carpeta de resultados si no existe
carpeta_resultados.mkdir(parents=True, exist_ok=True)

# 2. Leer la imagen original con imread
img0016 = cv2.imread(str(ruta_original))

# Comprobar que la imagen se haya leído correctamente
if img0016 is None:
    raise FileNotFoundError(
        f"No se pudo leer la imagen: {ruta_original}"
    )

# 3. Rotar la imagen 90 grados en sentido horario
img90_0016 = cv2.rotate(
    img0016, cv2.ROTATE_90_CLOCKWISE
)

# 4. Rotar la imagen 45 grados
alto, ancho = img0016.shape[:2]

centro = (ancho // 2, alto // 2)

matriz_rotacion = cv2.getRotationMatrix2D(
    centro, 45, 1.0
)

img45_0016 = cv2.warpAffine(
    img0016,
    matriz_rotacion,
    (ancho, alto)
)

# 5. Redimensionar a 600 píxeles de ancho
# y 500 píxeles de alto
img600x500_0016 = cv2.resize(
    img0016, (600, 500)
)

# 6. Dibujar un rectángulo rojo de 100 x 200
# píxeles sobre una copia de la imagen original
img_rojo_0016 = img0016.copy()

x1, y1 = 50, 50
x2, y2 = x1 + 100, y1 + 200

cv2.rectangle(
    img_rojo_0016,
    (x1, y1),
    (x2, y2),
    (0, 0, 255),
    3
)

# 7. Mostrar las cinco imágenes con sus títulos
cv2.imshow("tigre original 0016", img0016)

cv2.imshow("tigre 90 0016", img90_0016)

cv2.imshow("tigre 45 0016", img45_0016)

cv2.imshow(
    "tigre 600x500 0016",
    img600x500_0016
)

cv2.imshow("tigre rojo 0016", img_rojo_0016)

# 8. Guardar las cuatro imágenes procesadas
cv2.imwrite(
    str(carpeta_resultados / "img-Tigre-0016.jpg"),
    img90_0016
)

cv2.imwrite(
    str(carpeta_resultados / "img-Tigre2-0016.jpg"),
    img45_0016
)

cv2.imwrite(
    str(carpeta_resultados / "img-Tigre3-0016.jpg"),
    img600x500_0016
)

cv2.imwrite(
    str(carpeta_resultados / "img-Tigre4-0016.jpg"),
    img_rojo_0016
)

# 9. Esperar una tecla y cerrar las ventanas
print("Imágenes procesadas y guardadas.")
print("Presiona una tecla en las ventanas para finalizar.")

cv2.waitKey(0)
cv2.destroyAllWindows()