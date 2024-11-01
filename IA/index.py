import cv2
import mediapipe as mp
import numpy as np
import requests
import base64
import threading

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils  
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8)

class MediaMovel:
    def __init__(self, tamanho=8):
        self.valores = np.zeros((tamanho, 3))  
        self.index = 0

    def filtrar(self, valor_atual):
        self.valores[self.index % len(self.valores)] = valor_atual
        self.index += 1
        return np.mean(self.valores, axis=0)

filtros_landmarks = [MediaMovel() for _ in range(21)]

class GestoVerifier:
    def __init__(self, gesto, threshold=8):
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

verificador_rock = GestoVerifier([0, 1, 0, 0, 1])  # 🤘
verificador_sertanejo = GestoVerifier([1, 0, 0, 0, 1])  # 🤙
verificador_pop = GestoVerifier([0, 1, 1, 0, 0])  # ✌️
verificador_badboy = GestoVerifier([0, 0, 1, 0, 0])

def enviar_genero(genero):
    def enviar():
        urls = ['https://expoetex2024.onrender.com/setgender', 'http://localhost:3030/setgender']
        payload = {'gend': genero}
        for url in urls:
            try:
                requests.post(url, json=payload)
            except Exception as e:
                print(f'')
    threading.Thread(target=enviar).start()

def enviar_badboy(frame):
    def enviar():
        url = 'https://expoetex2024.onrender.com/badboy'
        url2 = 'http://localhost:3030/accountbadboy'
        _, img_encoded = cv2.imencode('.jpg', frame)
        print("")
        payload = {'image': base64.b64encode(img_encoded).decode('utf-8')}
        try:
            requests.get(url2)
            requests.post(url, json=payload)
        except Exception as e:
            print(f'')

    threading.Thread(target=enviar).start()

def enviar_imagem(frame):
    def enviar():
        url = 'http://localhost:3030/setfeedback'
        _, img_encoded = cv2.imencode('.jpg', frame)
        payload = {'image': base64.b64encode(img_encoded).decode('utf-8')}
        try:
            requests.post(url, json=payload)
        except Exception as e:
            print(f'')
    threading.Thread(target=enviar).start()

def detect_gestos(frame):
    imgNotMarcker = frame.copy()
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    estados_dedos = [0, 0, 0, 0, 0]

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            landmarks_filtrados = [
                filtros_landmarks[i].filtrar(np.array([landmark.x, landmark.y, landmark.z])) 
                for i, landmark in enumerate(hand_landmarks.landmark)
            ]

            estados_dedos = [
                1 if landmarks_filtrados[4][0] < landmarks_filtrados[3][0] else 0, 
                1 if landmarks_filtrados[8][1] < landmarks_filtrados[6][1] else 0,  
                1 if landmarks_filtrados[12][1] < landmarks_filtrados[10][1] else 0, 
                1 if landmarks_filtrados[16][1] < landmarks_filtrados[14][1] else 0, 
                1 if landmarks_filtrados[20][1] < landmarks_filtrados[18][1] else 0  
            ]

            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            if verificador_rock.verificar(estados_dedos):
                enviar_genero("rock")
            elif verificador_sertanejo.verificar(estados_dedos):
                enviar_genero("sertanejo")
            elif verificador_pop.verificar(estados_dedos):
                enviar_genero("pop")
            elif verificador_badboy.verificar(estados_dedos):
                enviar_badboy(imgNotMarcker)
                print("")

    enviar_imagem(frame)
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
