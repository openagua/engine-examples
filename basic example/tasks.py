from openagua import create_app
from demo_model import run_demo_model

from dotenv import load_dotenv

load_dotenv()

app = create_app()


@app.task(name='model.run')
def run(**kwargs):
    scenario_id_combinations = kwargs.pop('scenario_ids', [])

    # Here, common, high-level work can be done
    network = {'name', 'Demo Model'}

    for scen_ids in scenario_id_combinations:
        # This is how to run a single scenario model asynchronously
        run_scenario.apply_async(args=(scen_ids, network,), kwargs=kwargs)


@app.task
def run_scenario(scen_ids, **kwargs):
    run_demo_model(scen_ids, **kwargs)


if __name__ == '__main__':
    # IMPORTANT: Celery does not support Windows. -P solo seems to work.
    app.start(['-A', 'tasks', 'worker', '-l', 'INFO', '-P' 'solo'])
