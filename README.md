# ANPR Flask Web Application with PowerBI Dashboard and Chatbot

The following project was created to solve the issues of vehicular traffic data management within campuses or any enclosed area.
The Flask Web Application has the features to detect vehicular number plates from Images or Videos using TensorFlow's Object Detection Model. The detected data is stored in Google Sheets with the timestammp.
In addition to this, there is a PowerBI dashboard that fetches live data from Sheets and visualizes the fetched data.
Also, a chatbot has been designed powered  

The following concepts were used:
- <b><i>TensorFlow
- OpenCV
- EasyOCR
- Google Sheets API
- OpenAI API
- PowerBI
- Flask
- Pyscript</i></b>

<hr>

### Runnning the app

- ```pip install requirements.txt```
- Due to GitHiub's size limitation, the trained model can't be uploaded into the repository directly. Hence, Jupyter Notebooks with detailed steps have been uploaded in order to set up the model and train it with the images of number plates. Every step must be executed sequentially and in the same order.
- Also generate API Keys for OpenAI and Google Sheets and place them in the config files.
- After setting up the model correctly, run the flask application:
```python main.py```
- To use flask in debugging mode, use ```app.run(debug==True)``` in the main code of main.py

<hr>

### Application Preview

![home-ss](https://github.com/ayushmaanFCB/ANPR-Application-with-PowerBI-Dashboard-and-Chatbot/assets/92968225/48cebf41-2d78-4339-8715-bf0f0b79ca7c)
![Screenshot 2023-04-29 020420](https://github.com/ayushmaanFCB/ANPR-Application-with-PowerBI-Dashboard-and-Chatbot/assets/92968225/4bf518a0-17eb-4ec9-919b-6cf0db404c84)
![Screenshot 2023-05-10 154536](https://github.com/ayushmaanFCB/ANPR-Application-with-PowerBI-Dashboard-and-Chatbot/assets/92968225/4a1c3ca0-63fe-4f2c-9cc3-5ce356e69a21)
![Screenshot 2023-05-10 154610](https://github.com/ayushmaanFCB/ANPR-Application-with-PowerBI-Dashboard-and-Chatbot/assets/92968225/a6b8e785-1d0b-4787-b2e3-c05f8977cef6)
![Screenshot 2023-04-29 020703](https://github.com/ayushmaanFCB/ANPR-Application-with-PowerBI-Dashboard-and-Chatbot/assets/92968225/83733d44-8589-40fe-a35d-52475d90f66e)
![Screenshot 2023-04-29 020801](https://github.com/ayushmaanFCB/ANPR-Application-with-PowerBI-Dashboard-and-Chatbot/assets/92968225/1f9af2b5-8036-45f0-b5ac-e80772525d73)

