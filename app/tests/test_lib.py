import pd_app
import asyncio, pytest
from peptideqspr.evaluation.evaluate_peptide import Model

@pytest.yield_fixture(autouse=True)
def start_aioloop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield
    loop.stop()
    pending = asyncio.Task.all_tasks()
    assert len(pending) == 0, 'Remaining coroutines on stack: {}'.format(pending)

def test_model_init():
    m = Model()

'''def test_model_train_start_stop():
    m = pd_app.Model()
    assert m.train_status() == 0
    m.train_start()
    #need to await the stop if we want to get status
    loop = asyncio.get_event_loop()
    async def anon():
        await m.train_stop()
    loop.run_until_complete(anon())
    assert m.train_status() > 0
'''
def test_model_predict():
    m = Model()
    #m.reset_model()
    #m.train_start()
    #need to await the stop if we want to get status
    #loop = asyncio.get_event_loop()
    #async def anon():
    #    #give some time to train
    #    await asyncio.sleep(1)
    #    await m.train_stop()
    #loop.run_until_complete(anon())
    prediction = m.predict('CEK')
    assert prediction

def test_model_predict_basic():
    m = Model()
    #m.reset_model()
    #m.train_start()
    ##need to await the stop if we want to get status
    #loop = asyncio.get_event_loop()
    #async def anon():
    #    #give some time to train
    #    await asyncio.sleep(10)
    #    await m.train_stop()
    #loop.run_until_complete(anon())
    prediction = m.predict('KEP')
    assert prediction
