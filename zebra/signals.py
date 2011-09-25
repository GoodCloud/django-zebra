import django.dispatch


WEBHOOK_ARGS = ["customer", "full_json"]

zebra_webhook_recurring_payment_failed = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
zebra_webhook_invoice_ready = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
zebra_webhook_recurring_payment_succeeded = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
zebra_webhook_subscription_trial_ending = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
zebra_webhook_subscription_final_payment_attempt_failed = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
zebra_webhook_subscription_ping_sent = django.dispatch.Signal(providing_args=[])