"""
Device and Identity Correlation Module
Detect linked accounts based on shared devices or IPs.
"""
from collections import defaultdict

def simulate_device_data(transactions):
    """
    Simulate device data for transactions.

    Args:
        transactions (list): List of transactions, where each transaction is a tuple (account, ip_address, device_id, user_agent).

    Returns:
        dict: Simulated device data.
    """
    device_data = defaultdict(list)
    for account, ip_address, device_id, user_agent in transactions:
        device_data[account].append({
            "ip_address": ip_address,
            "device_id": device_id,
            "user_agent": user_agent
        })
    return device_data

def detect_linked_accounts(device_data):
    """
    Detect linked accounts based on shared devices or IPs.

    Args:
        device_data (dict): Device data for accounts.

    Returns:
        list: List of linked accounts with risk flags.
    """
    ip_to_accounts = defaultdict(set)
    device_to_accounts = defaultdict(set)

    for account, devices in device_data.items():
        for device in devices:
            ip_to_accounts[device["ip_address"]].add(account)
            device_to_accounts[device["device_id"]].add(account)

    linked_accounts = []

    # Detect accounts sharing the same IP
    for ip, accounts in ip_to_accounts.items():
        if len(accounts) > 1:
            linked_accounts.append({
                "type": "shared_ip",
                "ip_address": ip,
                "accounts": list(accounts),
                "risk_flag": "MEDIUM"
            })

    # Detect accounts sharing the same device
    for device, accounts in device_to_accounts.items():
        if len(accounts) > 1:
            linked_accounts.append({
                "type": "shared_device",
                "device_id": device,
                "accounts": list(accounts),
                "risk_flag": "HIGH"
            })

    return linked_accounts

# Example usage
if __name__ == "__main__":
    transactions = [
        ("A", "192.168.1.1", "device123", "Mozilla/5.0"),
        ("B", "192.168.1.1", "device456", "Mozilla/5.0"),
        ("C", "192.168.1.2", "device123", "Mozilla/5.0"),
        ("D", "192.168.1.3", "device789", "Mozilla/5.0"),
        ("E", "192.168.1.3", "device789", "Mozilla/5.0")
    ]

    device_data = simulate_device_data(transactions)
    linked_accounts = detect_linked_accounts(device_data)
    for linked in linked_accounts:
        print(linked)