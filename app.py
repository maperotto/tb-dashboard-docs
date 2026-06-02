from flask import Flask, render_template, request, jsonify
from data_analysis import TuberculosisAnalyzer
from pathlib import Path

app = Flask(__name__)

DATA_PATH = Path(__file__).resolve().parent / "data" / "tuberculose_data.csv"
analyzer = TuberculosisAnalyzer(DATA_PATH)

CRITICAL_THRESHOLD = 15

@app.route('/')
def index():
    estado_filtro = request.args.get('estado', 'Todos')

    stats = analyzer.get_summary_stats(estado=estado_filtro)
    trend_data = analyzer.get_trend_data(estado=estado_filtro)

    graph_json = analyzer.create_trend_chart(trend_data)

    alert = analyzer.check_alerts(trend_data, threshold=CRITICAL_THRESHOLD)
    
    return render_template('index.html', 
                           stats=stats, 
                           graph_json=graph_json, 
                           alert=alert, 
                           current_estado=estado_filtro)

@app.route('/api/data')
def get_data():
    estado = request.args.get('estado', 'Todos')
    trend_data = analyzer.get_trend_data(estado=estado)
    return jsonify(trend_data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
