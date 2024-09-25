import cv2
import mediapipe as mp
import numpy as np
import requests  # Importa a biblioteca requests

# Inicializa o MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8)

# Filtro de média móvel para suavização dos pontos
class MediaMovel:
    def __init__(self, tamanho=5):
        self.tamanho = tamanho
        self.valores = []

    def filtrar(self, valor_atual):
        self.valores.append(valor_atual)
        if len(self.valores) > self.tamanho:
            self.valores.pop(0)
        return np.mean(self.valores, axis=0)

# Inicializa filtros para os 21 pontos de cada mão
filtros_landmarks = [MediaMovel() for _ in range(21)]

# Classe para monitorar as detecções consecutivas
class GestoVerifier:
    def __init__(self, gesto, threshold=5):
        self.gesto = gesto
        self.threshold = threshold
        self.contagem_consecutiva = 0

    def verificar(self, gesto_atual):
        if gesto_atual == self.gesto:
            self.contagem_consecutiva += 1
        else:
            self.contagem_consecutiva = 0

        if self.contagem_consecutiva >= self.threshold:
            self.contagem_consecutiva = 0  # Reseta após a confirmação
            return True
        return False

# Inicializa verificadores para cada gesto
verificador_rock = GestoVerifier([1, 1, 0, 0, 1])  
verificador_shaka = GestoVerifier([1, 0, 0, 0, 1])  
verificador_paz = GestoVerifier([0, 1, 1, 0, 0])   

import requests

def enviar_genero(genero):
    url1 = 'https://expoetec2024.onrender.com/setgender'
    payload = {'gend': genero}

    try:
        response1 = requests.post(url1, json=payload)
        print(f'Resposta do servidor 1: {response1.text}')

    except Exception as e:
        print('')
        
def enviar_genero2(genero):
    url2 = 'http://localhost:3000/setgender'
    payload = {'gend': genero}

    try:
        response2 = requests.post(url2, json=payload)
        print(f'Resposta do servidor 2: {response2.text}')

    except Exception as e:
        print('')


def detect_gestos(frame):
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)
    estados_dedos = [0] * 5

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            landmarks = hand_landmarks.landmark

            landmarks_filtrados = [
                filtros_landmarks[i].filtrar(np.array([landmark.x, landmark.y, landmark.z])) 
                for i, landmark in enumerate(landmarks)
            ]

            estados_dedos[0] = 1 if landmarks_filtrados[4][0] < landmarks_filtrados[3][0] else 0  # Polegar
            estados_dedos[1] = 1 if landmarks_filtrados[8][1] < landmarks_filtrados[6][1] else 0  # Indicador
            estados_dedos[2] = 1 if landmarks_filtrados[12][1] < landmarks_filtrados[10][1] else 0  # Médio
            estados_dedos[3] = 1 if landmarks_filtrados[16][1] < landmarks_filtrados[14][1] else 0  # Anelar
            estados_dedos[4] = 1 if landmarks_filtrados[20][1] < landmarks_filtrados[18][1] else 0  # Mindinho

            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if verificador_rock.verificar(estados_dedos):
                enviar_genero("rock")
                enviar_genero2("rock")
            elif verificador_shaka.verificar(estados_dedos):
                enviar_genero("reggae")
                enviar_genero2("reggae")
            elif verificador_paz.verificar(estados_dedos):
                enviar_genero("hip-hop")
                enviar_genero2("hip-hop")

    return estados_dedos

def main():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cap.set(cv2.CAP_PROP_FPS, 30)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        detect_gestos(frame)

        cv2.imshow('ExpoEtec 2024', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()