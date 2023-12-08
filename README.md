# Parlak Nokta ve OCR Projesi

Bu proje, bir kamera ile görüntü yakalayarak parlak noktaları ve metinleri algılayan basit bir görüntü işleme uygulamasını içermektedir. Özellikle, proje aşağıdaki özelliklere sahiptir:

- **Parlak Nokta Algılama**: İki farklı ROI (Region of Interest) içinde parlak noktaları tespit eder.
- **OCR (Optical Character Recognition)**: Bir ROI içindeki metni Tesseract OCR kullanarak okur.
- **Özel Kontroller ve Pass Mesajı**: Belirli koşullar sağlandığında, örneğin "88" sayısı algılandığında ve bir ROI içinde belirli sayıda parlak nokta tespit edildiğinde "Pass" mesajını gösterir.

## Kurulum

1. Proje dosyalarını bilgisayarınıza kopyalayın.
2. Gerekli Python paketlerini yüklemek için terminal veya komut istemcisine şu komutu yazın:

   ```bash
   pip install opencv-python imutils pytesseract

1. Tesseract OCR'ın bilgisayarınıza yüklü olduğundan emin olun. [Tesseract OCR İndirme Sayfası](https://github.com/tesseract-ocr/tesseract "Tesseract OCR İndirme Sayfası")

3. `main.py` dosyasını çalıştırarak projeyi başlatın.

**Kullanım**

1. Kamera görüntüsü ekranda görüntülenecektir.
2. ROI1 içinde belirli sayıda parlak nokta ve ROI2 içinde "88" metni algılandığında "Pass" mesajı görüntülenir.

**Notlar**

- Projenin çalışması için bir kamera gereklidir.
- Tesseract OCR'ın doğru çalışabilmesi için uygun dil dosyalarının yüklü olduğundan emin olun.

**Katkılar**

Eğer bir hata bulursanız veya iyileştirmeler önerirseniz, lütfen bir konu açın veya bir çekme isteği gönderin. Katkılarınız her zaman memnuniyetle karşılanır.

**Lisans:** [MIT License](https://chat.openai.com/c/LICENSE "MIT License")
