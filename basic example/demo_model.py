from time import sleep
import datetime as dt
from loguru import logger
from openagua_engine import OpenAguaEngine


def run_demo_model(network_id, scenario_ids, **kwargs):
    """
    This is the main model run. The example is not built out at all. It just shows a skeleton, with usage of
    openagua-engine (OpenAguaEngine) and it's reporting facilities (start, step, stop, etc.)
    :param network_id: The network ID (this could also be changed to pass the entire network, to save time).
    :param scenario_ids: The scenario ID combinations for this run.
    :param kwargs: As-yet-undefined kwargs
    :return:
    """

    total_steps = 100

    guid = kwargs.get('guid')

    run_name = kwargs.get('run_name')
    debug = kwargs.get('debug')

    oa = OpenAguaEngine(
        name=run_name,
        guid=guid,
        request_host=kwargs.get('request_host'),
        network_id=network_id,
        run_key=None,  # basic run
        scenario_ids=scenario_ids,
    )

    # Tell OA that the model is started (this reports to the OpenAgua API and any logged in web client)
    oa.start()

    # Get the network data (note the ['network'] at the end; this will be fixed in the future).
    # network = oa.Client.get_network(network_id)['network']

    # do something with the network here...
    # e.g.: my_model = create_my_model(network)
    start = dt.date(1950, 10, 1)
    end = dt.date(2000, 9, 30)
    total_steps = 100  # Get the total number of steps (this is a contrived example)
    oa.total_steps = total_steps  # This lets the engine report the correct percent complete

    for i in range(total_steps):

        # Check if the user has paused or stopped the run
        if oa.paused:
            pause_start_time = dt.datetime.now()
            while oa.paused and (dt.datetime.now() - pause_start_time).seconds < 86400:
                sleep(0.1)

        if oa.stopped:  # this should be after pause is checked, to stop during a pause
            oa.stop()  # Tell OA that the model is stopped
            break

        datetime = start + dt.timedelta(days=i)
        logger.info(datetime)

        # Do something very important and computationally expensive here.
        try:
            sleep(1)

            # This is a fake error for demo
            if i == 5:
                raise Exception("Oops! Something went wrong.")

            # This repots progress to the web client (i.e. app user)
            oa.step(datetime=datetime)
        except Exception as err:
            logger.info(err)
            oa.error(extra_info=err)
            break

    # Tell OA that the model is finished
    oa.finish()


if __name__ == '__main__':
    import dotenv

    dotenv.load_dotenv()

    network_id = 1156
    scenario_id = 2519
    kwargs = {
        'run_name': 'baseline',
    }

    run_demo_model(network_id, scenario_ids=[scenario_id], **kwargs)

    logger.info('Finished')
