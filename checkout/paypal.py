import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "ARoU-lpNTiZVcYSNz0r2ea2GQelCaP1ZQBDh8spg_1usRUfqeM2XEWoSeQ6GrxiZsdcpV32SsHdCETzm"
        self.client_secret = "EAl7d-FNOC5E8tfKwSCK0ljy_tQMRGKW1FwRu5hjNUk1Z7TW5ak1669zL976v-9RJVbr1UQNTMwvLFap"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)