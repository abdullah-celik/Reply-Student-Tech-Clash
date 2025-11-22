from agents import SentinelAgent, HistorianAgent, TriageAgent
from mock_data import events_stream, patient_emr
import time

def run_calm_system():
    # Initialize the Digital Team
    sentinel = SentinelAgent()
    historian = HistorianAgent()
    triage = TriageAgent()

    print("🏥 --- C.A.L.M. SYSTEM ONLINE ---\n")

    for event in events_stream:
        print("-" * 50)
        print(f"Incoming Data: {event['metric']} = {event['value']}")
        
        # STEP 1: Sentinel watches the stream
        sentinel_result = sentinel.analyze(event)
        
        if sentinel_result['status'] == "NORMAL":
            print(f"✅ System: {sentinel_result['reason']}")
            continue # Skip to next event, no need to bother other agents
            
        print(f"⚠️  SENTINEL FLAG: {sentinel_result['reason']}")

        # STEP 2: Historian checks context (only if Sentinel flagged it)
        # We fetch the specific patient's EMR based on the ID in the event
        patient_data = patient_emr.get(event['patient_id'])
        historian_result = historian.check_context(event, patient_data, sentinel_result)
        
        print(f"📝 HISTORIAN OPINION: {historian_result['verdict']} - {historian_result['explanation']}")

        # STEP 3: Triage Officer makes the final call
        final_decision = triage.decide(sentinel_result, historian_result)

        # FINAL OUTPUT
        print(f"\n🚀 FINAL DECISION: {final_decision['final_action']}")
        print(f"📟 DASHBOARD MESSAGE: \"{final_decision['message_to_doctor']}\"")
        
        time.sleep(2) # Pause for dramatic effect

if __name__ == "__main__":
    run_calm_system()