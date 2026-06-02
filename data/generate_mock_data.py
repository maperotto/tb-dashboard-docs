import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_mock_data(n_records=1000):
    estados = ['SP', 'RJ', 'MG', 'BA', 'PR', 'RS', 'PE', 'CE', 'PA', 'SC']
    status_opcoes = ['Em Tratamento', 'Cura', 'Abandono', 'Óbito']
    
    data_inicio = datetime(2023, 1, 1)
    
    records = []
    for i in range(n_records):
        # Gerar data aleatória nos últimos 18 meses
        dias_atras = random.randint(0, 500)
        data_notificacao = data_inicio + timedelta(days=dias_atras)
        
        estado = random.choice(estados)
        # Simular cidades fictícias baseadas no estado
        cidade = f"Cidade_{estado}_{random.randint(1, 5)}"
        idade = random.randint(1, 90)
        status = random.choices(status_opcoes, weights=[0.6, 0.25, 0.1, 0.05])[0]
        
        records.append({
            'id_paciente': i + 1, # ID incremental apenas para controle, sem dados pessoais
            'data_notificacao': data_notificacao.strftime('%Y-%m-%d'),
            'estado': estado,
            'cidade': cidade,
            'idade': idade,
            'status_treatmento': status
        })
    
    df = pd.DataFrame(records)
    df.to_csv('/home/ubuntu/tuberculose_dashboard/data/tuberculose_data.csv', index=False)
    print(f"Mock data generated with {n_records} records.")

if __name__ == "__main__":
    generate_mock_data()
