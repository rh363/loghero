from django.http import JsonResponse
from django.utils import timezone

from loghero.manager import add_log, get_client_ip, Severity, Status
from loghero.models import Log


def index(request):
    ip = get_client_ip(request)
    log = add_log(
        actor="alex",
        actor_label="Ciccio",
        action="login",
        severity=Severity.INFO,
        status=Status.SUCCESS,
        target_type="mock",
        target="user",
        ip_address=ip,
        extra_data={"test": "is working", "date": timezone.now()},
    )
    return JsonResponse(status=200, data=dict(message=log.__str__()))


def list_logs(request):
    logs = Log.objects.all()
    print(logs.serialize())
    return JsonResponse(status=200, data=list(logs.serialize()), safe=False)
