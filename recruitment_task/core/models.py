from django.db import models


class Investor(models.Model):
    name = models.CharField(
        max_length=255, help_text="Investor name"
    )
    remaining_amount = models.DecimalField(
        max_digits=11, decimal_places=2, help_text="Remaining investor's amount.", default=0
    )
    total_amount = models.DecimalField(
        max_digits=11, decimal_places=2, help_text="Total investor's amount."
    )
    individual_amount = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        help_text="Individual amount per project",
    )
    project_delivery_deadline = models.DateField(
        help_text="Deadline that funded projects must deliver by"
    )

    def __str__(self):
        return f"Investor: {self.name}"


class Project(models.Model):
    name = models.CharField(
        "Project's name",
        max_length=255,
        help_text="Name of the project",
    )
    description = models.TextField(
        max_length=700,
        help_text="What’s the goal of the project?"
    )
    amount = models.DecimalField(
        help_text="Total project funding required",
        decimal_places=2,
        max_digits=7,
    )
    delivery_date = models.DateField(
        help_text="Estimated project delivery date."
    )
    funded_by = models.ForeignKey(Investor, null=True, blank=True, editable=False,
                                  related_name="funded_projects", on_delete=models.SET_NULL)
    # This is a backup field in case investor gets deleted and funded_by is NULL
    funded = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return f"Project: {self.name}"
