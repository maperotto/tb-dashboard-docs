# Dashboard de Monitoramento de Tuberculose

Este projeto acadêmico tem como objetivo demonstrar um dashboard simples para monitoramento de casos de Tuberculose, utilizando Python com Flask, Pandas, NumPy e Plotly. Os dados são simulados para fins de demonstração e não contêm informações reais de pacientes.

## Stack Tecnológico

*   **Python 3.x**
*   **Flask**: Framework web para o servidor e rotas da API.
*   **Pandas**: Para manipulação e análise de dados.
*   **NumPy**: Para operações numéricas auxiliares.
*   **Plotly**: Para a geração de gráficos interativos.

## Estrutura do Projeto

```
tuberculose_dashboard/
├── app.py
├── data_analysis.py
├── requirements.txt
├── .gitignore
├── README.md
├── data/
│   ├── generate_mock_data.py
│   └── tuberculose_data.csv (gerado)
├── templates/
│   └── index.html
└── static/
    ├── css/
    └── js/
```

## Funcionalidades

*   **Mock de Dados**: Geração de dados fictícios de casos de Tuberculose.
*   **Processamento de Dados**: Carga, limpeza e agrupamento de dados por mês e estado.
*   **Visualização**: Gráfico de linha interativo mostrando a tendência de casos.
*   **Interface Web**: Dashboard simples com filtros por estado.
*   **Alertas**: Notificação visual caso o número de casos em um mês ultrapasse um limite crítico.

## Como Rodar o Projeto Localmente

Siga os passos abaixo para configurar e executar o projeto em sua máquina local:

### 1. Clone o Repositório (se aplicável)

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd tuberculose_dashboard
```

### 2. Crie e Ative um Ambiente Virtual (Recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # No Linux/macOS
# venv\Scripts\activate    # No Windows
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Gere os Dados de Mock

Execute o script para criar o arquivo `tuberculose_data.csv`:

```bash
python3 data/generate_mock_data.py
```

### 5. Execute a Aplicação Flask

```bash
export FLASK_APP=app.py
export FLASK_ENV=development # Para ativar o modo debug
flask run
```

Ou, alternativamente, execute diretamente o `app.py`:

```bash
python3 app.py
```

### 6. Acesse o Dashboard

Abra seu navegador e acesse: `http://127.0.0.1:5000/`

## Considerações Éticas

Os dados utilizados neste projeto são **totalmente simulados** e não correspondem a casos reais de pacientes. A estrutura dos dados foi pensada para ser realista, mas sem qualquer informação que possa levar à identificação de indivíduos, respeitando a privacidade e as normas éticas em saúde. Este projeto serve apenas para fins educacionais e de demonstração de tecnologias.
