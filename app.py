from flask import Flask, request, render_template, jsonify
from src.chatbot import build_rag_chain

app = Flask(__name__)
rag = build_rag_chain()

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = None

    if request.method == 'POST':
        question = request.form.get('question')
        if question:
            try:
                response = rag.invoke({"input": question})
                answer = response['answer']
            except Exception as e:
                answer = f"Error: {str(e)}"

    return render_template('index.html', answer=answer)


# 👇 New JSON-based API endpoint for Postman
@app.route('/api/ask', methods=['POST'])
def api_ask():
    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({'error': 'Missing "question" in request'}), 400

    question = data['question']
    try:
        response = rag.invoke({"input": question})
        return jsonify({'answer': response['answer']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
