import numpy as np

def normalize_numeric_feature(value, min_val, max_val):
    value = max(min_val, min(max_val, value))
    return (value - min_val) / (max_val - min_val)

def normalize_readable_request(raw_request):
    max_url_length = 2000
    max_header_count = 50
    max_body_length = 10000
    max_user_agent_length = 200

    features = []

    method_map = {'GET':0, 'POST':1}
    method_val = method_map.get(raw_request.get('method','GET').upper(), 0.5)
    features.append(method_val)

    url_len = raw_request.get('url_length',0)
    features.append(normalize_numeric_feature(url_len, 0, max_url_length))

    header_count = raw_request.get('header_count',0)
    features.append(normalize_numeric_feature(header_count, 0, max_header_count))

    body_len = raw_request.get('body_length',0)
    features.append(normalize_numeric_feature(body_len, 0, max_body_length))

    has_cookie = 1 if raw_request.get('has_cookie', False) else 0
    features.append(has_cookie)

    ua_len = raw_request.get('user_agent_length',0)
    features.append(normalize_numeric_feature(ua_len, 0, max_user_agent_length))

    suspicious_chars = ['<', '>', '{', '}', '`', '$']
    url = raw_request.get('url', '')
    suspicious_flag = 1 if any(c in url for c in suspicious_chars) else 0
    features.append(suspicious_flag)

    features.append(normalize_numeric_feature(len(raw_request.get('query_string','')), 0, 500))
    features.append(1 if 'select' in raw_request.get('url','').lower() else 0)
    features.append(1 if 'script' in raw_request.get('url','').lower() else 0)
    features.append(1 if raw_request.get('content_type','') == 'application/json' else 0)
    features.append(0)  
    return np.array(features, dtype=np.float32)


def normalize_unreadable_request(raw_metadata):
    max_packet_size = 1500
    max_time_ms = 10000
    max_tls_version = 1.3  

    features = []

    packet_size = raw_metadata.get('packet_size', 0)
    features.append(normalize_numeric_feature(packet_size, 0, max_packet_size))

    encrypted = 1 if raw_metadata.get('encrypted', False) else 0
    features.append(encrypted)

    tls_version = raw_metadata.get('tls_version', 1.2)
    features.append(normalize_numeric_feature(tls_version, 1.0, max_tls_version))

    cipher_suite = raw_metadata.get('cipher_suite', 0)
    features.append(normalize_numeric_feature(cipher_suite, 0, 65535))

    flags = raw_metadata.get('flags', 0)
    flags_bits = [(flags >> i) & 1 for i in range(3)]
    features.extend(flags_bits)

    time_since_last = raw_metadata.get('time_since_last_packet_ms', 0)
    features.append(normalize_numeric_feature(time_since_last, 0, max_time_ms))

    features.append(0)

    return np.array(features, dtype=np.float32)
