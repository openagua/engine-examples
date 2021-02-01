from os import environ
from openagua import create_app
from weap import run_weap_model

from dotenv import load_dotenv

load_dotenv()

model_key = environ.get('OA_SECRET_KEY')
app = create_app(model_key)


@app.task(name='model.run')
def run(**kwargs):
    scenario_id_combinations = kwargs.pop('scenario_ids', [])
    network = {'name': 'Weaping River Basin'}
    for scen_ids in scenario_id_combinations:
        run_scenario.apply_async(args=(scen_ids, network,), kwargs=kwargs)


@app.task
def run_scenario(scen_ids, network, **kwargs):
    run_weap_model(scen_ids, network, **kwargs)


if __name__ == '__main__':
    # IMPORTANT: Celery does not support Windows. -P solo seems to work.
    app.start(['-A', 'tasks', 'worker', '-l', 'INFO', '-P' 'solo'])
