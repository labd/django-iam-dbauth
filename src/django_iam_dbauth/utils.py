import dns.name
import dns.rdatatype
import dns.resolver
from django.db.utils import OperationalError
from dns.exception import DNSException


def resolve_cname(hostname):
    """Resolve a CNAME record to the original RDS endpoint.

    This is required for AWS where the hostname of the RDS instance is part of
    the signing request.

    Looking for the endpoint which is of the form cluster-name.accountandregionhash.regionid.rds.amazonaws.com
    To do so, recursively resolve the host name until it's a subdomain of rds.amazonaws.com.
    """
    base_domain = dns.name.from_text("rds.amazonaws.com")
    answer = dns.name.from_text(hostname)
    while not answer.is_subdomain(base_domain):
        try:
            # Replace deprecated `query` with `resolve`
            # There is one and only one answer for a CNAME and its type is CNAME.
            # If the name doesn't exist or exists with a different type, an exception is raised.
            answer = dns.resolver.resolve(answer, dns.rdatatype.CNAME, search=True)[
                0
            ].target
        except DNSException as e:
            # Break when resolution doesn't work.
            # This avoids cryptic authentication failures from RDS.
            raise OperationalError("Failed to resolve hostname to RDS endpoint.") from e

    return answer.to_text().strip(".")
