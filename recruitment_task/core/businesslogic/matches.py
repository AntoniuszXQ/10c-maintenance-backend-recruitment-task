from core.models import Project , Investor
from .errors import CannotInvestIntoProjectException


def project_matches( queryset, investor) :
    matching_investor_ids = queryset.filter(
    funded=False,
    delivery_date__lte=investor.project_delivery_deadline,
    amount__lte=investor.individual_amount,
    ).filter(
    amount__lte=investor.remaining_amount
    )

    list_of_investor_ids = list(matching_investor_ids)
    return list_of_investor_ids


def investor_matches(queryset, project):
    matching_project_ids = queryset.filter(
        remaining_amount__gte=project.amount,
        individual_amount__gte=project.amount,
        project_delivery_deadline__gte=project.delivery_date,
    )
    list_of_project_ids = list(matching_project_ids)
    return list_of_project_ids








