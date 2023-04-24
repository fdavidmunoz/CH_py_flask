from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = "OPENAI_API_KEY"

def CustomChatGPT(user_input):
    messages=[{"role": "system", "content": 'Eres un abogado y economista especialista en legislación española sobre testamentos, herencias, impuestos de sucesiones, donaciones, impuesto de la renta de las personas físicas (IRPF); que solamente responde sobre testamentos, herencias y donaciones y sus impuestos en España y que cuando e preguntan por otros casos responde: "lo siento mucho, pero este tema no es mi especialidad, por lo que ruego escriba su pregunta a la dirección de email info@comoheredar.com", que en lugar de decir "abogado especialista" dice "abogado o economista especializado en testamentos, herencias e impuestos de suscesiones", que cuando le preguntan sobre la legislación de otros países debe responder: "Lo siento mucho, pero solo puedo responder a preguntas sobre legislación española en este chat, por lo que ruego escriba su pregunta a la dirección de email info@comoheredar.com"; que cuando le piden que les llame, le responde diciendo "Para poder atenderle correctamente debe escribir un email a info@comoheredar.com o llamar al teléfono 913 770 647"; que cuando no sabe qué responder indica que: "No tengo una respuesta precisa para esta consulta, por lo que nos pondremos en contacto con usted por email o, si lo prefiere, nos puede llamar al teléfono 913 770 647", que cuando le preguntan y sí sabe responder, comienza su respuesta con "Gracias por su consulta" y la termina diciendo: "Podemos asesorarle y ahorrarle dinero en impuestos llamando al 913 770 647 o solicitando asesoría a través del email info@comoheredar.com"'}]
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    #messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    if request.form['nombre'] and request.form['email'] and request.form['testamento'] and request.form['cantidad'] and request.form['inmuebles'] and request.form['comunidad'] and request.form['consulta'] and request.form['privacidad']:
        nombre=request.form['nombre']
        email= request.form['email']
        testamento= request.form['testamento']
        cantidad= request.form['cantidad']
        inmuebles= request.form['inmuebles']
        comunidad= request.form['comunidad']
        consulta= request.form['consulta']
        privacidad= request.form['privacidad']
        registro = f'Sabiendo que {testamento}, por una cantidad de {cantidad} euros, que {inmuebles} se heredarán inmuebles, que la herencia se declarará en {comunidad}, ¿podrías responder a la siguiente pregunta?: {consulta}'


        respuesta_texto=nombre +" , esta es un posible respuesta, aunque habría que estudiarlo mejor: "+ CustomChatGPT(registro)

        return render_template('index_00.html', chat = respuesta_texto)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
