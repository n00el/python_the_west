from the_west_inner.work import Work, work_task


class RecordingHandler:
    def __init__(self):
        self.payload = None

    def post(self, module, action, payload, use_h):
        self.payload = payload
        return {"success": True}


def test_work_task_uses_scalar_values_and_successive_queue_positions():
    handler = RecordingHandler()

    response = work_task(handler, 2, Work(7, 10, 11, 15), number_of_tasks=2)

    assert response == {"success": True}
    assert handler.payload == {
        "tasks[2][jobId]": "7",
        "tasks[2][x]": "10",
        "tasks[2][y]": "11",
        "tasks[2][duration]": "15",
        "tasks[2][taskType]": "job",
        "tasks[3][jobId]": "7",
        "tasks[3][x]": "10",
        "tasks[3][y]": "11",
        "tasks[3][duration]": "15",
        "tasks[3][taskType]": "job",
    }
