# Define the impressions dictionary
impressions = {'id': 'id1', 'name': 'name1', 'ip': '<ip_address>'}

# Define the clicks dictionary
clicks = {'id': 'id2', 'name': 'name2', 'ip': '<ip_address>'}

# Define additional information dictionary
additional_info = {'ip': '<ip_address>', 'browser': 'b1', 'os': 'os1'}

# Initialize the output dictionary
output = {'os': additional_info['os'], 'browser': additional_info['browser'], 'impressions': [], 'clicks': [], 'matching_ids': []}

# Check if the IP address matches for impressions and clicks
if impressions['ip'] == additional_info['ip'] and clicks['ip'] == additional_info['ip']:
    # Add impression information to the output
    output['impressions'].append({'id': impressions['id'], 'name': impressions['name']})
    
    # Add click information to the output
    output['clicks'].append({'id': clicks['id'], 'name': clicks['name']})

    # Check if there is a common ID between impressions and clicks
    if impressions['id'] == clicks['id']:
        # Add the common ID to the matching_ids list
        output['matching_ids'].append(impressions['id'])

# Print the final output
print(output)
