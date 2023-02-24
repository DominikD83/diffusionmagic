from backend.stablediffusion.models.scheduler_types import SchedulerType, Scheduler
from backend.stablediffusion.scheduler_factory import SchedulerFactory


class SamplerMixin:
    def __init__(self):
        self.samplers = {}

    def find_sampler(
        self,
        scheduler_name: str,
        repo_id: str,
    ) -> Scheduler:
        scheduler_factory = SchedulerFactory()
        if self.samplers.get(scheduler_name) is None:
            self.samplers[scheduler_name] = scheduler_factory.get_scheduler(
                scheduler_name,
                repo_id,
            )
        print(self.samplers)
        return self.samplers[scheduler_name]