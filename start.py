import cv2
import imutils
import numpy as np
from pytesseract import pytesseract

# Tesseract OCR konfigürasyonu
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

target_number = "88"
required_bright_spots_roi1 = 9

# Parlak Noktaları Tespit Etme Fonksiyonu (ROI İçinde)
def detect_bright_spots_in_roi(roi, threshold_area):
    # Gri tonlamaya çevir
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Gürültüyü azaltmak ve sonuçları iyileştirmek için GaussianBlur uygula
    blurred = cv2.GaussianBlur(gray, (15, 15), 0)

    # Parlak bölgeleri tespit etmek için eşikleme uygula
    _, thresh = cv2.threshold(blurred, 254, 300, cv2.THRESH_BINARY)

    # Konturları bul
    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)

    bright_spots = []

    # Konturlar üzerinde döngü
    for contour in contours:
        # Her konturun alanını hesapla
        area = cv2.contourArea(contour)

        # Belirli bir eşik değerinden büyük olan alanları parlak nokta olarak kabul et
        if area > threshold_area:
            # Konturun merkezini bul
            M = cv2.moments(contour)
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            bright_spots.append((cx, cy))

    return bright_spots

# Kamera bağlantısını başlat
cap = cv2.VideoCapture(0)

# ROI (Region of Interest) koordinatlarını belirle
roi1_x, roi1_y, roi1_w, roi1_h = 100, 100, 200, 100
roi2_x, roi2_y, roi2_w, roi2_h = 170, 200, 70, 70

# Her bir ROI için parlak nokta alan eşik değerini belirle
threshold_area_roi1 = 100
threshold_area_roi2 = 200

# Pass bayrağı
pass_flag = False

while True:
    # Kameradan bir kare al
    ret, frame = cap.read()

    # ROI1'yi seç
    roi1 = frame[roi1_y:roi1_y+roi1_h, roi1_x:roi1_x+roi1_w].copy()

    # ROI1 içindeki parlak noktaları tespit et
    bright_spots_roi1 = detect_bright_spots_in_roi(roi1, threshold_area_roi1)

    # Seçilen bölgeye bir dikdörtgen çiz
    cv2.rectangle(frame, (roi1_x, roi1_y), (roi1_x + roi1_w, roi1_y + roi1_h), (255, 0, 0), 2)

    # ROI2'yi seç
    roi2 = frame[roi2_y:roi2_y+roi2_h, roi2_x:roi2_x+roi2_w].copy()

    # ROI2 içindeki parlak noktaları tespit et
    gray_roi2 = cv2.cvtColor(roi2, cv2.COLOR_BGR2GRAY)
    blur_roi2 = cv2.GaussianBlur(gray_roi2, (5, 5), 0)
    bright_spots_roi2 = detect_bright_spots_in_roi(roi2, threshold_area_roi2)

    # Seçilen bölgeye bir dikdörtgen çiz
    cv2.rectangle(frame, (roi2_x, roi2_y), (roi2_x + roi2_w, roi2_y + roi2_h), (0, 0, 255), 2)

    # Parlak noktaların etrafına çizgi çiz
    for spot in bright_spots_roi1:
        # ROI içindeki koordinatlara çevir
        spot = (spot[0] + roi1_x, spot[1] + roi1_y)
        cv2.circle(frame, spot, 10, (0, 0, 255), -1)  # Kırmızı renk

    for spot in bright_spots_roi2:
        # ROI içindeki koordinatlara çevir
        spot = (spot[0] + roi2_x, spot[1] + roi2_y)
        cv2.circle(frame, spot, 10, (0, 255, 0), -1)  # Yeşil renk

    # ROI2 üzerindeki metni oku ve ekrana yazdır
    # Sayıları algılamak için pytesseract kullanarak metni okuyun
    custom_config = r'--psm 7 outputbase digits'
    text_roi2 = pytesseract.image_to_string(blur_roi2, config=custom_config)

    if text_roi2.strip() == target_number and len(bright_spots_roi1) == required_bright_spots_roi1:
        print("Display Pass")

    # Görüntüyü ekranda gösterin
    cv2.imshow('Video', frame)

    # 'q' tuşuna basılınca döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera bağlantısını ser
