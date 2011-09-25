import unittest
from django.conf import settings
from django.test.client import Client
from zebra.signals import *
from django.utils import simplejson


from django.core.urlresolvers import reverse

class TestWebhooks(unittest.TestCase):

    def setUp(self):
        self.signal_kwargs = None

    def _signal_reciever(self, **kwargs):
        self.signal_kwargs = kwargs

    def _customized_signal_reciever(self, **kwargs):
        self.customer = kwargs["customer"]
        self.full_json = kwargs["full_json"]

    def test_recurring_payment_failed_signal_fired(self):
        zebra_webhook_recurring_payment_failed.connect(self._signal_reciever)

        self.assertEqual(self.signal_kwargs, None)

        # Pulled directly from the stripe docs
        test_post_data = {'json': simplejson.dumps({
          "customer":1083,
          "livemode": True,
          "event": "recurring_payment_failed",
          "attempt": 2,
          "invoice": {
            "attempted": True,
            "charge": "ch_sUmNHkMiag",
            "closed": False,
            "customer": "1083",
            "date": 1305525584,
            "id": "in_jN6A1g8N76",
            "object": "invoice",
            "paid": True,
            "period_end": 1305525584,
            "period_start": 1305525584,
            "subtotal": 2000,
            "total": 2000,
            "lines": {
              "subscriptions": [
                {
                  "period": {
                    "start": 1305525584,
                    "end": 1308203984
                  },
                  "plan": {
                    "object": "plan",
                    "name": "Premium plan",
                    "id": "premium",
                    "interval": "month",
                    "amount": 2000
                  },
                  "amount": 2000
                }
              ]
            }
          },
          "payment": {
            "time": 1297887533,
            "card": {
              "type": "Visa",
              "last4": "4242"
            },
            "success": False
          }
        }) }

        c = Client()
        response = c.post(reverse("zebra:webhooks"), test_post_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.signal_kwargs["full_json"]["customer"], 1083)



    def test_invoice_ready_signal_fired(self):
        zebra_webhook_invoice_ready.connect(self._signal_reciever)

        self.assertEqual(self.signal_kwargs, None)

        # Pulled directly from the stripe docs
        test_post_data = {'json': simplejson.dumps(
        {
          "customer":1083,
          "event":"invoice_ready",
          "invoice": {
            "total": 1500,
            "subtotal": 3000,
            "lines": {
              "invoiceitems": [
                {
                  "id": "ii_N17xcRJUtn",
                  "amount": 1000,
                  "date": 1303586118,
                  "currency": "usd",
                  "description": "One-time setup fee"
                }
              ],
              "subscriptions": [
                {
                  "amount": 2000,
                  "period": {
                    "start": 1304588585,
                    "end": 1307266985
                  },
                  "plan": {
                    "amount": 2000,
                    "interval": "month",
                    "object": "plan",
                    "id": "p_Mr2NgWECmJ",
                    "id": "premium"
                  }
                }
              ]
            },
            "object": "invoice",
            "discount": {
              "code": "50OFF",
              "percent_off": 50
            },
            "date": 1304588585,
            "period_start": 1304588585,
            "id": "in_jN6A1g8N76",
            "period_end": 1304588585
          }
        }
        ) }

        c = Client()
        response = c.post(reverse("zebra:webhooks"), test_post_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.signal_kwargs["full_json"]["invoice"]["date"], 1304588585)

      
 

    def test_recurring_payment_succeeded_signal_fired(self):
        zebra_webhook_recurring_payment_succeeded.connect(self._signal_reciever)

        self.assertEqual(self.signal_kwargs, None)

        # Pulled directly from the stripe docs
        test_post_data = {'json': simplejson.dumps(
            {
              "customer":"1083",
              "livemode": True,
              "event":"recurring_payment_succeeded",
              "invoice": {
                "total": 2000,
                "subtotal": 2000,
                "lines": {
                  "subscriptions": [
                  {
                    "amount": 2000,
                    "period": {
                      "start": 1304588585,
                      "end": 1307266985
                    },
                    "plan": {
                      "amount": 2000,
                      "interval": "month",
                      "object": "plan",
                      "id": "premium",
                      "name": "Premium plan"
                    }
                  }
                  ]
                },
                "object": "invoice",
                "date": 1304588585,
                "period_start": 1304588585,
                "id": "in_jN6A1g8N76",
                "period_end": 1304588585
              },
              "payment": {
                "time": 1297887533,
                "card":
                {
                  "type": "Visa",
                  "last4": "4242"
                },
                "success": True
              }
            }        
        ) }

        c = Client()
        response = c.post(reverse("zebra:webhooks"), test_post_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.signal_kwargs["full_json"]["payment"]["time"], 1297887533)

             

    def test_subscription_trial_ending_signal_fired(self):
        zebra_webhook_subscription_trial_ending.connect(self._signal_reciever)

        self.assertEqual(self.signal_kwargs, None)

        # Pulled directly from the stripe docs
        test_post_data = {'json': simplejson.dumps(
            {
              "customer":1083,
              "event":"subscription_trial_ending",
              "subscription":
              {
                "trial_start": 1304627445,
                "trial_end": 1307305845,
                "plan": {
                  "trial_period_days": 31,
                  "amount": 2999,
                  "interval": "month",
                  "id": "silver",
                  "name": "Silver"
                },
              }
            }      
        ) }

        c = Client()
        response = c.post(reverse("zebra:webhooks"), test_post_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.signal_kwargs["full_json"]["subscription"]["trial_end"], 1307305845)



    def test_subscription_final_payment_attempt_failed_signal_fired(self):
        zebra_webhook_subscription_final_payment_attempt_failed.connect(self._signal_reciever)

        self.assertEqual(self.signal_kwargs, None)

        # Pulled directly from the stripe docs
        test_post_data = {'json': simplejson.dumps(
            {
              "customer":1083,
              "event":"subscription_final_payment_attempt_failed",
              "subscription": {
                "status": "canceled",
                "start": 1304585542,
                "plan": {
                  "amount": 2000,
                  "interval": "month",
                  "object": "plan",
                  "id": "p_ag2NgWECmJ",
                  "id": "silver"
                },
                "canceled_at": 1304585552,
                "ended_at": 1304585552,
                "object": "subscription",
                "current_period_end": 1307263942,
                "id": "sub_kP4M63kFrb",
                "current_period_start": 1304585542
              }
            } 
        ) }

        c = Client()
        response = c.post(reverse("zebra:webhooks"), test_post_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.signal_kwargs["full_json"]["subscription"]["start"], 1304585542)


    def test_webhooks_return_valid_customer_obj(self):
        zebra_webhook_subscription_trial_ending.connect(self._signal_reciever)

        from zebra.models import Customer
        cust = Customer.objects.create()
        
        # since ZEBRA_AUTO_CREATE_STRIPE_CUSTOMERS is on (default), this creates a customer
        cust.stripe_customer

        self.assertEqual(self.signal_kwargs, None)

        # Pulled directly from the stripe docs
        test_post_data = {'json': simplejson.dumps(
            {
              "customer":cust.stripe_customer_id,
              "event":"subscription_trial_ending",
              "subscription":
              {
                "trial_start": 1304627445,
                "trial_end": 1307305845,
                "plan": {
                  "trial_period_days": 31,
                  "amount": 2999,
                  "interval": "month",
                  "id": "silver",
                  "name": "Silver"
                },
              }
            }      
        ) }

        c = Client()
        response = c.post(reverse("zebra:webhooks"), test_post_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.signal_kwargs["customer"], cust)

    def test_webhooks_return_valid_customer_obj_as_an_arg(self):
        zebra_webhook_subscription_trial_ending.connect(self._customized_signal_reciever)

        from zebra.models import Customer
        cust = Customer.objects.create()
        
        # since ZEBRA_AUTO_CREATE_STRIPE_CUSTOMERS is on (default), this creates a customer
        cust.stripe_customer

        self.assertEqual(self.signal_kwargs, None)

        # Pulled directly from the stripe docs
        test_post_data = {'json': simplejson.dumps(
            {
              "customer":cust.stripe_customer_id,
              "event":"subscription_trial_ending",
              "subscription":
              {
                "trial_start": 1304627445,
                "trial_end": 1307305845,
                "plan": {
                  "trial_period_days": 31,
                  "amount": 2999,
                  "interval": "month",
                  "id": "silver",
                  "name": "Silver"
                },
              }
            }      
        ) }

        c = Client()
        response = c.post(reverse("zebra:webhooks"), test_post_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.customer, cust)

      
 

    def test_ping_webhook_signal_fired(self):
        zebra_webhook_subscription_ping_sent.connect(self._signal_reciever)

        self.assertEqual(self.signal_kwargs, None)

        # Pulled directly from the stripe docs
        test_post_data = {'json': simplejson.dumps(
            {
              "event":"ping",
            }        
        ) }

        c = Client()
        response = c.post(reverse("zebra:webhooks"), test_post_data)

        self.assertEqual(response.status_code, 200)
