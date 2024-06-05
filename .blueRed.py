import cv2
import numpy as np

def detect_color(frame, lower_bound, upper_bound, color_name):
    # Converter a imagem para o espaço de cores HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Criar a máscara para a cor
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Encontrar contornos na máscara
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Desenhar retângulos ao redor dos contornos detectados
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Filtrar pequenos contornos
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, color_name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    return frame

# Definir os intervalos de cor em HSV
# Intervalo para a cor azul
lower_blue = np.array([100, 150, 50])
upper_blue = np.array([140, 255, 255])

# Intervalo para a cor vermelha mais intensa
lower_red = np.array([0, 150, 150])
upper_red = np.array([10, 255, 255])

# Capturar o vídeo da webcam
cap = cv2.VideoCapture(0)

while True:
    # Ler um frame do vídeo
    ret, frame = cap.read()
    if not ret:
        break

    # Detectar a cor azul
    frame = detect_color(frame, lower_blue, upper_blue, "Blue")

    # Detectar a cor vermelha
    frame = detect_color(frame, lower_red, upper_red, "Red")

    # Mostrar o resultado
    cv2.imshow('Original', frame)

    # Pressione 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar os recursos
cap.release()
cv2.destroyAllWindows()

