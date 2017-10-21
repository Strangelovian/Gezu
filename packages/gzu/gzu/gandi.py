import pprint
import xmlrpc.client

from .settings import *

logger = logging.getLogger('gandi')
pp = pprint.PrettyPrinter(indent=4)

def shouldUpdateWanV4Address(wanV4Adress):
    api = xmlrpc.client.ServerProxy(Gzu.GANDI_XMLRPC_URL)
    logger.debug(api.version.info(Gzu.GANDI_API_KEY))
    logger.debug(pp.pformat(api.domain.zone.list(Gzu.GANDI_API_KEY)))

    A_records = api.domain.zone.record.list(Gzu.GANDI_API_KEY, Gzu.GANDI_ZONE_ID, 0, {'type': ['A']})
    logger.debug(pp.pformat(A_records))

    for A_record in A_records:
        if A_record['value'] != wanV4Adress:
            logger.info('wan v4 address ' + wanV4Adress + ' mismatches with zone record ' + A_record['value'])
            return True

    return False


def doUpdateWanV4Address(wanV4Adress):
    api = xmlrpc.client.ServerProxy(Gzu.GANDI_XMLRPC_URL)
    logger.debug(api.version.info(Gzu.GANDI_API_KEY))

    new_version_id = api.domain.zone.version.new(Gzu.GANDI_API_KEY, Gzu.GANDI_ZONE_ID)
    new_A_records = api.domain.zone.record.list(Gzu.GANDI_API_KEY, Gzu.GANDI_ZONE_ID, new_version_id, {'type': ['A']})

    for new_A_record in new_A_records:
        api.domain.zone.record.update(
            Gzu.GANDI_API_KEY,
            Gzu.GANDI_ZONE_ID,
            new_version_id,
            {
                'id': new_A_record['id']
            },
            {
                'name': new_A_record['name'],
                'type': new_A_record['type'],
                'value': wanV4Adress,
                'ttl': new_A_record['ttl']
            }
        )

    api.domain.zone.version.set(Gzu.GANDI_API_KEY, Gzu.GANDI_ZONE_ID, new_version_id)
