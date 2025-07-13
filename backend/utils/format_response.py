import pandas as pd

def format_result(result):
    if isinstance(result, pd.DataFrame):
        if result.empty:
            return {
                "type": "text",
                "data": "No data found."
            }

        if result.shape[1] == 2 and pd.api.types.is_numeric_dtype(result.iloc[:, 1]):
            return {
                "type": "graph",
                "data": result.to_dict(orient="records")
            }

        return {
            "type": "table",
            "data": result.to_dict(orient="records")
        }

    elif isinstance(result, list) and len(result) > 0 and isinstance(result[0], dict):
        return {
            "type": "table",
            "data": result
        }

    else:
        return {
            "type": "text",
            "data": str(result)
        }
