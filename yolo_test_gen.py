import cv2
from ultralytics import YOLO

iterdd = 0

def fun(qual,model):

    global iterdd
    iterdd += 1
    
    # Inicialize o modelo YOLO
    model = YOLO(model)

    # Abra o arquivo de vídeo
    cap = cv2.VideoCapture(f'out{qual}.mp4')

    # Abra o arquivo de texto para escrever os resultados
    with open(f'res/{iterdd}_{qual}.txt', 'w') as f:
        frame_number = 0
        
        while True:
            # Leia o próximo frame
            ret, frame = cap.read()
            
            if not ret:
                break  # Fim do vídeo
            
            frame_number += 1
            
            # Execute o modelo YOLO no frame atual
            results = model(frame)

            # Extraia as caixas de detecção
            detections = results[0].boxes
            class_ids = detections.cls.cpu().numpy()  # IDs das classes detectadas
            labels = results[0].names  # Nomes das classes (como 'car', 'person', 'truck')

            # Contadores para as classes de interesse
            counts = {'car': 0, 'person': 0}
            
            for class_id in class_ids:
                # Pegue o nome da classe detectada
                label_name = labels[int(class_id)]

                # Se for 'truck', tratamos como 'car'
                if label_name == 'truck':
                    counts['car'] += 1
                elif label_name in counts:
                    counts[label_name] += 1

            # Prepare a string de detecção (ex.: "5 car, 8 person")
            detection_str = ', '.join([f"{count} {label}" for label, count in counts.items() if count > 0])
            
            # Escreva a detecção no arquivo de texto
            f.write(detection_str + '\n')
            
            print(f"Processed frame {frame_number}")

    # Libere o objeto de captura de vídeo
    cap.release()


models = ["models/yolo11s.pt","models/yolo11n.pt","models/yolo11l.pt","models/yolo11m.pt"]
quals = [144,360,720,1080]

for m in models:
    for q in quals:
        fun(q,m)