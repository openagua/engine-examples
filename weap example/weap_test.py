from weap import run_weap_model


from dotenv import load_dotenv

load_dotenv()

network = {'name': 'Weaping River Basin'}
run_weap_model(scenario_ids=[], network=network)
