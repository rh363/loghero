from loghero.models import *
from django.contrib.auth.models import User
from datetime import datetime
from hostip_client.client import Client
# class Manager:
#     def __init__(self):
#         pass

def add_log(actor: str|User,
            action: str,
            severity: Severity,
            status: Status,
            target: str,
            target_type: str,
            ip_address: str = None,
            user_agent: str = None,
            url: str = None,
            location: str = None,
            result: str = None,
            result_type: str = None,
            description: str = None,
            extra_data: dict = None):
    """
    This function creates a log entry with the specified information about an action.
    The function accepts various parameters including actor, action, severity,
    and more to document the details of a particular event or action. If no location
    is provided but an IP address is available, it attempts to determine the location
    from the IP address. Finally, a log entry is created with the collected data.

    :param actor: The individual or entity performing the action.
    :type actor: str or User
    :param action: The action or event being logged.
    :type action: str
    :param severity: The severity level of the action.
    :type severity: Severity
    :param status: The status of the action or event.
    :type status: Status
    :param target: The target of the action or event.
    :type target: str
    :param target_type: The type or category of the target.
    :type target_type: str
    :param ip_address: The IP address from which the action is initiated.
    :type ip_address: str, optional
    :param user_agent: The user agent string from the client's request.
    :type user_agent: str, optional
    :param url: The URL associated with the action or event.
    :type url: str, optional
    :param location: The physical location related to the IP address.
    :type location: str, optional
    :param result: The outcome of the action or event.
    :type result: str, optional
    :param result_type: The type or nature of the result.
    :type result_type: str, optional
    :param description: Additional description or context for the action.
    :type description: str, optional
    :param extra_data: Any extra data related to the action, stored as a dictionary.
    :type extra_data: dict, optional
    :return: The created log entry object.
    :rtype: Log
    """
    if location is None and ip_address is not None:
        try:
            c = Client(ip_address)
            location = f"{c.country_name} ({c.country_code}), {c.city}"
        except Exception:
            pass
    return Log.objects.create(
        actor=actor,
        action=action,
        severity=severity,
        status=status,
        target=target,
        target_type=target_type,
        ip_address=ip_address,
        user_agent=user_agent,
        url=url,
        location=location,
        result=result,
        result_type=result_type,
        description=description,
        extra_data=extra_data,
    )

def get_client_ip(request):
    """
    Retrieves the client's IP address from a Django request object. It first checks if
    the 'HTTP_X_FORWARDED_FOR' header is present in the request metadata, indicating that
    the request was forwarded by a proxy or load balancer. If it is present, the first
    IP address in the comma-separated string is returned as the client's IP address.
    Otherwise, it returns the IP address from the 'REMOTE_ADDR' header.

    :param request: Django HttpRequest object used to retrieve the client's IP
                    address from headers.
    :return: A string representing the client's IP address.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip