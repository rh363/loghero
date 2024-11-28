from django.http import JsonResponse

from loghero.manager import add_log, get_client_ip, Severity, Status

def index(request):
    ip = get_client_ip(request)
    log = add_log(
        actor="alex",
        action="login",
        severity=Severity.INFO,
        status=Status.SUCCESS,
        target_type="mock",
        target="user",
        ip_address=ip,
    )
    return JsonResponse(status=200, data=dict(message=log.__str__()))