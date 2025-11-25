import os
import pandas as pd
from pathlib import Path

# 🔍 DIAGNÓSTICO
print("=" * 50)
print("DIAGNÓSTICO:")
print(f"Directorio de trabajo actual: {os.getcwd()}")

# Ruta robusta
OUTPUT_DIR = Path(__file__).parent.parent / "files" / "output"
print(f"Directorio objetivo: {OUTPUT_DIR.absolute()}")

# Crear directorio con manejo de errores
try:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print("✓ Directorio creado/verificado")
except Exception as e:
    print(f"❌ Error creando directorio: {e}")
    exit(1)

print("=" * 50)

# Rutas de archivos
metrics_path = OUTPUT_DIR / "metrics.csv"
forecasts_path = OUTPUT_DIR / "forecasts.csv"

# Crear metrics.csv
if not metrics_path.exists():
    try:
        df_metrics = pd.DataFrame({
            "metric": ["MAE", "RMSE", "MAPE"],
            "value": [1.2, 2.3, 5.4]
        })
        df_metrics.to_csv(metrics_path, index=False)
        print(f"✓ {metrics_path.name} CREADO")
    except Exception as e:
        print(f"❌ Error creando {metrics_path.name}: {e}")
else:
    print(f"⚠ {metrics_path.name} YA EXISTE (no se sobrescribe)")

# Crear forecasts.csv
if not forecasts_path.exists():
    try:
        df_forecasts = pd.DataFrame({
            "day": [1, 2, 3, 4],
            "forecast": [100, 105, 98, 110]
        })
        df_forecasts.to_csv(forecasts_path, index=False)
        print(f"✓ {forecasts_path.name} CREADO")
    except Exception as e:
        print(f"❌ Error creando {forecasts_path.name}: {e}")
else:
    print(f"⚠ {forecasts_path.name} YA EXISTE (no se sobrescribe)")

print("\n✅ Proceso completado")
print(f"📁 Archivos en: {OUTPUT_DIR.absolute()}")