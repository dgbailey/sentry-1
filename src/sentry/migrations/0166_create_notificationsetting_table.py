# Generated by Django 1.11.29 on 2021-02-26 22:11

from django.db import migrations
import sentry.db.models.fields.bounded
import sentry.models.integration
import sentry.models.notificationsetting


class Migration(migrations.Migration):
    # This flag is used to mark that a migration shouldn't be automatically run in
    # production. We set this to True for operations that we think are risky and want
    # someone from ops to run manually and monitor.
    # General advice is that if in doubt, mark your migration as `is_dangerous`.
    # Some things you should always mark as dangerous:
    # - Large data migrations. Typically we want these to be run manually by ops so that
    #   they can be monitored. Since data migrations will now hold a transaction open
    #   this is even more important.
    # - Adding columns to highly active tables, even ones that are NULL.
    is_dangerous = False

    # This flag is used to decide whether to run this migration in a transaction or not.
    # By default we prefer to run in a transaction, but for migrations where you want
    # to `CREATE INDEX CONCURRENTLY` this needs to be set to False. Typically you'll
    # want to create an index concurrently when adding one to an existing table.
    # You'll also usually want to set this to `False` if you're writing a data
    # migration, since we don't want the entire migration to run in one long-running
    # transaction.
    atomic = True

    dependencies = [
        ("sentry", "0165_metric_alerts_fix_group_ids"),
    ]

    operations = [
        migrations.CreateModel(
            name="NotificationSetting",
            fields=[
                (
                    "id",
                    sentry.db.models.fields.bounded.BoundedBigAutoField(
                        primary_key=True, serialize=False
                    ),
                ),
                (
                    "scope_type",
                    sentry.db.models.fields.bounded.BoundedPositiveIntegerField(
                        choices=[
                            (sentry.models.notificationsetting.NotificationScopeType(0), "user"),
                            (
                                sentry.models.notificationsetting.NotificationScopeType(10),
                                "organization",
                            ),
                            (
                                sentry.models.notificationsetting.NotificationScopeType(20),
                                "project",
                            ),
                        ]
                    ),
                ),
                ("scope_identifier", sentry.db.models.fields.bounded.BoundedBigIntegerField()),
                (
                    "target_type",
                    sentry.db.models.fields.bounded.BoundedPositiveIntegerField(
                        choices=[
                            (sentry.models.notificationsetting.NotificationTargetType(0), "user"),
                            (sentry.models.notificationsetting.NotificationTargetType(10), "team"),
                        ]
                    ),
                ),
                ("target_identifier", sentry.db.models.fields.bounded.BoundedBigIntegerField()),
                (
                    "provider",
                    sentry.db.models.fields.bounded.BoundedPositiveIntegerField(
                        choices=[
                            (sentry.models.integration.ExternalProviders(100), "email"),
                            (sentry.models.integration.ExternalProviders(110), "slack"),
                        ]
                    ),
                ),
                (
                    "type",
                    sentry.db.models.fields.bounded.BoundedPositiveIntegerField(
                        choices=[
                            (
                                sentry.models.notificationsetting.NotificationSettingTypes(0),
                                "default",
                            ),
                            (
                                sentry.models.notificationsetting.NotificationSettingTypes(10),
                                "deploy",
                            ),
                            (
                                sentry.models.notificationsetting.NotificationSettingTypes(20),
                                "issue",
                            ),
                            (
                                sentry.models.notificationsetting.NotificationSettingTypes(30),
                                "workflow",
                            ),
                        ]
                    ),
                ),
                (
                    "value",
                    sentry.db.models.fields.bounded.BoundedPositiveIntegerField(
                        choices=[
                            (
                                sentry.models.notificationsetting.NotificationSettingOptionValues(
                                    0
                                ),
                                "default",
                            ),
                            (
                                sentry.models.notificationsetting.NotificationSettingOptionValues(
                                    10
                                ),
                                "off",
                            ),
                            (
                                sentry.models.notificationsetting.NotificationSettingOptionValues(
                                    20
                                ),
                                "on",
                            ),
                            (
                                sentry.models.notificationsetting.NotificationSettingOptionValues(
                                    30
                                ),
                                "subscribe_only",
                            ),
                            (
                                sentry.models.notificationsetting.NotificationSettingOptionValues(
                                    40
                                ),
                                "committed_only",
                            ),
                        ]
                    ),
                ),
            ],
            options={
                "db_table": "sentry_notificationsetting",
            },
        ),
        migrations.AlterUniqueTogether(
            name="notificationsetting",
            unique_together={
                (
                    "scope_type",
                    "scope_identifier",
                    "target_type",
                    "target_identifier",
                    "provider",
                    "type",
                )
            },
        ),
        migrations.AlterIndexTogether(
            name="notificationsetting",
            index_together={("target_type", "target_identifier")},
        ),
    ]
