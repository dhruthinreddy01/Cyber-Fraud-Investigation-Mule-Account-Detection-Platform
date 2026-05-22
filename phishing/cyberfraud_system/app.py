from flask import Flask, render_template, request, jsonify
from cyberfraud_system.backend.case_management import create_case_folder
from cyberfraud_system.backend.forensic_evidence import collect_evidence, save_evidence
from cyberfraud_system.backend.soc_dashboard import get_dashboard_data
from cyberfraud_system.backend.legal_mapper import map_it_act
from cyberfraud_system.backend.pdf_report import generate_pdf_report
import os
import hashlib
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'cyberfraud_system/uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan_url', methods=['POST'])
def scan_url():
    url = request.form.get('url')
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    # Example: Phishing detection logic
    detection_type = "phishing"  # Placeholder for ML model
    case_id, case_path = create_case_folder()
    sha256_hash = collect_evidence(case_path, "URL", {"url": url})
    it_act_sections = map_it_act(detection_type)

    return jsonify({"case_id": case_id, "it_act_sections": it_act_sections})

@app.route('/dashboard')
def dashboard():
    data = get_dashboard_data()
    return render_template('dashboard.html', data=data)

@app.route('/generate_report', methods=['POST'])
def generate_report():
    case_id = request.form.get('case_id')
    case_path = f"cyberfraud_system/evidence/cases/{case_id}"
    evidence_summary = {"type": "URL", "sha256": "examplehash"}  # Placeholder
    it_act_sections = map_it_act("phishing")
    report_path = generate_pdf_report(case_id, case_path, evidence_summary, it_act_sections)

    return jsonify({"report_path": report_path})

@app.route('/analyze-apk', methods=['POST'])
def analyze_apk():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected for uploading"}), 400

    # Save the file temporarily
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    file.save(file_path)

    try:
        # Generate case ID
        case_id = str(uuid.uuid4())

        # Calculate file metadata
        file_size = os.path.getsize(file_path)
        sha256_hash = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)

        metadata = {
            "file_name": file.filename,
            "file_size": file_size,
            "sha256_hash": sha256_hash.hexdigest(),
            "analysis_status": "success"
        }

        # Save evidence and log to database
        save_evidence(case_id, file_path, metadata)
        log_evidence(case_id, file.filename, sha256_hash.hexdigest())

        return jsonify(metadata), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)