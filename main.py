from flask import Flask, request, jsonify
import chess
import chess.engine

app = Flask(__name__)
engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")

@app.route('/get_best_move', methods=['POST'])
def get_best_move():
    data = request.json
    board = chess.Board(data['fen'])
    result = engine.play(board, chess.engine.Limit(time=0.1))
    return jsonify({"best_move": result.move.uci()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
