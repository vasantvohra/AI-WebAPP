## AI Web APP
A bundle of applications developed using Django.
<details>
 <summary>Applications!</summary>

- Signture Extraction and Verification
	- Image Processing
		- OpenCV - ROI, Canny Edge, HSV, Morphological Transformation
	 - Image Classification
		 - Siamese Neural Network - Signature Verification
- Waste Segregation
	- Convolution Neural Network
 - Object Detection
	 - YOLO 
 - Automatic License Plate Recognition 
	 - Viola Jones Algorithm - HaarCascades  
	 - YOLO - Trucks License plate identification ( Integration pending)
	-	pytesseract for OCR, MLP (pending)
</details>

### Docker Image

<details><summary> Docker-Hub</summary><blockquote>

```sh
docker pull vvohra/webapp:v1
```
or
```sh
version: '3.1'

services:
  db:
    image: postgres
    environment:
      POSTGRES_DB: "db"
      POSTGRES_HOST_AUTH_METHOD: "trust"
  web:
    image: vvohra/webapp:v1
    command:
      - /bin/bash
      - -c
      - |
        python manage.py migrate
        python manage.py runserver 0.0.0.0:8000
    ports:
      - "8000:8000"
    depends_on:
      - db
```
```sh
docker-compose up
```
</blockquote></details>

<details><summary> Build local Docker container</summary><blockquote>

```sh
docker-compose build
docker-compose run web bash
python3 manage.py migrate
python3 manage.py createsuperuser
exit
docker-compose up
0.0.0.0:8000
```
</blockquote></details>

### Screenshots
![Home](https://raw.githubusercontent.com/vasantvohra/AI-WebAPP/master/media/screencapture/Homepage.jpg "Homepage")
![Login](https://raw.githubusercontent.com/vasantvohra/AI-WebAPP/blob/master/media/screencapture/Login%20Screen.jpg "Login")
![Signature Extraction](https://raw.githubusercontent.com/vasantvohra/AI-WebAPP/blob/master/media/screencapture/SignatureExtract.jpg "Signature Extraction")
![Signature Verification](https://raw.githubusercontent.com/vasantvohra/AI-WebAPP/blob/master/media/screencapture/signatureVerification.jpg "Signature Verification")
![Waste Segregation](https://raw.githubusercontent.com//vasantvohra/AI-WebAPP/blob/master/media/screencapture/wasteseg2.jpg "Waste Segregation")
![Object Detection](https://raw.githubusercontent.com/vasantvohra/AI-WebAPP/blob/master/media/screencapture/ObjectDetection.png "Object Detection")
![ALPR](https://raw.githubusercontent.com/vasantvohra/AI-WebAPP/blob/master/media/screencapture/ALPR.jpg "ALPR")
![About](https://raw.githubusercontent.com/vasantvohra/AI-WebAPP/blob/master/media/screencapture/About.png "About")
