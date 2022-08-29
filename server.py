from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/detalhes')
def detalhes():
    produto = request.args.get('codigo')
    if produto == "1":    
        nome="Paçoca"
        descricao="Macho, 8 meses, castrado, vacinado e chipado. Muito amoroso e brincalhão"
        imagem="/static/pacoca.jpg"
        return render_template('detalhes.html', nome=nome, descricao=descricao, imagem=imagem)

    if produto == "2":    
        nome="Princesa"
        descricao="Fêmea, 15 meses, castrada, vacinada e chipada. Bem sossegada e adora um colinho"
        imagem="/static/princesa.jpg"
        return render_template('detalhes.html', nome=nome, descricao=descricao, imagem=imagem)

    if produto == "3":    
        nome="Pingato"
        descricao="Macho, 2 anos, castrado, vacinado e chipado. Brincalhão e companheiro. Mia bastante"
        imagem="/static/pingato.jpeg"
        return render_template('detalhes.html', nome=nome, descricao=descricao, imagem=imagem)

    if produto == "4":    
        nome="Chantilly"
        descricao="Macho, 3 anos, castrado, vacinado e chipado. Muito bonzinho e gosta de atenção. Mia bastante"
        imagem="/static/chantilly.jpg"
        return render_template('detalhes.html', nome=nome, descricao=descricao, imagem=imagem)

    if produto == "5":    
        nome="Marge"
        descricao="Fêmea, 12 meses, castrada, vacinada e chipada. Brincalhona, fofa e exigente. Gosta de muita atenção"
        imagem="/static/marge.jpg"
        return render_template('detalhes.html', nome=nome, descricao=descricao, imagem=imagem)

    if produto == "6":    
        nome="Pastel"
        descricao="Macho, 5 meses, castrado, vacinado e chipado. Muito esperto e brincalhão. Um amiguinho para todas as horas"
        imagem="/static/pastel.jpg"
        return render_template('detalhes.html', nome=nome, descricao=descricao, imagem=imagem)


if __name__ == '__main__':
    app.run(debug=True)






