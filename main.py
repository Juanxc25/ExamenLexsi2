from flask import Flask, request, render_template 
import analizador_lexico as lex
import analizador_Sintactico as yacc

app = Flask(__name__)

@app.route('/')
def hello_world():
    lex.reset_lexer()  # Reiniciar el contador de líneas
    return render_template('index.html')


@app.route('/api/v1/lexer', methods=['POST'])
def lexer():
    
    data = request.get_json()
    code = data.get('code')

    lex.lexer.input(code)

    tokens = []
    while True:
        tok = lex.lexer.token()
        if not tok:
            break
        tokens.append({
            'type': tok.type,
            'value': tok.value,
            'line': tok.lineno,
            'lexpos': tok.lexpos
        })


    debug_messages = []
    resultado_sintactico = yacc.parse_code(code, debug=debug_messages)

    print("Code:", code)
    print("Tokens:", tokens)
    print("Resultado Sintáctico:", resultado_sintactico)
    print("Debug Messages:", debug_messages)

    if resultado_sintactico["status"] == "success":
        return render_template('result.html', code=code, tokens=tokens, resultado_sintactico=resultado_sintactico)
    else:
        error_message = resultado_sintactico["message"]
        return render_template('error.html', code=code, tokens=tokens, resultado_sintactico=resultado_sintactico, error_message=error_message, debug_messages=debug_messages)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
