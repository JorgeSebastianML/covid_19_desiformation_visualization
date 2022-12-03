import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image, ImageDraw
from streamlit_autorefresh import st_autorefresh

def draw_image(w, h, w2, h2, image2):
    
    # create rectangle image
    img1 = ImageDraw.Draw(image2)  
    #img1.rectangle([(w,h),(w2,h2)],outline="white", width=3)
    img1.ellipse((w, h, w2, h2),outline="white", width=3)
    return image2
    

# Run the autorefresh about every 2000 milliseconds (2 seconds) and stop
# after it's been refreshed 100 times.
image = Image.open('test.jpg')
image2 = image.copy()

count = st_autorefresh(interval=20000, limit=100, key="fizzbuzzcounter")

SHEET_ID = '1bhPe9qsimOtTnpZtgeO8KuuOgP_2TdkXjn7t_MqY3Gk'
SHEET_NAME = 'Form%20Responses'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
df = pd.read_csv(url)
feature_1 = df.iloc[-1]["1"]
feature_2 = df.iloc[-1]["31"]
feature_3 = df.iloc[-1]["71"]
feature_4 = df.iloc[-1]["91"]

if feature_1 == '“Alemania declara que comprueban que el Covid-19 se instala en la garganta durante 7 días, por lo tanto, las gárgaras de agua con sal y bicarbonato, varias veces al día cambia el pH del cuerpo y el virus muere.”':
    w = 255
    h = 258
    w2 = w + 70
    h2 = h + 70
    image2 = draw_image(w, h, w2, h2, image2)
elif feature_1 == "Ninguno de los anteriores.":
    w = 270
    h = 102
    w2 = w + 155
    h2 = h + 155
    image2 = draw_image(w, h, w2, h2, image2)
elif feature_1 == '“El Covid-19 se quita con Dolex Gripa, Noraver noche, gárgaras con sal, limón y agua tibia.”':
    w = 394
    h = 247
    w2 = w + 30
    h2 = h + 30
    image2 = draw_image(w, h, w2, h2, image2)
elif feature_1 == '“Mi otra hermana diabética con 62 años se recuperó hoy tomando cordoncillo con tajada de limón regional.”':
    w = 188
    h = 201
    w2 = w + 20
    h2 = h + 20
    image2 = draw_image(w, h, w2, h2, image2)

if feature_2 == "Youtube - Dr. Raul Salazar y COVID":
    w = 525
    h = 525
    w2 = w + 80
    h2 = h + 80
    image2 = draw_image(w, h, w2, h2, image2)
elif feature_2 == 'Canal 1 - Enjuague bucal "mata " el COVID':
    w = 615
    h = 520
    w2 = w + 70
    h2 = h + 70
    image2 = draw_image(w, h, w2, h2, image2)
elif feature_2 == 'Ninguna de las anteriores':
    w = 500
    h = 430
    w2 = w + 90
    h2 = h + 90
    image2 = draw_image(w, h, w2, h2, image2)
elif feature_2 == 'Facebook - Científico colombiano tiene la cura del COVID':
    w = 597
    h = 406
    w2 = w + 20
    h2 = h + 20
    image2 = draw_image(w, h, w2, h2, image2)

if feature_3 == 'Ninguna de las anteriores':
    w = 737
    h = 109
    w2 = w + 185
    h2 = h + 185
    image2 = draw_image(w, h, w2, h2, image2)
elif feature_3 == 'Agua con Zinc':
    w = 896
    h = 269
    w2 = w + 30
    h2 = h + 30
    image2 = draw_image(w, h, w2, h2, image2)
elif feature_3 == 'Agua con Limón':
    w = 942
    h = 159
    w2 = w + 40
    h2 = h + 40
    image2 = draw_image(w, h, w2, h2, image2)

if feature_4 == 'Página oficial del gobierno y tratamientos':
    w = 1032
    h = 415
    w2 = w + 192
    h2 = h + 192
    image2 = draw_image(w, h, w2, h2, image2)
elif feature_4 == 'Ninguna de las anteriores':
    w = 1040
    h = 370
    w2 = w + 30
    h2 = h + 30
    image2 = draw_image(w, h, w2, h2, image2)
elif feature_4 == 'FDA y evitar el fraude':
    w = 975
    h = 437
    w2 = w + 30
    h2 = h + 30
    image2 = draw_image(w, h, w2, h2, image2)
elif feature_4 == 'OPS y el ajo':
    w = 992
    h = 526
    w2 = w + 20
    h2 = h + 20
    image2 = draw_image(w, h, w2, h2, image2)


st.image(image2)

