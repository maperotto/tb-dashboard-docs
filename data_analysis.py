import json
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.utils

class TuberculosisAnalyzer:
    def __init__(self, csv_path: Path):
        self.csv_path = Path(csv_path)
        self.df = pd.DataFrame()
        self.load_data()

    def load_data(self):
        try:
            df = pd.read_csv(self.csv_path)
        except Exception:
            self.df = pd.DataFrame()
            return self.df

        required = {"data_notificacao", "estado", "idade"}
        if not required.issubset(df.columns):
            self.df = pd.DataFrame()
            return self.df

        df["data_notificacao"] = pd.to_datetime(df["data_notificacao"], errors="coerce")
        df = df.dropna(subset=["data_notificacao", "estado", "idade"])
        df["mes_ano"] = df["data_notificacao"].dt.to_period("M")
        self.df = df
        return self.df

    def get_summary_stats(self, estado=None):
        df_filtered = self.df
        if estado and estado != "Todos":
            df_filtered = self.df[self.df["estado"] == estado]

        total_casos = len(df_filtered)
        media_idade = np.round(df_filtered["idade"].mean(), 1) if not df_filtered.empty else 0
        estados_unicos = (
            sorted(self.df["estado"].unique().tolist())
            if not self.df.empty
            else []
        )

        return {
            "total_casos": int(total_casos),
            "media_idade": float(media_idade),
            "estados_unicos": estados_unicos,
        }

    def get_trend_data(self, estado=None):
        if self.df.empty:
            return pd.DataFrame({"mes_ano": [], "casos": []})

        df_filtered = self.df
        if estado and estado != "Todos":
            df_filtered = self.df[self.df["estado"] == estado]

        if df_filtered.empty:
            return pd.DataFrame({"mes_ano": [], "casos": []})

        trend = df_filtered.groupby("mes_ano").size().reset_index(name="casos")
        trend["mes_ano"] = trend["mes_ano"].astype(str)
        return trend

    def check_alerts(self, trend_df, threshold=20):
        if trend_df.empty:
            return {"triggered": False}
        alerts = trend_df[trend_df['casos'] > threshold]
        if not alerts.empty:
            last_alert = alerts.iloc[-1]
            return {
                "triggered": True,
                "mes": last_alert["mes_ano"],
                "casos": int(last_alert["casos"]),
                "limite": int(threshold),
            }
        return {"triggered": False}

    def create_trend_chart(self, trend_df):
        fig = px.line(
            trend_df,
            x="mes_ano",
            y="casos",
            title="Tendência de Casos de Tuberculose ao Longo do Tempo",
            labels={"mes_ano": "Mês/Ano", "casos": "Número de Casos"},
            markers=True,
        )

        fig.update_layout(template="plotly_white")
        return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
