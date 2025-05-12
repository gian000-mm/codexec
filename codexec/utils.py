import os
import frappe

def save_script_to_file(script_name, script_code):
    # Ottieni il path della root dell'app "codexec"
    app_root = frappe.get_app_path("codexec")  # es: /frappe-bench/apps/codexec/codexec

    # Normalizza il nome del file (evita caratteri problematici)
    safe_name = "".join(c if c.isalnum() else "_" for c in script_name)
    file_name = f"{safe_name}.py"
    file_path = os.path.join(app_root, file_name)

    # Scrive il codice Python nel file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(script_code)

    frappe.logger().info(f"Script salvato in: {file_path}")
    return file_path