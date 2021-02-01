from time import sleep
import datetime as dt
from loguru import logger
from openagua import OpenAgua

import win32com.client as win32


def run_weap_model(scenario_ids, network, **kwargs):
    """
    :param scen_ids: The scenario ID combinations for this run.
    :param kwargs: As-yet-undefined kwargs
    :return:
    """

    WEAP = win32.gencache.EnsureDispatch('WEAP.WEAPApplication')
    while not WEAP.ProgramStarted:
        sleep(1)

    WEAP.ActiveArea = network['name']
    while not WEAP.ProgramStarted:
        sleep(1)

    run_name = kwargs.get('run_name')

    total_steps = (WEAP.EndYear - WEAP.BaseYear) * WEAP.Timesteps.Count

    oa = OpenAgua(
        guid=kwargs.get('guid'),
        name=run_name,
        network_id=kwargs.get('network_id'),
        run_key=None,  # basic run
        scenario_ids=scenario_ids,
        total_steps=total_steps
    )

    # tell OA that the model is started
    oa.start()

    S = WEAP.Scenario("Reference")

    WEAP.InitializeInteractiveCalculations()
    S.InitializeInteractiveCalculations()

    for i in range(total_steps):

        # Check if the user has paused or stopped the run
        if oa.paused:
            pause_start_time = dt.datetime.now()
            while oa.paused and (dt.datetime.now() - pause_start_time).seconds < 86400:
                sleep(0.1)

        if oa.stopped:  # this should be after pause is checked, to stop during a pause
            oa.stop()  # This will report back to OA that the model has stopped
            break

        # datetime = start + dt.timedelta(days=i)
        # logger.info(datetime)
        # oa.step(datetime=datetime)
        # sleep(1)
        S.CalculateNextTimeStep()
        timestep = S.StepTS

    oa.finish()
