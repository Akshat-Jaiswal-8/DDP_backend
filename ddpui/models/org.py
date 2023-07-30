from django.db import models
from ninja import Schema


class OrgDbt(models.Model):
    """Docstring"""

    gitrepo_url = models.CharField(max_length=100)
    gitrepo_access_token_secret = models.CharField(
        max_length=100, null=True
    )  # skipcq: PTC-W0901, PTC-W0906

    project_dir = models.CharField(max_length=200)
    dbt_version = models.CharField(max_length=10)

    target_type = models.CharField(max_length=10)
    default_schema = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"OrgDbt[{self.gitrepo_url}|{self.target_type}|{self.default_schema}]"


class Org(models.Model):
    """Docstring"""

    name = models.CharField(max_length=50)
    slug = models.CharField(
        max_length=20, null=True
    )  # skipcq: PTC-W0901 skipcq: PTC-W0906
    airbyte_workspace_id = models.CharField(
        max_length=36, null=True
    )  # skipcq: PTC-W0901, PTC-W0906
    dbt = models.ForeignKey(
        OrgDbt, on_delete=models.SET_NULL, null=True
    )  # skipcq: PTC-W0901, PTC-W0906

    def __str__(self) -> str:
        return f"Org[{self.slug}|{self.name}|{self.airbyte_workspace_id}]"


class OrgPrefectBlock(models.Model):
    """Docstring"""

    org = models.ForeignKey(Org, on_delete=models.CASCADE)
    block_type = models.CharField(max_length=25)  # all dbt blocks have the same type!
    block_id = models.CharField(max_length=36, unique=True)
    block_name = models.CharField(
        max_length=100, unique=True
    )  # use blockname to distinguish between different dbt commands
    display_name = models.CharField(
        max_length=100, null=True
    )  # skipcq: PTC-W0901, PTC-W0906
    command = models.CharField(
        max_length=100, null=True
    )  # skipcq: PTC-W0901, PTC-W0906
    dbt_target_schema = models.CharField(
        max_length=50, null=True
    )  # skipcq: PTC-W0901, PTC-W0906
    seq = models.SmallIntegerField(null=True)  # skipcq: PTC-W0901, PTC-W0906

    def __str__(self) -> str:
        return f"OrgPrefectBlock[{self.org.name}|{self.block_type}|{self.block_name}]"


class OrgDataFlow(models.Model):
    """This contains the deployment id of an organization to schedule flows/pipelines"""

    org = models.ForeignKey(Org, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    deployment_name = models.CharField(
        max_length=100, null=True
    )  # skipcq: PTC-W0901, PTC-W0906
    deployment_id = models.CharField(
        max_length=36, unique=True, null=True
    )  # skipcq: PTC-W0901, PTC-W0906
    cron = models.CharField(max_length=36, null=True)  # skipcq: PTC-W0901, PTC-W0906
    # and if deployment is manual airbyte-connection-sync,then we store the conn_id
    connection_id = models.CharField(
        max_length=36, unique=True, null=True
    )  # skipcq: PTC-W0901, PTC-W0906

    def __str__(self) -> str:
        return f"OrgDataFlow[{self.name}|{self.deployment_name}|{self.deployment_id}|{self.cron}|{self.connection_id}]"


class OrgSchema(Schema):
    """Docstring"""

    name: str
    slug: str = None
    airbyte_workspace_id: str = None


class OrgWarehouse(models.Model):
    """A data warehouse for an org. Typically we expect exactly one"""

    wtype = models.CharField(max_length=25)  # postgres, bigquery
    credentials = models.CharField(max_length=200)
    org = models.ForeignKey(Org, on_delete=models.CASCADE)
    airbyte_destination_id = models.TextField(
        max_length=36, null=True
    )  # skipcq: PTC-W0901, PTC-W0906
    airbyte_norm_op_id = models.TextField(
        max_length=36, null=True
    )  # skipcq: PTC-W0901, PTC-W0906

    def __str__(self) -> str:
        return (
            f"OrgWarehouse[{self.org.slug}|{self.wtype}|{self.airbyte_destination_id}]"
        )


class OrgWarehouseSchema(Schema):
    """payload to register an organization's data warehouse"""

    wtype: str
    destinationDefId: str
    airbyteConfig: dict
