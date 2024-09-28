import cv2
import mediapipe as mp
import numpy as np
import requests
import base64

# Inicialização de variáveis globais e configurações
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils  # Para desenhar os landmarks
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8)

# Classe para filtragem de landmarks com média móvel
class MediaMovel:
    def __init__(self, tamanho=5):
        self.valores = np.zeros((tamanho, 3))  # Uso de NumPy para maior eficiência
        self.index = 0

    def filtrar(self, valor_atual):
        self.valores[self.index % len(self.valores)] = valor_atual
        self.index += 1
        return np.mean(self.valores, axis=0)

filtros_landmarks = [MediaMovel() for _ in range(21)]

# Verificador de gestos com contagem consecutiva
class GestoVerifier:
    def __init__(self, gesto, threshold=5):
        self.gesto = gesto
        self.threshold = threshold
        self.contagem_consecutiva = 0

    def verificar(self, gesto_atual):
        if gesto_atual == self.gesto:
            self.contagem_consecutiva += 1
            if self.contagem_consecutiva >= self.threshold:
                self.contagem_consecutiva = 0
                return True
        else:
            self.contagem_consecutiva = 0
        return False

# Definição dos gestos
verificador_rock = GestoVerifier([0, 1, 0, 0, 1])  # 🤘
verificador_sertanejo = GestoVerifier([1, 0, 0, 0, 1])  # 🤙
verificador_pop = GestoVerifier([0, 1, 1, 0, 0])  # ✌️
verificador_badboy = GestoVerifier([0, 0, 1, 0, 0]);

# Função para enviar dados de gênero
def enviar_genero(genero):
    urls = ['https://expoetec2024.onrender.com/setgender', 'http://localhost:3030/setgender']
    payload = {'gend': genero}
    for url in urls:
        try:
            requests.post(url, json=payload)
        except Exception as e:
            print(f'Erro ao enviar para {url}: {e}')

def enviar_badboy(frame):
    url = 'https://expoetec2024.onrender.com/badboy'
    _, img_encoded = cv2.imencode('.jpg', frame)
    payload = {'image': base64.b64encode(img_encoded).decode('utf-8')}
    try:
        requests.post(url, json=payload)
        print('badboy capturado e enviado!')
    except Exception as e:
        print(f'Erro ao enviar imagem badboy.')

# Função para enviar imagem codificada em Base64
def enviar_imagem(frame):
    url = 'http://localhost:3030/setfeedback'
    _, img_encoded = cv2.imencode('.jpg', frame)
    payload = {'image': base64.b64encode(img_encoded).decode('utf-8')}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f'Erro ao enviar imagem: {e}')

# Função para detecção de gestos
def detect_gestos(frame):
    imgNotMarcker = frame
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    estados_dedos = [0, 0, 0, 0, 0]

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            landmarks_filtrados = [
                filtros_landmarks[i].filtrar(np.array([landmark.x, landmark.y, landmark.z])) 
                for i, landmark in enumerate(hand_landmarks.landmark)
            ]

            # Verificação dos dedos (0 para não levantado, 1 para levantado)
            estados_dedos = [
                1 if landmarks_filtrados[4][0] < landmarks_filtrados[3][0] else 0,  # Polegar
                1 if landmarks_filtrados[8][1] < landmarks_filtrados[6][1] else 0,  # Indicador
                1 if landmarks_filtrados[12][1] < landmarks_filtrados[10][1] else 0, # Médio
                1 if landmarks_filtrados[16][1] < landmarks_filtrados[14][1] else 0, # Anelar
                1 if landmarks_filtrados[20][1] < landmarks_filtrados[18][1] else 0  # Mindinho
            ]

            # Desenhar landmarks e conexões na imagem
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Verificação dos gestos e envio do gênero correspondente
            if verificador_rock.verificar(estados_dedos):
                enviar_genero("rock")
                print("")
            elif verificador_sertanejo.verificar(estados_dedos):
                enviar_genero("sertanejo")
                print("")
            elif verificador_pop.verificar(estados_dedos):
                enviar_genero("pop")
                print("")
            elif verificador_badboy.verificar(estados_dedos):
                enviar_badboy(imgNotMarcker)
                print("")

    return estados_dedos

# Função principal
def main():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cap.set(cv2.CAP_PROP_FPS, 30)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        enviar_imagem(frame)  # Enviar imagem ao servidor
        detect_gestos(frame)  # Detectar gestos
        cv2.imshow('ExpoEtec 2024', frame)  # Mostrar a imagem com landmarks

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
