# Simulates the incoming stream from ICU devices
events_stream = [
    # Event 1: Normal
    {"id": 101, "type": "VITALS", "metric": "Heart Rate", "value": 72, "patient_id": "P-808"},
    
    # Event 2: CRITICAL (Actual Cardiac Arrest simulation)
    {"id": 102, "type": "VITALS", "metric": "Heart Rate", "value": 0, "patient_id": "P-808"},
    
    # Event 3: TRICKY (The "Bradycardia" Negotiation case)
    {"id": 103, "type": "VITALS", "metric": "Heart Rate", "value": 42, "patient_id": "P-808"},
]

# Simulates the Electronic Medical Record (EMR) database
patient_emr = {
    "P-808": {
        "name": "Alessandro Rossi",
        "age": 28,
        "condition": "Post-Op Knee Surgery",
        "medications": ["Atenolol (Beta-Blocker) taken at 08:00 AM"],
        "history": "Competitive swimmer, resting heart rate typically 40-45 bpm.",
        "notes": "Patient is currently sleeping."
    }
}