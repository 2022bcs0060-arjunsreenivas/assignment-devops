import logging
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

def compute_risk(customer):
    now = datetime.now()
    cutoff = now - timedelta(days=30)

    recent_tickets = [t for t in customer.tickets if t.date > cutoff]

    logger.info(f"Recent tickets count: {len(recent_tickets)}")

    if len(recent_tickets) > 5:
        logger.info("Rule triggered: HIGH risk (ticket count)")
        return "HIGH"

    if (customer.monthly_charges > customer.previous_month_charges) and len(recent_tickets) >= 3:
        logger.info("Rule triggered: MEDIUM risk (charge increase + tickets)")
        return "MEDIUM"

    if customer.contract_type.lower() == "month-to-month":
        if any(t.type == "complaint" for t in customer.tickets):
            logger.info("Rule triggered: HIGH risk (contract + complaint)")
            return "HIGH"

    logger.info("Rule triggered: LOW risk (default)")
    return "LOW"