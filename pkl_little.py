import pickle

# Lista de archivos pkl originales (ajusta nombres)
archivos = ["best_dt_pack.pkl", "best_lg_pack.pkl", "best_svm_pack.pkl", "best_xgb_pack.pkl"]

for archivo in archivos:
    try:
        with open(archivo, "rb") as f:
            data = pickle.load(f)

        # Si el archivo contiene el modelo completo, debes haber guardado también estos arrays
        # (si no están, no podemos hacer nada)
        y_test = data.get("y_test")
        y_pred = data.get("y_pred")
        y_prob = data.get("y_prob", None)
        metrics = data.get("metrics", {})

        # Empaquetar versión liviana
        pack_liviano = {
            "y_test": y_test,
            "y_pred": y_pred,
            "y_prob": y_prob,
            "metrics": metrics
        }

        nuevo_nombre = archivo.replace(".pkl", "_lite.pkl")
        with open(nuevo_nombre, "wb") as f_out:
            pickle.dump(pack_liviano, f_out)

        print(f"✅ Reempacado: {archivo} → {nuevo_nombre}")

    except Exception as e:
        print(f"❌ Error con {archivo}: {e}")
